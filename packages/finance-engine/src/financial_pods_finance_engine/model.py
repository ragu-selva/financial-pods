from dataclasses import dataclass
from datetime import date
from enum import StrEnum

from .errors import invalid
from .identifiers import (
    AssumptionId,
    CounterpartyId,
    ExposureId,
    FacilityId,
    InstitutionId,
    ProductId,
)
from .primitives import CURRENCY_POLICY_VERSION, Money
from .provenance import Assumption, AssumptionStatus, Provenance, SourceKind

SCHEMA_VERSION = "1.0"


def _require_text(value: object, *, field: str) -> None:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        invalid(code="invalid_text", field=field, message="must be a non-empty trimmed string")


def _require_exact_type(value: object, expected: type[object], *, field: str) -> None:
    if type(value) is not expected:
        invalid(code="invalid_type", field=field, message=f"must be a {expected.__name__}")


class ProductKind(StrEnum):
    TERM_LOAN = "term_loan"


@dataclass(frozen=True, slots=True)
class Institution:
    id: InstitutionId
    name: str

    def __post_init__(self) -> None:
        _require_exact_type(self.id, InstitutionId, field="institution.id")
        _require_text(self.name, field="institution.name")


@dataclass(frozen=True, slots=True)
class Counterparty:
    id: CounterpartyId
    legal_name: str

    def __post_init__(self) -> None:
        _require_exact_type(self.id, CounterpartyId, field="counterparty.id")
        _require_text(self.legal_name, field="counterparty.legal_name")


@dataclass(frozen=True, slots=True)
class Product:
    id: ProductId
    name: str
    kind: ProductKind

    def __post_init__(self) -> None:
        _require_exact_type(self.id, ProductId, field="product.id")
        _require_text(self.name, field="product.name")
        _require_exact_type(self.kind, ProductKind, field="product.kind")


@dataclass(frozen=True, slots=True)
class Facility:
    id: FacilityId
    institution_id: InstitutionId
    borrower_id: CounterpartyId
    product_id: ProductId
    original_principal: Money
    origination_date: date
    maturity_date: date

    def __post_init__(self) -> None:
        _require_exact_type(self.id, FacilityId, field="facility.id")
        _require_exact_type(self.institution_id, InstitutionId, field="facility.institution_id")
        _require_exact_type(self.borrower_id, CounterpartyId, field="facility.borrower_id")
        _require_exact_type(self.product_id, ProductId, field="facility.product_id")
        _require_exact_type(self.original_principal, Money, field="facility.original_principal")
        _require_exact_type(self.origination_date, date, field="facility.origination_date")
        _require_exact_type(self.maturity_date, date, field="facility.maturity_date")
        if self.original_principal.amount <= 0:
            invalid(
                code="non_positive_money",
                field="facility.original_principal",
                message="must be greater than zero",
            )
        if self.maturity_date <= self.origination_date:
            invalid(
                code="invalid_date_range",
                field="facility.maturity_date",
                message="must be after origination_date",
            )


@dataclass(frozen=True, slots=True)
class Exposure:
    id: ExposureId
    facility_id: FacilityId
    as_of_date: date
    outstanding_principal: Money

    def __post_init__(self) -> None:
        _require_exact_type(self.id, ExposureId, field="exposure.id")
        _require_exact_type(self.facility_id, FacilityId, field="exposure.facility_id")
        _require_exact_type(self.as_of_date, date, field="exposure.as_of_date")
        _require_exact_type(
            self.outstanding_principal, Money, field="exposure.outstanding_principal"
        )
        if self.outstanding_principal.amount < 0:
            invalid(
                code="negative_money",
                field="exposure.outstanding_principal",
                message="must be zero or greater",
            )


@dataclass(frozen=True, slots=True)
class FinBankCase:
    schema_version: str
    fixture_version: str
    currency_policy_version: str
    institution: Institution
    counterparty: Counterparty
    product: Product
    facility: Facility
    exposure: Exposure
    assumptions: tuple[Assumption, ...]
    provenance: tuple[Provenance, ...]

    def __post_init__(self) -> None:
        if self.schema_version != SCHEMA_VERSION:
            invalid(
                code="unsupported_schema_version",
                field="schema_version",
                message=f"must equal {SCHEMA_VERSION}",
            )
        _require_text(self.fixture_version, field="fixture_version")
        if self.currency_policy_version != CURRENCY_POLICY_VERSION:
            invalid(
                code="unsupported_currency_policy",
                field="currency_policy_version",
                message=f"must equal {CURRENCY_POLICY_VERSION}",
            )
        _require_exact_type(self.institution, Institution, field="institution")
        _require_exact_type(self.counterparty, Counterparty, field="counterparty")
        _require_exact_type(self.product, Product, field="product")
        _require_exact_type(self.facility, Facility, field="facility")
        _require_exact_type(self.exposure, Exposure, field="exposure")
        if not self.assumptions:
            invalid(code="missing_assumptions", field="assumptions", message="must not be empty")
        if not self.provenance:
            invalid(code="missing_provenance", field="provenance", message="must not be empty")
        self._validate_references()
        self._validate_assumptions_and_provenance()

    def _validate_references(self) -> None:
        if self.facility.institution_id != self.institution.id:
            invalid(
                code="reference_mismatch",
                field="facility.institution_id",
                message="must reference institution.id",
            )
        if self.facility.borrower_id != self.counterparty.id:
            invalid(
                code="reference_mismatch",
                field="facility.borrower_id",
                message="must reference counterparty.id",
            )
        if self.facility.product_id != self.product.id:
            invalid(
                code="reference_mismatch",
                field="facility.product_id",
                message="must reference product.id",
            )
        if self.exposure.facility_id != self.facility.id:
            invalid(
                code="reference_mismatch",
                field="exposure.facility_id",
                message="must reference facility.id",
            )
        if self.exposure.as_of_date < self.facility.origination_date:
            invalid(
                code="invalid_as_of_date",
                field="exposure.as_of_date",
                message="must not precede facility.origination_date",
            )
        if self.exposure.as_of_date > self.facility.maturity_date:
            invalid(
                code="invalid_as_of_date",
                field="exposure.as_of_date",
                message="must not follow facility.maturity_date",
            )
        if (
            self.exposure.outstanding_principal.currency
            != self.facility.original_principal.currency
        ):
            invalid(
                code="currency_mismatch",
                field="exposure.outstanding_principal.currency",
                message="must match facility.original_principal.currency",
            )

    def _validate_assumptions_and_provenance(self) -> None:
        assumption_ids: set[AssumptionId] = set()
        for assumption in self.assumptions:
            _require_exact_type(assumption, Assumption, field="assumptions")
            if assumption.status is not AssumptionStatus.APPROVED:
                invalid(
                    code="unapproved_assumption",
                    field="assumptions.status",
                    message="all assumptions must be approved",
                )
            if assumption.id in assumption_ids:
                invalid(
                    code="duplicate_assumption",
                    field="assumptions.id",
                    message=f"duplicate assumption {assumption.id}",
                )
            assumption_ids.add(assumption.id)

        field_paths: set[str] = set()
        for item in self.provenance:
            _require_exact_type(item, Provenance, field="provenance")
            if item.field_path in field_paths:
                invalid(
                    code="duplicate_provenance",
                    field="provenance.field_path",
                    message=f"duplicate field path {item.field_path}",
                )
            field_paths.add(item.field_path)
            if item.source_kind is SourceKind.APPROVED_ASSUMPTION:
                try:
                    referenced_id = AssumptionId(item.source_locator)
                except ValueError as exc:
                    invalid(
                        code="invalid_assumption_reference",
                        field="provenance.source_locator",
                        message=str(exc),
                    )
                if referenced_id not in assumption_ids:
                    invalid(
                        code="missing_assumption_reference",
                        field="provenance.source_locator",
                        message=f"{referenced_id} is not present in assumptions",
                    )
