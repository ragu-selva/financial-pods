"""Sprint 02 runtime proofs against immutable, human-approved source and fact artifacts."""

from __future__ import annotations

import ast
import json
import socket
from dataclasses import FrozenInstanceError, replace
from datetime import date
from decimal import Decimal, getcontext, localcontext
from pathlib import Path
from typing import cast

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from financial_pods_finance_engine.primitives import Currency, Money
from financial_pods_finance_engine.regulatory import (
    RegulatoryEngine,
    RegulatoryError,
    RulesetRegistry,
    error_to_json,
    result_to_dict,
    result_to_json,
    snapshot_from_dict,
)
from financial_pods_finance_engine.regulatory.arithmetic import multiply_money
from financial_pods_finance_engine.regulatory.contracts import (
    CalculationTrace,
    RegulatoryFact,
    RegulatoryFactSnapshot,
    RiskWeight,
    RulesetIdentity,
)
from financial_pods_finance_engine.regulatory.errors import ErrorCode
from financial_pods_finance_engine.regulatory.serialization import encode, parse_json, snapshot_hash
from financial_pods_finance_engine.regulatory.us_sources import (
    GOLDEN_HASH,
    MANIFEST_HASH,
    RULE_IDS,
    US_VERSION,
    USSourcePackage,
    load_golden_snapshot,
    load_us_source_package,
)
from financial_pods_finance_engine.regulatory.us_standardized import USStandardizedRuleset

REPOSITORY = Path(__file__).resolve().parents[3]
SPRINT = REPOSITORY / "sprints" / "sprint-02"
APPROVED_GOLDEN = json.loads((SPRINT / "GOLDEN_CASE_APPROVED.json").read_text(encoding="utf-8"))
GROUPS = APPROVED_GOLDEN["fact_groups"]
DEFINITIONS = [
    "definition." + item["concept"]
    for row in APPROVED_GOLDEN["definition_screen"]
    for item in row["alternative_assessments"]
]
REQUIRED = (
    [group + "." + key for group, body in GROUPS.items() for key in body["facts"]]
    + [
        "exposure." + key
        for key in APPROVED_GOLDEN["exposure_facts"]
        if not key.endswith("_review")
    ]
    + DEFINITIONS
)
AMOUNTS = {
    "accounting.original_principal",
    "accounting.outstanding_principal",
    "accounting.gross_amortized_cost",
    "accounting.net_balance_sheet_amount_candidate",
    "accounting.gaap_based_regulatory_carrying_value_candidate",
    "exposure.original_principal",
    "exposure.outstanding_balance",
    "exposure.gaap_carrying_value",
}


@pytest.fixture(scope="module")
def package() -> USSourcePackage:
    return load_us_source_package(SPRINT)


@pytest.fixture(scope="module")
def snapshot(package: USSourcePackage) -> RegulatoryFactSnapshot:
    return load_golden_snapshot(REPOSITORY, package)


def engine(package: USSourcePackage, **kwargs: tuple[str, ...]) -> RegulatoryEngine:
    return RegulatoryEngine(
        RulesetRegistry(
            providers=(USStandardizedRuleset(package),),
            prohibited_versions=kwargs.get("prohibited_versions", ("R-1888-PROPOSAL",)),
            revoked_versions=kwargs.get("revoked_versions", ()),
        )
    )


def change(
    snapshot: RegulatoryFactSnapshot, path: str, value: str | bool | int | Money
) -> RegulatoryFactSnapshot:
    assert path in {item.path for item in snapshot.facts}
    return replace(
        snapshot,
        facts=tuple(
            replace(item, value=value) if item.path == path else item for item in snapshot.facts
        ),
    )


def with_amount(snapshot: RegulatoryFactSnapshot, amount: str) -> RegulatoryFactSnapshot:
    value = Money(Decimal(amount), Currency("USD"))
    return replace(
        snapshot,
        facts=tuple(
            replace(
                item,
                value=value,
                provenance=replace(
                    item.provenance,
                    source_ref="Sprint02-runtime-test:" + item.path,
                    source_version="sprint-02-owner-authorized-alternate-amount.v1",
                    assumption_id="TEST-ALTERNATE-AMOUNT:" + item.path,
                ),
            )
            if item.path in AMOUNTS
            else item
            for item in snapshot.facts
        ),
    )


def assert_failure(
    package: USSourcePackage, facts: RegulatoryFactSnapshot, codes: set[ErrorCode]
) -> RegulatoryError:
    with pytest.raises(RegulatoryError) as caught:
        engine(package).calculate(facts)
    error = caught.value
    assert error.code in codes
    payload = json.loads(error_to_json(error))
    assert set(payload) == {"code", "field_path", "message", "rule_refs", "validation_trace"}
    assert payload["validation_trace"]["steps"][-1]["output"]["code"] == error.code
    assert error.validation_trace is not None
    assert tuple(step.sequence for step in error.validation_trace.steps) == tuple(
        range(1, len(error.validation_trace.steps) + 1)
    )
    return error


def test_golden_runtime_matches_reviewed_values(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot
) -> None:
    result = engine(package).calculate(snapshot)
    actual = result_to_dict(result)
    expected = APPROVED_GOLDEN["expected_result"]
    assert actual["schema_version"] == "regulatory-calculation.v1"
    assert result.classification.exposure_class == expected["classification"]["exposure_class"]
    assert result.classification.subclass == "GENERAL_CORPORATE"
    measure = cast(dict[str, object], actual["regulatory_exposure_measure"])
    for key in ("amount", "currency", "measure_type", "measurement_basis"):
        assert measure[key] == expected["regulatory_exposure_measure"][key]
    assert set(measure) == {
        "amount",
        "currency",
        "measure_type",
        "measurement_basis",
        "rule_refs",
        "warnings",
    }
    assert result.risk_weight.value == Decimal("1.00")
    assert result.risk_weight.unit == "RATIO"
    assert result.rwa.amount == Decimal("10000000.00")
    teaching = result.capital_teaching_outputs
    assert len(teaching) == 1
    assert teaching[0].name == "baseline_total_capital_equivalent"
    assert teaching[0].amount == Decimal("800000.00")
    assert teaching[0].ratio == Decimal("0.08")
    assert set(expected["capital_teaching_outputs"][0]["warnings"]) <= set(teaching[0].warnings)
    assert "NOT_ECONOMIC_CAPITAL" in teaching[0].warnings
    assert "NOT_COMPLETE_REQUIRED_REGULATORY_CAPITAL" in teaching[0].warnings
    assert "ead" not in actual and "exposure_amount" not in actual
    assert actual["ruleset_version"] == US_VERSION
    assert actual["manifest_hash"] == MANIFEST_HASH
    assert len(result.input_snapshot_hash) == 64
    assert set(dict(result.rule_versions)) == set(RULE_IDS)
    assert result.regulatory_exposure_measure.rule_refs[0].rule_id == "US-MEASURE"
    assert result.risk_weight.rule_refs[0].rule_id == "US-CORP-RW"


def test_name_and_ids_do_not_choose_rules_or_affect_authoritative_serialization(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
) -> None:
    alternate = replace(
        snapshot,
        metadata=replace(
            snapshot.metadata,
            borrower_name="Beta Industrial Components",
            counterparty_id="CP-BETA",
            case_id="CASE-BETA",
            calculation_id="caller-123",
        ),
    )
    one, two = engine(package).calculate(snapshot), engine(package).calculate(alternate)
    assert snapshot_hash(snapshot) == snapshot_hash(alternate)
    assert result_to_json(one) == result_to_json(two)
    assert one.calculation_trace == two.calculation_trace
    assert result_to_json(one, include_metadata=True) != result_to_json(two, include_metadata=True)


def test_five_million_uses_same_orchestration(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot
) -> None:
    alternate = with_amount(snapshot, "5000000.00")
    one, two = engine(package).calculate(snapshot), engine(package).calculate(alternate)
    assert two.risk_weight.value == Decimal("1.00")
    assert two.rwa.amount == Decimal("5000000.00")
    assert two.capital_teaching_outputs[0].amount == Decimal("400000.00")
    assert [step.operation for step in one.calculation_trace.steps] == [
        step.operation for step in two.calculation_trace.steps
    ]
    assert one.input_snapshot_hash != two.input_snapshot_hash


@pytest.mark.parametrize("path", REQUIRED)
def test_every_required_fact_missing_fails_closed(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot, path: str
) -> None:
    facts = replace(snapshot, facts=tuple(item for item in snapshot.facts if item.path != path))
    error = assert_failure(package, facts, {ErrorCode.MISSING_REQUIRED_FACT})
    assert error.field_path == path


@pytest.mark.parametrize("path", DEFINITIONS)
@pytest.mark.parametrize("value", ["UNKNOWN", True])
def test_every_corporate_exclusion_is_required_negative(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    path: str,
    value: str | bool,
) -> None:
    assert_failure(
        package,
        change(snapshot, path, value),
        {ErrorCode.UNKNOWN_FACT, ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE},
    )


@pytest.mark.parametrize(
    ("path", "value"),
    [
        ("institution.cblr_elected", True),
        ("institution.cblr_grace_period", True),
        ("institution.cblr_ever_elected", True),
        ("institution.state_member_bank", False),
        ("counterparty.national_or_state_bank_or_banking_association", True),
        ("counterparty.receives_deposits", True),
        ("counterparty.foreign_bank_or_bank_branch_or_agency", True),
        ("counterparty.federal_or_state_credit_union_charter", True),
        ("counterparty.government_established_or_chartered_public_purpose_enterprise", True),
        ("ppp.ppp_loan", True),
        ("ppp.originated_under_15_usc_636_a_36", True),
        ("market_risk.managed_as_trading", True),
        ("market_risk.hedges_another_covered_position", True),
        ("market_risk.foreign_exchange_position", True),
        ("other_scope.real_estate_collateral", True),
        ("other_scope.real_estate_acquisition_development_or_construction_purpose", True),
        ("other_scope.cash_collateral_to_ccp", True),
        ("other_scope.cleared_transaction", True),
        ("other_scope.guarantee", True),
        ("other_scope.collateral", True),
        ("other_scope.crm_recognition", True),
        ("other_scope.netting", True),
        ("exposure.nonaccrual", True),
        ("exposure.past_due", True),
        ("exposure.days_past_due", 90),
        ("exposure.defaulted", True),
        ("exposure.product_type", "DERIVATIVE"),
        ("exposure.off_balance_sheet", True),
        ("exposure.on_balance_sheet", False),
        ("accounting.pcd", True),
        ("accounting.fair_value_option", True),
        ("accounting.held_for_sale", True),
    ],
)
def test_material_excluded_paths_never_get_alternative_rates(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    path: str,
    value: str | bool | int,
) -> None:
    assert_failure(
        package,
        change(snapshot, path, value),
        {
            ErrorCode.INSTITUTION_OUT_OF_SCOPE,
            ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE,
            ErrorCode.CONFLICTING_FACTS,
        },
    )


@pytest.mark.parametrize(
    "path",
    [
        "accounting.credit_loss_allowance",
        "accounting.partial_write_offs",
        "accounting.unamortized_premium",
        "accounting.unamortized_deferred_fees",
        "accounting.accrued_interest_receivable",
        "exposure.gaap_carrying_value",
    ],
)
def test_nonzero_adjustments_or_inconsistent_measure_require_new_review(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    path: str,
) -> None:
    assert_failure(
        package,
        change(snapshot, path, Money(Decimal("1.00"), Currency("USD"))),
        {ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE, ErrorCode.CONFLICTING_FACTS},
    )


@pytest.mark.parametrize(
    ("field", "value", "code"),
    [
        ("jurisdiction", "BCBS", ErrorCode.UNSUPPORTED_JURISDICTION),
        ("jurisdiction", "SAMA", ErrorCode.UNSUPPORTED_JURISDICTION),
        ("regulator", "FDIC", ErrorCode.UNSUPPORTED_JURISDICTION),
        ("regime", "IRB", ErrorCode.UNSUPPORTED_JURISDICTION),
        ("as_of_date", date(2024, 12, 31), ErrorCode.RULESET_NOT_EFFECTIVE),
        ("as_of_date", date(2025, 1, 2), ErrorCode.RULESET_NOT_EFFECTIVE),
        ("as_of_date", date(2026, 3, 19), ErrorCode.RULESET_NOT_EFFECTIVE),
        ("ruleset_version", "UNKNOWN", ErrorCode.UNKNOWN_RULESET),
        ("ruleset_version", "US_STANDARDIZED_CURRENT", ErrorCode.UNKNOWN_RULESET),
        ("ruleset_version", "R-1888-PROPOSAL", ErrorCode.RULESET_STATUS_NOT_EXECUTABLE),
    ],
)
def test_exact_context_selection(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    field: str,
    value: str | date,
    code: ErrorCode,
) -> None:
    context = snapshot.context
    if field == "as_of_date":
        context = replace(context, as_of_date=cast(date, value))
    elif field == "jurisdiction":
        context = replace(context, jurisdiction=cast(str, value))
    elif field == "regulator":
        context = replace(context, regulator=cast(str, value))
    elif field == "regime":
        context = replace(context, regime=cast(str, value))
    else:
        assert field == "ruleset_version"
        context = replace(context, ruleset_version=cast(str, value))
    changed = replace(snapshot, context=context)
    assert_failure(package, changed, {code})


def test_registry_ambiguity_and_revocation(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot
) -> None:
    provider = USStandardizedRuleset(package)
    with pytest.raises(RegulatoryError, match="AMBIGUOUS_RULESET"):
        RegulatoryEngine(RulesetRegistry(providers=(provider, provider))).calculate(snapshot)
    with pytest.raises(RegulatoryError, match="RULESET_NOT_APPROVED"):
        engine(package, revoked_versions=(US_VERSION,)).calculate(snapshot)


@pytest.mark.parametrize("status", ["PROPOSED", "FUTURE", "SUPERSEDED"])
def test_noncurrent_provider_cannot_use_current_alias(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    status: str,
) -> None:
    class OtherLifecycle(USStandardizedRuleset):
        @property
        def identity(self) -> RulesetIdentity:
            return replace(super().identity, legal_status=status)

    registry = RulesetRegistry(providers=(OtherLifecycle(package),))
    with pytest.raises(RegulatoryError, match="RULESET_STATUS_NOT_EXECUTABLE"):
        RegulatoryEngine(registry).calculate(snapshot)


@pytest.mark.parametrize("field", ["manifest", "baseline", "golden", "approval"])
def test_approved_artifact_tampering_fails(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot, field: str
) -> None:
    changed = replace(package, **{field: getattr(package, field) + b" "})
    assert_failure(changed, snapshot, {ErrorCode.SOURCE_HASH_MISMATCH})


def test_each_capture_is_checked_not_only_metadata(package: USSourcePackage) -> None:
    for index, blob in enumerate(package.captures):
        changed = replace(
            package,
            captures=(
                *package.captures[:index],
                replace(blob, content=blob.content + b"x"),
                *package.captures[index + 1 :],
            ),
        )
        with pytest.raises(RegulatoryError, match="SOURCE_HASH_MISMATCH"):
            changed.validate()
    for captures in (package.captures[:-1], (*package.captures, package.captures[0])):
        with pytest.raises(RegulatoryError, match="SOURCE_EVIDENCE_INCOMPLETE"):
            replace(package, captures=captures).validate()


def test_unapproved_rule_and_newer_proposed_rate_cannot_replace_2025(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
) -> None:
    original = json.loads(package.manifest)
    for field, value, code in (
        ("review_status", "PENDING_REVIEW", ErrorCode.RULESET_NOT_APPROVED),
        ("legal_status", "PROPOSED", ErrorCode.RULESET_STATUS_NOT_EXECUTABLE),
        ("approved_for_execution_evidence", False, ErrorCode.RULESET_NOT_APPROVED),
    ):
        manifest = json.loads(package.manifest)
        rule = next(item for item in manifest["approved_rules"] if item["rule_id"] == "US-CORP-RW")
        rule[field] = value
        rule["proposed_risk_weight"] = "0.65"  # adversarial test value, not a legal assertion
        changed = replace(package, manifest=json.dumps(manifest).encode())
        assert_failure(changed, snapshot, {code})
    manifest = json.loads(package.manifest)
    rule = next(item for item in manifest["approved_rules"] if item["rule_id"] == "US-CORP-RW")
    rule["source_refs"][0]["source_id"] = "R-1888-PROPOSAL"
    assert_failure(
        replace(package, manifest=json.dumps(manifest).encode()),
        snapshot,
        {ErrorCode.RULESET_STATUS_NOT_EXECUTABLE},
    )
    # Even relabelled CURRENT/APPROVED proposal text cannot match the approved manifest hash.
    original["approved_rules"][3]["interpretation"] = "Newer proposed corporate rate 0.65"
    assert_failure(
        replace(package, manifest=json.dumps(original).encode()),
        snapshot,
        {ErrorCode.SOURCE_HASH_MISMATCH},
    )
    assert engine(package).calculate(snapshot).risk_weight.value == Decimal("1.00")


def test_trace_is_ordered_typed_and_bound_to_sources(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot
) -> None:
    result = engine(package).calculate(snapshot)
    trace = result.calculation_trace
    assert len(trace.steps) == 12
    assert [step.sequence for step in trace.steps] == list(range(1, 13))
    assert trace.steps[7].output == result.regulatory_exposure_measure
    assert trace.steps[8].output == result.risk_weight
    assert trace.steps[9].inputs_used == ("regulatory_exposure_measure", "risk_weight")
    assert trace.steps[9].output == result.rwa
    assert trace.steps[10].output == result.capital_teaching_outputs[0]
    for step in trace.steps:
        if step.sequence in (1, 2, 3, 12):
            assert not step.rule_refs and step.engine_contract == "regulatory-engine.v1"
        else:
            assert step.rule_refs and step.engine_contract is None
        for ref in step.rule_refs:
            assert ref.rule_id in RULE_IDS and ref.authority
            assert ref.locators and ref.citations
            assert ref.approved_as_of == date(2025, 1, 1)
            assert ref.effective_to is None
            assert ref.effective_to_status == "UNKNOWN_NOT_OPEN_ENDED"
            assert ref.reviewer_name == "Ragunath Selvaraj"
            for citation in ref.citations:
                assert citation.source_id != "R-1888-PROPOSAL"
                assert len(citation.content_sha256) == 64
                assert citation.canonical_source.startswith("https://")
    assert len({item.source_id for item in result.source_citations}) == len(result.source_citations)


def test_runtime_immutability_and_strict_construction(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
) -> None:
    result = engine(package).calculate(snapshot)
    with pytest.raises(FrozenInstanceError):
        result.rwa.amount = Decimal("1")  # type: ignore[misc]
    with pytest.raises(RegulatoryError, match="INVALID_TYPE"):
        replace(snapshot, facts=cast(tuple[RegulatoryFact, ...], list(snapshot.facts)))
    with pytest.raises(RegulatoryError, match="INVALID_TYPE"):
        replace(result.calculation_trace, steps=cast(tuple, list(result.calculation_trace.steps)))  # type: ignore[type-arg]
    with pytest.raises(RegulatoryError, match="INVALID_TYPE"):
        replace(result.regulatory_exposure_measure, rule_refs=cast(tuple, []))  # type: ignore[type-arg]
    with pytest.raises(RegulatoryError, match="INVALID_TYPE"):
        RiskWeight(value=cast(Decimal, 0.08), rule_refs=())
    with pytest.raises(RegulatoryError, match="INVALID_PROVENANCE"):
        replace(snapshot, facts=(*snapshot.facts, snapshot.facts[0]))
    with pytest.raises(RegulatoryError, match="INVALID_SCHEMA"):
        CalculationTrace(steps=(result.calculation_trace.steps[1],))


def test_strict_json_roundtrip_and_detached_collections(snapshot: RegulatoryFactSnapshot) -> None:
    payload = encode(snapshot)
    result = snapshot_from_dict(payload)
    assert result == snapshot
    assert isinstance(payload, dict)
    payload["facts"] = []
    assert result.facts == snapshot.facts
    with pytest.raises(RegulatoryError):
        parse_json('{"duplicate":1,"duplicate":2}')
    with pytest.raises(RegulatoryError):
        parse_json('{"rate":0.08}')
    with pytest.raises(RegulatoryError):
        parse_json('{"rate":NaN}')


@pytest.mark.parametrize(
    "mutation",
    ["missing", "unknown_field", "schema", "float", "precision", "currency", "provenance"],
)
def test_invalid_json_contract(snapshot: RegulatoryFactSnapshot, mutation: str) -> None:
    payload = json.loads(json.dumps(encode(snapshot)))
    if mutation == "missing":
        del payload["context"]["as_of_date"]
    elif mutation == "unknown_field":
        payload["ead"] = "10000000"
    elif mutation == "schema":
        payload["schema_version"] = "regulatory-facts.v0.1-draft"
    else:
        fact = next(
            item for item in payload["facts"] if item["path"] == "exposure.outstanding_balance"
        )
        if mutation == "float":
            fact["value"]["amount"] = 0.08
        elif mutation == "precision":
            fact["value"]["amount"] = "1.001"
        elif mutation == "currency":
            fact["value"]["currency"] = "EUR"
        else:
            fact["provenance"]["review_status"] = "UNKNOWN"
    with pytest.raises(RegulatoryError):
        snapshot_from_dict(payload)


@pytest.mark.parametrize(
    "label", ["bcbs_sme", "bcbs_external_rating", "specialised_lending", "regulatory_retail"]
)
def test_bcbs_informational_labels_do_not_determine_us_treatment(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    label: str,
) -> None:
    added = RegulatoryFact(
        path="informational." + label, value=True, provenance=snapshot.facts[0].provenance
    )
    result = engine(package).calculate(replace(snapshot, facts=(*snapshot.facts, added)))
    assert result.classification.exposure_class == "CORPORATE"
    assert result.risk_weight.value == Decimal("1.00")
    assert result.rwa.amount == Decimal("10000000.00")


@pytest.mark.parametrize(
    "rounding",
    [
        "ROUND_HALF_EVEN",
        "ROUND_DOWN",
        "ROUND_UP",
        "ROUND_FLOOR",
        "ROUND_CEILING",
        "ROUND_HALF_UP",
        "ROUND_HALF_DOWN",
        "ROUND_05UP",
    ],
)
@pytest.mark.parametrize("traps", [True, False])
def test_whole_calculation_is_independent_of_hostile_decimal_context(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    rounding: str,
    traps: bool,
) -> None:
    expected = result_to_json(engine(package).calculate(snapshot))
    with localcontext() as ctx:
        ctx.prec, ctx.Emin, ctx.Emax, ctx.clamp, ctx.rounding = 1, -2, 2, 1, rounding
        for signal in ctx.traps:
            ctx.traps[signal] = traps
        ctx.clear_flags()
        before = str(getcontext())
        assert result_to_json(engine(package).calculate(snapshot)) == expected
        assert str(getcontext()) == before


@given(dollars=st.integers(min_value=1, max_value=10**25), precision=st.integers(1, 8))
@settings(max_examples=50, deadline=None)
def test_amount_property_no_hardcoded_principal(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    dollars: int,
    precision: int,
) -> None:
    facts = with_amount(snapshot, str(dollars) + ".00")
    with localcontext() as ctx:
        ctx.prec = precision
        result = engine(package).calculate(facts)
    assert result.rwa.amount == Decimal(str(dollars) + ".00")
    parts = Decimal(dollars * 8).as_tuple()
    assert result.capital_teaching_outputs[0].amount == Decimal((parts.sign, parts.digits, -2))


@pytest.mark.parametrize("amount", ["0.01", "0.12", "1.01"])
def test_fractional_cent_teaching_results_are_rejected_without_rounding(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    amount: str,
) -> None:
    error = assert_failure(
        package, with_amount(snapshot, amount), {ErrorCode.ROUNDING_POLICY_UNDEFINED}
    )
    assert error.validation_trace is not None
    assert error.validation_trace.steps[-1].operation == "calculate_educational_capital_equivalent"


def test_no_core_network_or_filesystem_at_calculation_time(
    package: USSourcePackage,
    snapshot: RegulatoryFactSnapshot,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def forbidden(*args: object, **kwargs: object) -> None:
        raise AssertionError("Runtime external access is forbidden")

    monkeypatch.setattr(Path, "read_bytes", forbidden)
    monkeypatch.setattr(Path, "read_text", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)
    assert engine(package).calculate(snapshot).rwa.amount == Decimal("10000000.00")


def test_core_imports_do_not_include_external_services() -> None:
    directory = REPOSITORY / "packages/finance-engine/src/financial_pods_finance_engine/regulatory"
    prohibited = {"requests", "httpx", "redis", "sqlalchemy", "openai", "random", "time", "socket"}
    for path in directory.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                assert not {alias.name.split(".")[0] for alias in node.names} & prohibited
            if isinstance(node, ast.ImportFrom) and node.module:
                assert node.module.split(".")[0] not in prohibited
    generic = (directory / "engine.py").read_text(encoding="utf-8")
    assert "Alpha" not in generic and "US-" not in generic and "0.08" not in generic
    assert MANIFEST_HASH and GOLDEN_HASH


def test_multiply_money_rejects_invalid_ratio() -> None:
    with pytest.raises(RegulatoryError, match="EXCESS_PRECISION"):
        multiply_money(Money(Decimal("100"), Currency("USD")), Decimal("0.0000001"))
    with pytest.raises(RegulatoryError, match="INVALID_TYPE"):
        multiply_money(Money(Decimal("100"), Currency("USD")), Decimal("NaN"))


def test_provider_helpers_reject_incompatible_typed_results(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot
) -> None:
    result = engine(package).calculate(snapshot)
    provider = USStandardizedRuleset(package)
    for classification in (
        replace(result.classification, jurisdiction="BCBS"),
        replace(result.classification, rule_refs=()),
    ):
        with pytest.raises(RegulatoryError, match="UNSUPPORTED_EXPOSURE_SCOPE"):
            provider.resolve_treatment(classification)
    for measure in (
        replace(result.regulatory_exposure_measure, measurement_basis="IRB_EAD"),
        replace(result.regulatory_exposure_measure, amount=Decimal("-1.00")),
        replace(result.regulatory_exposure_measure, rule_refs=()),
    ):
        with pytest.raises(RegulatoryError, match="UNSUPPORTED_EXPOSURE_SCOPE"):
            provider.calculate_rwa(measure, result.risk_weight)
    with pytest.raises(RegulatoryError, match="INVALID_TYPE"):
        replace(result.regulatory_exposure_measure, measure_type="EAD")  # type: ignore[arg-type]
    with pytest.raises(RegulatoryError, match="INVALID_TYPE"):
        replace(result.capital_teaching_outputs[0], name="CET1")  # type: ignore[arg-type]


def test_direct_provider_calls_cannot_bypass_source_verification(
    package: USSourcePackage, snapshot: RegulatoryFactSnapshot
) -> None:
    result = engine(package).calculate(snapshot)
    provider = USStandardizedRuleset(replace(package, manifest=package.manifest + b" "))
    for operation in (
        lambda: provider.classify_exposure(snapshot),
        lambda: provider.resolve_treatment(result.classification),
        lambda: provider.determine_regulatory_exposure_measure(snapshot),
        lambda: provider.determine_risk_weight(snapshot),
        lambda: provider.calculate_rwa(result.regulatory_exposure_measure, result.risk_weight),
        lambda: provider.calculate_capital_teaching_outputs(result.rwa),
    ):
        with pytest.raises(RegulatoryError, match="SOURCE_HASH_MISMATCH"):
            operation()
