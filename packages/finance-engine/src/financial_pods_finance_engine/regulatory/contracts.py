"""Version 1 immutable contracts. No jurisdiction policy or borrower-specific behavior."""

from __future__ import annotations

from dataclasses import dataclass, fields
from datetime import date
from decimal import Decimal
from types import UnionType
from typing import Literal, get_args, get_origin, get_type_hints

from ..errors import DomainValidationError
from ..primitives import Currency, Money
from .errors import ErrorCode, fail


def _matches(value: object, annotation: object) -> bool:
    origin, args = get_origin(annotation), get_args(annotation)
    if origin is UnionType:
        return any(_matches(value, item) for item in args)
    if origin is Literal:
        return any(type(value) is type(item) and value == item for item in args)
    if origin is tuple:
        if type(value) is not tuple:
            return False
        if len(args) == 2 and args[1] is Ellipsis:
            return all(_matches(item, args[0]) for item in value)
        return len(value) == len(args) and all(
            _matches(item, kind) for item, kind in zip(value, args, strict=True)
        )
    return isinstance(annotation, type) and type(value) is annotation


class Immutable:
    __slots__ = ()

    def __post_init__(self) -> None:
        hints = get_type_hints(type(self))
        for field in fields(self):  # type: ignore[arg-type]
            if not _matches(getattr(self, field.name), hints[field.name]):
                fail(ErrorCode.INVALID_TYPE, field.name, "Invalid type or mutable collection")


def text(value: str, field: str) -> None:
    if not value.strip() or value != value.strip():
        fail(ErrorCode.INVALID_TYPE, field, "Expected nonempty trimmed text")


def money(amount: Decimal, currency: Currency) -> Money:
    try:
        return Money(amount, currency)
    except DomainValidationError as exc:
        code = (
            ErrorCode.EXCESS_PRECISION
            if exc.issue.code == "excess_precision"
            else ErrorCode.INVALID_TYPE
        )
        fail(code, "amount", exc.issue.message)


def ratio(value: Decimal) -> None:
    if not value.is_finite() or value < 0:
        fail(ErrorCode.INVALID_TYPE, "ratio", "Expected finite nonnegative Decimal ratio")
    _, digits, exponent = value.as_tuple()
    if not isinstance(exponent, int):
        fail(ErrorCode.INVALID_TYPE, "ratio", "Expected finite ratio")
    while len(digits) > 1 and digits[-1] == 0:
        digits, exponent = digits[:-1], exponent + 1
    if not value.is_zero() and exponent < -6:
        fail(ErrorCode.EXCESS_PRECISION, "ratio", "At most six fractional digits; no rounding")


@dataclass(frozen=True, slots=True, kw_only=True)
class RegulatoryContext(Immutable):
    jurisdiction: str
    regulator: str
    regime: str
    as_of_date: date
    ruleset_version: str

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        for key in ("jurisdiction", "regulator", "regime", "ruleset_version"):
            text(getattr(self, key), key)


@dataclass(frozen=True, slots=True, kw_only=True)
class FactProvenance(Immutable):
    source_ref: str
    source_version: str
    assumption_id: str
    review_status: Literal["APPROVED_FOR_INTERNAL_PROTOTYPE"]

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        for key in ("source_ref", "source_version", "assumption_id"):
            text(getattr(self, key), "provenance." + key)


@dataclass(frozen=True, slots=True, kw_only=True)
class RegulatoryFact(Immutable):
    path: str
    value: str | bool | int | Money
    provenance: FactProvenance

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        text(self.path, "fact.path")


@dataclass(frozen=True, slots=True, kw_only=True)
class RequestMetadata(Immutable):
    case_id: str
    counterparty_id: str
    institution_id: str
    borrower_name: str
    calculation_id: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class RegulatoryFactSnapshot(Immutable):
    context: RegulatoryContext
    facts: tuple[RegulatoryFact, ...]
    metadata: RequestMetadata
    fixture_version: str
    schema_version: Literal["regulatory-facts.v1"] = "regulatory-facts.v1"

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        text(self.fixture_version, "fixture_version")
        paths = [item.path for item in self.facts]
        if len(set(paths)) != len(paths):
            fail(ErrorCode.INVALID_PROVENANCE, "facts", "Duplicate fact/provenance paths")
        object.__setattr__(self, "facts", tuple(sorted(self.facts, key=lambda item: item.path)))


@dataclass(frozen=True, slots=True, kw_only=True)
class SourceCitation(Immutable):
    source_id: str
    authority: str | None
    canonical_source: str
    locator: str
    content_sha256: str
    retrieval_date: str
    version_evidence: str


@dataclass(frozen=True, slots=True, kw_only=True)
class RuleReference(Immutable):
    rule_id: str
    rule_version: str
    authority: str
    locators: tuple[str, ...]
    citations: tuple[SourceCitation, ...]
    effective_from: date
    approved_as_of: date
    reviewer_name: str
    review_date: date
    review_status: Literal["APPROVED_FOR_INTERNAL_PROTOTYPE"]
    effective_to: None = None
    effective_to_status: Literal["UNKNOWN_NOT_OPEN_ENDED"] = "UNKNOWN_NOT_OPEN_ENDED"


@dataclass(frozen=True, slots=True, kw_only=True)
class RulesetIdentity(Immutable):
    jurisdiction: str
    regulator: str
    regime: str
    ruleset_id: str
    ruleset_version: str
    approved_as_of: date
    manifest_hash: str
    catalog_snapshot_id: str
    legal_status: str
    approved: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class ClassificationResult(Immutable):
    jurisdiction: str
    ruleset_version: str
    exposure_class: str
    subclass: str
    reason_codes: tuple[str, ...]
    rule_refs: tuple[RuleReference, ...]
    warnings: tuple[str, ...] = ()
    schema_version: Literal["regulatory-classification.v1"] = "regulatory-classification.v1"


@dataclass(frozen=True, slots=True, kw_only=True)
class RegulatoryTreatment(Immutable):
    name: str
    rule_refs: tuple[RuleReference, ...]
    exclusions: tuple[str, ...]


@dataclass(frozen=True, slots=True, kw_only=True)
class RegulatoryExposureMeasure(Immutable):
    amount: Decimal
    currency: Currency
    measure_type: Literal["EXPOSURE_AMOUNT"]
    measurement_basis: str
    rule_refs: tuple[RuleReference, ...]
    warnings: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        object.__setattr__(self, "amount", money(self.amount, self.currency).amount)


@dataclass(frozen=True, slots=True, kw_only=True)
class RiskWeight(Immutable):
    value: Decimal
    rule_refs: tuple[RuleReference, ...]
    unit: Literal["RATIO"] = "RATIO"

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        ratio(self.value)


@dataclass(frozen=True, slots=True, kw_only=True)
class RwaResult(Immutable):
    amount: Decimal
    currency: Currency
    rule_refs: tuple[RuleReference, ...]

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        object.__setattr__(self, "amount", money(self.amount, self.currency).amount)


@dataclass(frozen=True, slots=True, kw_only=True)
class TeachingOutput(Immutable):
    name: Literal["baseline_total_capital_equivalent"]
    amount: Decimal
    currency: Currency
    ratio: Decimal
    rule_refs: tuple[RuleReference, ...]
    warnings: tuple[str, ...]

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        ratio(self.ratio)
        object.__setattr__(self, "amount", money(self.amount, self.currency).amount)


@dataclass(frozen=True, slots=True, kw_only=True)
class ValidationEvidence(Immutable):
    fact_paths: tuple[str, ...]
    conclusion: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TraceCompletion(Immutable):
    source_ids: tuple[str, ...]
    exclusions: tuple[str, ...]


@dataclass(frozen=True, slots=True, kw_only=True)
class FailureDetail(Immutable):
    code: str
    field_path: str
    message: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TraceStep(Immutable):
    sequence: int
    step_id: str
    operation: str
    reason_code: str
    inputs_used: tuple[str, ...]
    output: (
        RegulatoryContext
        | RulesetIdentity
        | ValidationEvidence
        | ClassificationResult
        | RegulatoryTreatment
        | RegulatoryExposureMeasure
        | RiskWeight
        | RwaResult
        | TeachingOutput
        | TraceCompletion
        | FailureDetail
    )
    rule_refs: tuple[RuleReference, ...] = ()
    engine_contract: str | None = None
    warnings: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        if self.sequence < 1 or (not self.rule_refs and not self.engine_contract):
            fail(
                ErrorCode.INVALID_SCHEMA,
                "trace",
                "Positive sequence and rule/engine evidence required",
            )


@dataclass(frozen=True, slots=True, kw_only=True)
class CalculationTrace(Immutable):
    steps: tuple[TraceStep, ...]
    schema_version: Literal["regulatory-trace.v1"] = "regulatory-trace.v1"

    def __post_init__(self) -> None:
        Immutable.__post_init__(self)
        if tuple(item.sequence for item in self.steps) != tuple(range(1, len(self.steps) + 1)):
            fail(ErrorCode.INVALID_SCHEMA, "trace", "Trace sequence must be contiguous")
        if len({item.step_id for item in self.steps}) != len(self.steps):
            fail(ErrorCode.INVALID_SCHEMA, "trace", "Duplicate step IDs")


@dataclass(frozen=True, slots=True, kw_only=True)
class RegulatoryCalculationResult(Immutable):
    jurisdiction: str
    as_of_date: date
    fixture_version: str
    fact_schema_version: str
    classification: ClassificationResult
    regulatory_treatment: RegulatoryTreatment
    regulatory_exposure_measure: RegulatoryExposureMeasure
    risk_weight: RiskWeight
    rwa: RwaResult
    capital_teaching_outputs: tuple[TeachingOutput, ...]
    ruleset: RulesetIdentity
    rule_versions: tuple[tuple[str, str], ...]
    input_snapshot_hash: str
    calculation_trace: CalculationTrace
    source_citations: tuple[SourceCitation, ...]
    warnings: tuple[str, ...]
    exclusions: tuple[str, ...]
    request_metadata: RequestMetadata
    schema_version: Literal["regulatory-calculation.v1"] = "regulatory-calculation.v1"
