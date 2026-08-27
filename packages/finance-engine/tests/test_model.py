from dataclasses import FrozenInstanceError, replace
from datetime import date
from decimal import Decimal
from typing import Any

import pytest

from financial_pods_finance_engine import (
    Assumption,
    AssumptionId,
    AssumptionStatus,
    Counterparty,
    CounterpartyId,
    Currency,
    DomainValidationError,
    Exposure,
    ExposureId,
    Facility,
    FacilityId,
    FinBankCase,
    Institution,
    InstitutionId,
    Money,
    Product,
    ProductId,
    ProductKind,
    Provenance,
    SourceKind,
)


def valid_case() -> FinBankCase:
    assumption = Assumption(
        id=AssumptionId("ASM-DATES"),
        description="Synthetic dates.",
        value="origination=2025-01-01;maturity=2030-01-01",
        status=AssumptionStatus.APPROVED,
        approval_reference="sprints/sprint-01/DOMAIN_MODEL_SCOPE.md",
    )
    return FinBankCase(
        schema_version="1.0",
        fixture_version="1.0.0",
        currency_policy_version="sprint-01-v1",
        institution=Institution(InstitutionId("INS-FINBANK"), "FinBank"),
        counterparty=Counterparty(CounterpartyId("CP-ALPHA-MANUFACTURING"), "Alpha Manufacturing"),
        product=Product(ProductId("PRD-TERM-LOAN"), "Term Loan", ProductKind.TERM_LOAN),
        facility=Facility(
            id=FacilityId("FAC-ALPHA-001"),
            institution_id=InstitutionId("INS-FINBANK"),
            borrower_id=CounterpartyId("CP-ALPHA-MANUFACTURING"),
            product_id=ProductId("PRD-TERM-LOAN"),
            original_principal=Money(Decimal("10000000"), Currency("USD")),
            origination_date=date(2025, 1, 1),
            maturity_date=date(2030, 1, 1),
        ),
        exposure=Exposure(
            id=ExposureId("EXP-ALPHA-20250101"),
            facility_id=FacilityId("FAC-ALPHA-001"),
            as_of_date=date(2025, 1, 1),
            outstanding_principal=Money(Decimal("10000000"), Currency("USD")),
        ),
        assumptions=(assumption,),
        provenance=(
            Provenance(
                field_path="facility.origination_date",
                source_kind=SourceKind.APPROVED_ASSUMPTION,
                source_locator="ASM-DATES",
                source_version="sprint-01:2026-08-27",
            ),
        ),
    )


def test_domain_objects_are_immutable() -> None:
    institution = valid_case().institution

    with pytest.raises(FrozenInstanceError):
        institution.name = "Changed"  # type: ignore[misc]


def test_typed_identifiers_reject_wrong_entity_type_at_runtime() -> None:
    wrong_id: Any = CounterpartyId("CP-FINBANK")

    with pytest.raises(DomainValidationError) as exc_info:
        Institution(id=wrong_id, name="FinBank")

    assert exc_info.value.issue.code == "invalid_type"
    assert exc_info.value.issue.field == "institution.id"


def test_identifier_prefix_is_enforced() -> None:
    with pytest.raises(DomainValidationError) as exc_info:
        InstitutionId("CP-FINBANK")

    assert exc_info.value.issue.code == "invalid_identifier_prefix"


def test_facility_requires_positive_principal() -> None:
    with pytest.raises(DomainValidationError) as exc_info:
        replace(
            valid_case().facility,
            original_principal=Money(Decimal("0"), Currency("USD")),
        )

    assert exc_info.value.issue.code == "non_positive_money"


def test_facility_requires_maturity_after_origination() -> None:
    with pytest.raises(DomainValidationError) as exc_info:
        replace(valid_case().facility, maturity_date=date(2025, 1, 1))

    assert exc_info.value.issue.code == "invalid_date_range"


def test_case_rejects_cross_entity_reference_mismatch() -> None:
    case = valid_case()
    invalid_facility = replace(case.facility, institution_id=InstitutionId("INS-OTHER"))

    with pytest.raises(DomainValidationError) as exc_info:
        replace(case, facility=invalid_facility)

    assert exc_info.value.issue.code == "reference_mismatch"
    assert exc_info.value.issue.field == "facility.institution_id"


@pytest.mark.parametrize("as_of_date", [date(2024, 12, 31), date(2030, 1, 2)])
def test_case_rejects_exposure_outside_facility_dates(as_of_date: date) -> None:
    case = valid_case()
    invalid_exposure = replace(case.exposure, as_of_date=as_of_date)

    with pytest.raises(DomainValidationError) as exc_info:
        replace(case, exposure=invalid_exposure)

    assert exc_info.value.issue.code == "invalid_as_of_date"


def test_case_requires_provenance() -> None:
    with pytest.raises(DomainValidationError) as exc_info:
        replace(valid_case(), provenance=())

    assert exc_info.value.issue.code == "missing_provenance"


def test_case_requires_provenance_assumption_to_exist() -> None:
    case = valid_case()
    invalid_provenance = (replace(case.provenance[0], source_locator="ASM-NOT-PRESENT"),)

    with pytest.raises(DomainValidationError) as exc_info:
        replace(case, provenance=invalid_provenance)

    assert exc_info.value.issue.code == "missing_assumption_reference"
