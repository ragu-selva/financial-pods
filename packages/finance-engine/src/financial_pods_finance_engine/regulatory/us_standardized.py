"""Only the reviewed ordinary US/FRB corporate path; alternative treatments fail closed."""

from dataclasses import dataclass
from decimal import Decimal

from ..primitives import Money
from .arithmetic import multiply_money
from .contracts import (
    ClassificationResult,
    RegulatoryExposureMeasure,
    RegulatoryFact,
    RegulatoryFactSnapshot,
    RegulatoryTreatment,
    RiskWeight,
    RuleReference,
    RulesetIdentity,
    RwaResult,
    TeachingOutput,
)
from .errors import ErrorCode, fail
from .us_sources import USSourcePackage

VARIABLE_AMOUNTS = frozenset(
    {
        "accounting.original_principal",
        "accounting.outstanding_principal",
        "accounting.gross_amortized_cost",
        "accounting.net_balance_sheet_amount_candidate",
        "accounting.gaap_based_regulatory_carrying_value_candidate",
        "exposure.original_principal",
        "exposure.outstanding_balance",
        "exposure.gaap_carrying_value",
    }
)
INFORMATIONAL_FACTS = frozenset(
    {
        "informational.bcbs_sme",
        "informational.bcbs_external_rating",
        "informational.specialised_lending",
        "informational.regulatory_retail",
        "informational.annual_sales",
    }
)
WARNINGS = (
    "INTERNAL_PROTOTYPE_ONLY",
    "EDUCATIONAL_ONLY",
    "NOT_ALLOCATED_LOAN_CAPITAL",
    "NOT_ECONOMIC_CAPITAL",
    "NOT_COMPLETE_REQUIRED_REGULATORY_CAPITAL",
    "NOT_INSTITUTION_SPECIFIC_REQUIREMENT",
    "NOT_CAPITAL_ADEQUACY_CONCLUSION",
)
EXCLUSIONS = (
    "NO_CET1_OR_TIER1_TEACHING_EQUIVALENTS",
    "NO_BUFFERS_OR_COMPLETE_CAPITAL_REQUIREMENT",
    "NO_OTHER_EXPOSURE_CLASSES_OR_JURISDICTIONS",
    "NO_CRM_CALCULATION",
    "NO_REAL_BANK_GAAP_OR_CECL_CERTIFICATION",
    "NO_PORTFOLIO_OR_ACTUAL_CAPITAL_RATIO",
)


@dataclass(frozen=True, slots=True)
class USStandardizedRuleset:
    evidence: USSourcePackage

    def __post_init__(self) -> None:
        if type(self.evidence) is not USSourcePackage:
            fail(ErrorCode.INVALID_TYPE, "evidence", "Expected immutable U.S. evidence package")

    @property
    def identity(self) -> RulesetIdentity:
        return self.evidence.identity

    def validate_evidence(self) -> None:
        self.evidence.validate()

    def rule(self, rule_id: str) -> RuleReference:
        return self.evidence.rule(rule_id)

    def institution_scope_refs(self) -> tuple[RuleReference, ...]:
        return (self.rule("US-SCOPE"),)

    def classification_scope_refs(self) -> tuple[RuleReference, ...]:
        return tuple(self.rule(key) for key in ("US-CLASS", "US-SCOPE", "US-MEASURE", "US-CORP-RW"))

    def _schema(self, facts: RegulatoryFactSnapshot) -> tuple[RegulatoryFact, ...]:
        required = self.evidence.fact_specification()
        supplied = {item.path: item for item in facts.facts}
        missing = {item.path for item in required} - supplied.keys()
        if missing:
            fail(
                ErrorCode.MISSING_REQUIRED_FACT,
                sorted(missing)[0],
                "Required explicit regulatory fact is absent",
            )
        unknown = supplied.keys() - {item.path for item in required} - INFORMATIONAL_FACTS
        if unknown:
            fail(ErrorCode.INVALID_SCHEMA, sorted(unknown)[0], "Unsupported fact field")
        for item in required:
            fact = supplied[item.path]
            if type(fact.value) is str and fact.value == "UNKNOWN":
                fail(
                    ErrorCode.UNKNOWN_FACT,
                    item.path,
                    "An unknown fact cannot select the ordinary path",
                )
            if type(fact.value) is not type(item.value):
                fail(ErrorCode.INVALID_TYPE, item.path, "Fact type does not match required schema")
        return required

    def validate_institution(self, facts: RegulatoryFactSnapshot) -> tuple[str, ...]:
        required = self._schema(facts)
        values = {item.path: item.value for item in facts.facts}
        paths = []
        for item in required:
            if item.path.startswith("institution."):
                paths.append(item.path)
                if values[item.path] != item.value:
                    fail(
                        ErrorCode.INSTITUTION_OUT_OF_SCOPE,
                        item.path,
                        "Only the reviewed in-scope state member bank, never CBLR elected/in grace",
                        ("US-SCOPE",),
                    )
        return tuple(paths)

    def validate_exposure(self, facts: RegulatoryFactSnapshot) -> tuple[str, ...]:
        required = self._schema(facts)
        values = {item.path: item.value for item in facts.facts}
        for prefix in ("exposure", "other_scope"):
            if values[prefix + ".on_balance_sheet"] == values[prefix + ".off_balance_sheet"]:
                fail(
                    ErrorCode.CONFLICTING_FACTS,
                    prefix,
                    "On/off-balance-sheet flags must be complementary",
                    ("US-MEASURE",),
                )
        for left, right in (
            ("exposure.defaulted", "other_scope.defaulted"),
            ("exposure.nonaccrual", "other_scope.nonaccrual"),
            ("exposure.days_past_due", "other_scope.days_past_due"),
            ("exposure.on_balance_sheet", "other_scope.on_balance_sheet"),
            ("exposure.off_balance_sheet", "other_scope.off_balance_sheet"),
            ("exposure.fully_drawn", "other_scope.fully_drawn"),
            ("exposure.undrawn_amount", "other_scope.undrawn_amount"),
            ("exposure.partial_write_offs", "accounting.partial_write_offs"),
            ("exposure.credit_loss_allowance", "accounting.credit_loss_allowance"),
        ):
            if values[left] != values[right]:
                fail(ErrorCode.CONFLICTING_FACTS, left, "Contradicts " + right, ("US-MEASURE",))
        principal = values["exposure.outstanding_balance"]
        if type(principal) is not Money:
            fail(ErrorCode.INVALID_TYPE, "exposure.outstanding_balance", "Expected Money")
        if principal.amount <= 0:
            fail(
                ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE,
                "exposure.outstanding_balance",
                "Positive ordinary loan amount required",
            )
        for item in required:
            actual = values[item.path]
            if item.path in VARIABLE_AMOUNTS:
                if actual != principal:
                    fail(
                        ErrorCode.CONFLICTING_FACTS,
                        item.path,
                        "Zero-adjustment carrying-value reconciliation does not balance",
                        ("US-MEASURE",),
                    )
            elif not item.path.startswith("institution.") and actual != item.value:
                rules = (
                    ("US-CLASS",)
                    if item.path.startswith(("counterparty.", "definition.", "ppp."))
                    else ("US-SCOPE", "US-MEASURE", "US-CORP-RW")
                )
                fail(
                    ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE,
                    item.path,
                    "Outside approved ordinary corporate scope; no alternative treatment",
                    rules,
                )
        return tuple(item.path for item in required if not item.path.startswith("institution."))

    def _validate(self, facts: RegulatoryFactSnapshot) -> None:
        # Public provider methods must not bypass the engine's source-validation gate.
        self.validate_evidence()
        identity, context = self.identity, facts.context
        if (context.jurisdiction, context.regulator, context.regime) != (
            identity.jurisdiction,
            identity.regulator,
            identity.regime,
        ):
            fail(ErrorCode.UNSUPPORTED_JURISDICTION, "context", "Provider/regime mismatch")
        if context.as_of_date != identity.approved_as_of:
            fail(
                ErrorCode.RULESET_NOT_EFFECTIVE,
                "as_of_date",
                "Only approved point-in-time execution",
            )
        if context.ruleset_version != identity.ruleset_version:
            fail(ErrorCode.UNKNOWN_RULESET, "ruleset_version", "Exact approved version required")
        self.validate_institution(facts)
        self.validate_exposure(facts)

    def classify_exposure(self, facts: RegulatoryFactSnapshot) -> ClassificationResult:
        self._validate(facts)
        # Every named exclusion and its underlying granular facts was explicitly screened.
        return ClassificationResult(
            jurisdiction=self.identity.jurisdiction,
            ruleset_version=self.identity.ruleset_version,
            exposure_class="CORPORATE",
            subclass="GENERAL_CORPORATE",
            reason_codes=("US_CORPORATE_DEFINITION_SATISFIED",),
            rule_refs=(self.rule("US-CLASS"),),
        )

    def resolve_treatment(self, classification: ClassificationResult) -> RegulatoryTreatment:
        self.validate_evidence()
        if (
            classification.jurisdiction,
            classification.exposure_class,
            classification.subclass,
            classification.ruleset_version,
            classification.rule_refs,
        ) != (
            self.identity.jurisdiction,
            "CORPORATE",
            "GENERAL_CORPORATE",
            self.identity.ruleset_version,
            (self.rule("US-CLASS"),),
        ):
            fail(
                ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE,
                "classification",
                "Ordinary approved corporate class required",
            )
        return RegulatoryTreatment(
            name="ORDINARY_US_STANDARDIZED_CORPORATE",
            rule_refs=(self.rule("US-CORP-RW"), self.rule("US-MEASURE")),
            exclusions=EXCLUSIONS,
        )

    def determine_regulatory_exposure_measure(
        self, facts: RegulatoryFactSnapshot
    ) -> RegulatoryExposureMeasure:
        self._validate(facts)
        amount = next(
            item.value for item in facts.facts if item.path == "exposure.gaap_carrying_value"
        )
        if type(amount) is not Money:
            fail(ErrorCode.INVALID_TYPE, "carrying_value", "Expected Money")
        return RegulatoryExposureMeasure(
            amount=amount.amount,
            currency=amount.currency,
            measure_type="EXPOSURE_AMOUNT",
            measurement_basis="US_STANDARDIZED_CARRYING_VALUE",
            rule_refs=(self.rule("US-MEASURE"),),
        )

    def determine_risk_weight(self, facts: RegulatoryFactSnapshot) -> RiskWeight:
        self._validate(facts)
        return RiskWeight(value=Decimal("1.00"), rule_refs=(self.rule("US-CORP-RW"),))

    def calculate_rwa(self, measure: RegulatoryExposureMeasure, weight: RiskWeight) -> RwaResult:
        self.validate_evidence()
        if (
            measure.measure_type != "EXPOSURE_AMOUNT"
            or measure.measurement_basis != "US_STANDARDIZED_CARRYING_VALUE"
            or measure.amount <= 0
            or weight.value != Decimal("1.00")
            or measure.rule_refs != (self.rule("US-MEASURE"),)
            or weight.rule_refs != (self.rule("US-CORP-RW"),)
        ):
            fail(
                ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE,
                "measure",
                "Measure/rate/evidence must belong to selected provider",
            )
        amount = multiply_money(Money(measure.amount, measure.currency), weight.value)
        return RwaResult(
            amount=amount.amount, currency=amount.currency, rule_refs=(self.rule("US-RWA"),)
        )

    def calculate_capital_teaching_outputs(self, rwa: RwaResult) -> tuple[TeachingOutput, ...]:
        self.validate_evidence()
        if rwa.rule_refs != (self.rule("US-RWA"),) or rwa.amount <= 0:
            fail(
                ErrorCode.UNSUPPORTED_EXPOSURE_SCOPE,
                "rwa",
                "Positive approved single-exposure RWA required",
            )
        amount = multiply_money(Money(rwa.amount, rwa.currency), Decimal("0.08"))
        return (
            TeachingOutput(
                name="baseline_total_capital_equivalent",
                amount=amount.amount,
                currency=amount.currency,
                ratio=Decimal("0.08"),
                rule_refs=(self.rule("US-TEACHING"),),
                warnings=WARNINGS,
            ),
        )
