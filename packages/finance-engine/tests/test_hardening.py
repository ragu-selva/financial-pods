from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, replace
from decimal import (
    ROUND_05UP,
    ROUND_CEILING,
    ROUND_DOWN,
    ROUND_FLOOR,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_HALF_UP,
    ROUND_UP,
    Decimal,
    getcontext,
    localcontext,
)
from pathlib import Path
from typing import cast

import pytest
from hypothesis import given
from hypothesis import strategies as st

from financial_pods_finance_engine import (
    DomainValidationError,
    FinBankCase,
    Money,
    Percentage,
    SourceKind,
    case_from_dict,
    case_to_dict,
    load_case_fixture,
)
from financial_pods_finance_engine.model import SUPPORTED_PROVENANCE_PATHS
from financial_pods_finance_engine.primitives import Currency

FIXTURE_PATH = (
    Path(__file__).resolve().parents[3] / "data" / "finbank" / "alpha_manufacturing_v1.json"
)
REQUIRED_PATHS = (
    "institution.name",
    "counterparty.legal_name",
    "product.kind",
    "facility.original_principal",
    "facility.origination_date",
    "facility.maturity_date",
    "exposure.as_of_date",
    "exposure.outstanding_principal",
)
ROUNDINGS = (
    ROUND_05UP,
    ROUND_CEILING,
    ROUND_DOWN,
    ROUND_FLOOR,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_HALF_UP,
    ROUND_UP,
)


@contextmanager
def hostile_context(precision: int, rounding: str, traps: bool = True) -> Iterator[None]:
    with localcontext() as context:
        context.prec = precision
        context.rounding = rounding
        context.Emin = -2
        context.Emax = 2
        context.clamp = 1
        for signal in context.traps:
            context.traps[signal] = traps
        context.clear_flags()
        before = str(context)
        yield
        assert str(getcontext()) == before, "domain operations must not modify caller context"


def scaled_integer(value: int, places: int) -> Decimal:
    parts = Decimal(value).as_tuple()
    return Decimal((parts.sign, parts.digits, -places))


@pytest.mark.parametrize("rounding", ROUNDINGS)
@pytest.mark.parametrize("traps", [False, True])
def test_approved_fixture_round_trips_under_hostile_context(rounding: str, traps: bool) -> None:
    expected = case_to_dict(load_case_fixture(FIXTURE_PATH))
    with hostile_context(1, rounding, traps):
        case = load_case_fixture(FIXTURE_PATH)
        assert case_to_dict(case) == expected
        assert case_from_dict(expected) == case
        assert case.facility.original_principal.to_decimal_string() == "10000000.00"
        assert Percentage(Decimal("12.3456")).to_decimal_string() == "12.3456"


@given(
    cents=st.integers(min_value=-(10**50), max_value=10**50),
    other_cents=st.integers(min_value=-(10**50), max_value=10**50),
    millionths=st.integers(min_value=-(10**50), max_value=10**50),
    precision=st.integers(min_value=1, max_value=12),
    rounding=st.sampled_from(ROUNDINGS),
)
def test_primitives_are_exact_under_arbitrary_contexts(
    cents: int, other_cents: int, millionths: int, precision: int, rounding: str
) -> None:
    amount = scaled_integer(cents, 2)
    other_amount = scaled_integer(other_cents, 2)
    rate = scaled_integer(millionths, 6)
    expected_money = format(amount, ".2f")
    expected_percentage = Percentage(rate).to_decimal_string()
    expected_sum = format(scaled_integer(cents + other_cents, 2), ".2f")
    expected_difference = format(scaled_integer(cents - other_cents, 2), ".2f")

    with hostile_context(precision, rounding):
        money = Money(amount, Currency("USD"))
        other = Money(other_amount, Currency("USD"))
        percentage = Percentage(rate)
        assert money.amount == amount
        assert money.to_decimal_string() == expected_money
        assert Money(Decimal(expected_money), money.currency) == money
        assert percentage.value == rate
        assert percentage.to_decimal_string() == expected_percentage
        assert Percentage(Decimal(expected_percentage)) == percentage
        assert (money + other).to_decimal_string() == expected_sum
        assert (money - other).to_decimal_string() == expected_difference
        percentage.require_range(field="rate", minimum=rate, maximum=rate)


@given(
    coefficient=st.integers(min_value=-(10**35), max_value=10**35),
    precision=st.integers(min_value=1, max_value=6),
    rounding=st.sampled_from(ROUNDINGS),
)
def test_excess_precision_never_rounds_into_acceptance(
    coefficient: int, precision: int, rounding: str
) -> None:
    # Last digit is always nonzero, so the value cannot be represented at the allowed scale.
    money_value = scaled_integer(coefficient * 10 + 1, 3)
    percentage_value = scaled_integer(coefficient * 10 + 1, 7)
    with hostile_context(precision, rounding):
        with pytest.raises(DomainValidationError) as money_error:
            Money(money_value, Currency("USD"))
        assert money_error.value.issue.code == "excess_precision"
        with pytest.raises(DomainValidationError) as percentage_error:
            Percentage(percentage_value)
        assert percentage_error.value.issue.code == "excess_precision"


@pytest.mark.parametrize(
    ("text", "money_text", "percentage_text"),
    [
        ("1.230000", "1.23", "1.23"),
        ("-0.0000000000", "-0.00", "0"),
        ("1E+40", "1" + "0" * 40 + ".00", "1" + "0" * 40),
    ],
)
def test_canonicalization_preserves_trailing_zero_policy(
    text: str, money_text: str, percentage_text: str
) -> None:
    with hostile_context(1, ROUND_UP):
        assert Money(Decimal(text), Currency("USD")).to_decimal_string() == money_text
        assert Percentage(Decimal(text)).to_decimal_string() == percentage_text


@pytest.mark.parametrize("text", ["NaN", "sNaN", "Infinity", "-Infinity"])
def test_nonfinite_values_have_stable_domain_errors(text: str) -> None:
    with hostile_context(1, ROUND_DOWN):
        with pytest.raises(DomainValidationError) as money_error:
            Money(Decimal(text), Currency("USD"))
        with pytest.raises(DomainValidationError) as percentage_error:
            Percentage(Decimal(text))
        assert money_error.value.issue.code == "non_finite_decimal"
        assert percentage_error.value.issue.code == "non_finite_decimal"


def approved_case() -> FinBankCase:
    return load_case_fixture(FIXTURE_PATH)


@pytest.mark.parametrize("path", REQUIRED_PATHS)
def test_each_case_fact_requires_provenance(path: str) -> None:
    case = approved_case()
    with pytest.raises(DomainValidationError) as error:
        replace(case, provenance=tuple(item for item in case.provenance if item.field_path != path))
    assert error.value.issue.code == "missing_provenance_coverage"
    assert error.value.issue.field == "provenance"
    assert path in error.value.issue.message


@given(st.sets(st.sampled_from(REQUIRED_PATHS), min_size=1, max_size=7))
def test_any_incomplete_nonempty_coverage_is_rejected(paths: set[str]) -> None:
    case = approved_case()
    with pytest.raises(DomainValidationError) as error:
        replace(
            case, provenance=tuple(item for item in case.provenance if item.field_path in paths)
        )
    assert error.value.issue.code == "missing_provenance_coverage"


@pytest.mark.parametrize(
    "path",
    [
        "does.not.exist",
        "facility",
        "facility..id",
        "facility[0].id",
        "facility.__class__",
        "facility.original_principal.nope",
        "facility.rwa",
        "assumptions[0].value",
        "provenance",
        "facility.origination_date.year",
        "institution.Name",
    ],
)
def test_invalid_paths_are_rejected_even_with_complete_coverage(path: str) -> None:
    case = approved_case()
    item = replace(case.provenance[0], field_path=path)
    with pytest.raises(DomainValidationError) as error:
        replace(case, provenance=(*case.provenance, item))
    assert error.value.issue.code == "unsupported_provenance_path"
    assert error.value.issue.field == "provenance.field_path"


@pytest.mark.parametrize("path", ["", " facility.origination_date", "facility.origination_date "])
def test_untrimmed_or_empty_paths_are_rejected(path: str) -> None:
    with pytest.raises(DomainValidationError) as error:
        replace(approved_case().provenance[0], field_path=path)
    assert error.value.issue.code == "invalid_text"


def test_duplicate_provenance_and_assumptions_remain_rejected() -> None:
    case = approved_case()
    with pytest.raises(DomainValidationError) as error:
        replace(case, provenance=(*case.provenance, case.provenance[0]))
    assert error.value.issue.code == "duplicate_provenance"
    with pytest.raises(DomainValidationError) as error:
        replace(case, assumptions=(*case.assumptions, case.assumptions[0]))
    assert error.value.issue.code == "duplicate_assumption"


@pytest.mark.parametrize("path", sorted(SUPPORTED_PROVENANCE_PATHS))
def test_every_supported_path_resolves_in_schema_and_can_be_provenanced(path: str) -> None:
    case = approved_case()
    value: object = case_to_dict(case)
    for component in path.split("."):
        assert isinstance(value, dict)
        assert component in value
        value = value[component]
    if path not in REQUIRED_PATHS:
        item = replace(case.provenance[0], field_path=path)
        expanded = replace(case, provenance=(*case.provenance, item))
        assert case_from_dict(case_to_dict(expanded)) == expanded


def test_money_child_paths_do_not_replace_required_pair_coverage() -> None:
    case = approved_case()
    retained = tuple(
        item for item in case.provenance if item.field_path != "facility.original_principal"
    )
    children = tuple(
        replace(case.provenance[0], field_path=f"facility.original_principal.{component}")
        for component in ("amount", "currency")
    )
    with pytest.raises(DomainValidationError) as error:
        replace(case, provenance=(*retained, *children))
    assert error.value.issue.code == "missing_provenance_coverage"


def test_json_boundary_enforces_the_same_provenance_coverage_and_paths() -> None:
    payload = case_to_dict(approved_case())
    entries = cast(list[dict[str, object]], payload["provenance"])
    entries[0]["field_path"] = "made.up.path"
    with pytest.raises(DomainValidationError) as error:
        case_from_dict(payload)
    assert error.value.issue.code == "unsupported_provenance_path"
    entries.pop(0)
    with pytest.raises(DomainValidationError) as error:
        case_from_dict(payload)
    assert error.value.issue.code == "missing_provenance_coverage"


@pytest.mark.parametrize(
    ("locator", "code"),
    [
        ("bad-reference", "invalid_assumption_reference"),
        ("ASM-MISSING", "missing_assumption_reference"),
    ],
)
def test_assumption_references_remain_validated(locator: str, code: str) -> None:
    case = approved_case()
    first = replace(
        case.provenance[0], source_kind=SourceKind.APPROVED_ASSUMPTION, source_locator=locator
    )
    with pytest.raises(DomainValidationError) as error:
        replace(case, provenance=(first, *case.provenance[1:]))
    assert error.value.issue.code == code


@pytest.mark.parametrize("field", ["assumptions", "provenance"])
@pytest.mark.parametrize("container", [list, set, dict, iter])
def test_direct_construction_rejects_non_tuple_collections(field: str, container: object) -> None:
    case = approved_case()
    original = getattr(case, field)
    value = {} if container is dict else container(original)  # type: ignore[operator]
    with pytest.raises(DomainValidationError) as error:
        replace(case, **{field: value})  # type: ignore[arg-type]
    assert error.value.issue.code == "invalid_type"
    assert error.value.issue.field == field


@pytest.mark.parametrize("field", ["assumptions", "provenance"])
def test_tuple_elements_must_be_immutable_domain_types(field: str) -> None:
    with pytest.raises(DomainValidationError) as error:
        replace(approved_case(), **{field: ({},)})  # type: ignore[arg-type]
    assert error.value.issue.code == "invalid_type"


def test_deserialization_detaches_input_lists_and_retains_immutable_state() -> None:
    payload = case_to_dict(approved_case())
    case = case_from_dict(payload)
    cast(list[object], payload["assumptions"]).clear()
    cast(list[object], payload["provenance"]).clear()
    assert type(case.assumptions) is tuple
    assert type(case.provenance) is tuple
    assert case == approved_case()
    with pytest.raises(FrozenInstanceError):
        case.assumptions[0].value = "mutated"  # type: ignore[misc]
