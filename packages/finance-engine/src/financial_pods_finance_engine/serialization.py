from collections.abc import Mapping
from datetime import date
from decimal import Decimal, InvalidOperation
from typing import cast

from .errors import DomainValidationError, invalid
from .identifiers import (
    AssumptionId,
    CounterpartyId,
    ExposureId,
    FacilityId,
    InstitutionId,
    ProductId,
)
from .model import (
    Counterparty,
    Exposure,
    Facility,
    FinBankCase,
    Institution,
    Product,
    ProductKind,
)
from .primitives import Currency, Money
from .provenance import Assumption, AssumptionStatus, Provenance, SourceKind

JsonObject = dict[str, object]


def _mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, dict):
        invalid(code="invalid_type", field=field, message="must be an object")
    return cast(dict[str, object], value)


def _list(value: object, *, field: str) -> list[object]:
    if not isinstance(value, list):
        invalid(code="invalid_type", field=field, message="must be an array")
    return cast(list[object], value)


def _string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        invalid(code="invalid_type", field=field, message="must be a string")
    return value


def _exact_fields(value: Mapping[str, object], expected: set[str], *, field: str) -> None:
    actual = set(value)
    missing = sorted(expected - actual)
    unknown = sorted(actual - expected)
    if missing:
        invalid(
            code="missing_field",
            field=field,
            message=f"missing required fields: {', '.join(missing)}",
        )
    if unknown:
        invalid(
            code="unknown_field",
            field=field,
            message=f"unknown fields: {', '.join(unknown)}",
        )


def _date(value: object, *, field: str) -> date:
    text = _string(value, field=field)
    try:
        parsed = date.fromisoformat(text)
    except ValueError:
        invalid(code="invalid_date", field=field, message="must be an ISO 8601 date")
    if parsed.isoformat() != text:
        invalid(code="invalid_date", field=field, message="must use canonical YYYY-MM-DD form")
    return parsed


def _decimal(value: object, *, field: str) -> Decimal:
    text = _string(value, field=field)
    try:
        decimal_value = Decimal(text)
    except InvalidOperation:
        invalid(code="invalid_decimal", field=field, message="must be a plain decimal string")
    if not decimal_value.is_finite() or "e" in text.lower():
        invalid(
            code="invalid_decimal", field=field, message="must be a finite plain decimal string"
        )
    return decimal_value


def _money_to_dict(value: Money) -> JsonObject:
    return {"amount": value.to_decimal_string(), "currency": value.currency.code}


def _money_from_dict(value: object, *, field: str) -> Money:
    data = _mapping(value, field=field)
    _exact_fields(data, {"amount", "currency"}, field=field)
    return Money(
        amount=_decimal(data["amount"], field=f"{field}.amount"),
        currency=Currency(_string(data["currency"], field=f"{field}.currency")),
    )


def case_to_dict(case: FinBankCase) -> JsonObject:
    return {
        "schema_version": case.schema_version,
        "fixture_version": case.fixture_version,
        "currency_policy_version": case.currency_policy_version,
        "institution": {"id": str(case.institution.id), "name": case.institution.name},
        "counterparty": {
            "id": str(case.counterparty.id),
            "legal_name": case.counterparty.legal_name,
        },
        "product": {
            "id": str(case.product.id),
            "name": case.product.name,
            "kind": case.product.kind.value,
        },
        "facility": {
            "id": str(case.facility.id),
            "institution_id": str(case.facility.institution_id),
            "borrower_id": str(case.facility.borrower_id),
            "product_id": str(case.facility.product_id),
            "original_principal": _money_to_dict(case.facility.original_principal),
            "origination_date": case.facility.origination_date.isoformat(),
            "maturity_date": case.facility.maturity_date.isoformat(),
        },
        "exposure": {
            "id": str(case.exposure.id),
            "facility_id": str(case.exposure.facility_id),
            "as_of_date": case.exposure.as_of_date.isoformat(),
            "outstanding_principal": _money_to_dict(case.exposure.outstanding_principal),
        },
        "assumptions": [
            {
                "id": str(item.id),
                "description": item.description,
                "value": item.value,
                "status": item.status.value,
                "approval_reference": item.approval_reference,
            }
            for item in case.assumptions
        ],
        "provenance": [
            {
                "field_path": item.field_path,
                "source_kind": item.source_kind.value,
                "source_locator": item.source_locator,
                "source_version": item.source_version,
            }
            for item in case.provenance
        ],
    }


def case_from_dict(value: object) -> FinBankCase:
    data = _mapping(value, field="case")
    _exact_fields(
        data,
        {
            "schema_version",
            "fixture_version",
            "currency_policy_version",
            "institution",
            "counterparty",
            "product",
            "facility",
            "exposure",
            "assumptions",
            "provenance",
        },
        field="case",
    )

    institution_data = _mapping(data["institution"], field="institution")
    _exact_fields(institution_data, {"id", "name"}, field="institution")
    institution = Institution(
        id=InstitutionId(_string(institution_data["id"], field="institution.id")),
        name=_string(institution_data["name"], field="institution.name"),
    )

    counterparty_data = _mapping(data["counterparty"], field="counterparty")
    _exact_fields(counterparty_data, {"id", "legal_name"}, field="counterparty")
    counterparty = Counterparty(
        id=CounterpartyId(_string(counterparty_data["id"], field="counterparty.id")),
        legal_name=_string(counterparty_data["legal_name"], field="counterparty.legal_name"),
    )

    product_data = _mapping(data["product"], field="product")
    _exact_fields(product_data, {"id", "name", "kind"}, field="product")
    try:
        product_kind = ProductKind(_string(product_data["kind"], field="product.kind"))
    except ValueError:
        invalid(
            code="invalid_enum", field="product.kind", message="is not a supported product kind"
        )
    product = Product(
        id=ProductId(_string(product_data["id"], field="product.id")),
        name=_string(product_data["name"], field="product.name"),
        kind=product_kind,
    )

    facility_data = _mapping(data["facility"], field="facility")
    _exact_fields(
        facility_data,
        {
            "id",
            "institution_id",
            "borrower_id",
            "product_id",
            "original_principal",
            "origination_date",
            "maturity_date",
        },
        field="facility",
    )
    facility = Facility(
        id=FacilityId(_string(facility_data["id"], field="facility.id")),
        institution_id=InstitutionId(
            _string(facility_data["institution_id"], field="facility.institution_id")
        ),
        borrower_id=CounterpartyId(
            _string(facility_data["borrower_id"], field="facility.borrower_id")
        ),
        product_id=ProductId(_string(facility_data["product_id"], field="facility.product_id")),
        original_principal=_money_from_dict(
            facility_data["original_principal"], field="facility.original_principal"
        ),
        origination_date=_date(
            facility_data["origination_date"], field="facility.origination_date"
        ),
        maturity_date=_date(facility_data["maturity_date"], field="facility.maturity_date"),
    )

    exposure_data = _mapping(data["exposure"], field="exposure")
    _exact_fields(
        exposure_data,
        {"id", "facility_id", "as_of_date", "outstanding_principal"},
        field="exposure",
    )
    exposure = Exposure(
        id=ExposureId(_string(exposure_data["id"], field="exposure.id")),
        facility_id=FacilityId(_string(exposure_data["facility_id"], field="exposure.facility_id")),
        as_of_date=_date(exposure_data["as_of_date"], field="exposure.as_of_date"),
        outstanding_principal=_money_from_dict(
            exposure_data["outstanding_principal"], field="exposure.outstanding_principal"
        ),
    )

    assumptions = tuple(
        _assumption_from_dict(item, index=index)
        for index, item in enumerate(_list(data["assumptions"], field="assumptions"))
    )
    provenance = tuple(
        _provenance_from_dict(item, index=index)
        for index, item in enumerate(_list(data["provenance"], field="provenance"))
    )

    return FinBankCase(
        schema_version=_string(data["schema_version"], field="schema_version"),
        fixture_version=_string(data["fixture_version"], field="fixture_version"),
        currency_policy_version=_string(
            data["currency_policy_version"], field="currency_policy_version"
        ),
        institution=institution,
        counterparty=counterparty,
        product=product,
        facility=facility,
        exposure=exposure,
        assumptions=assumptions,
        provenance=provenance,
    )


def _assumption_from_dict(value: object, *, index: int) -> Assumption:
    field = f"assumptions[{index}]"
    data = _mapping(value, field=field)
    _exact_fields(
        data,
        {"id", "description", "value", "status", "approval_reference"},
        field=field,
    )
    try:
        status = AssumptionStatus(_string(data["status"], field=f"{field}.status"))
    except ValueError:
        invalid(code="invalid_enum", field=f"{field}.status", message="is not supported")
    return Assumption(
        id=AssumptionId(_string(data["id"], field=f"{field}.id")),
        description=_string(data["description"], field=f"{field}.description"),
        value=_string(data["value"], field=f"{field}.value"),
        status=status,
        approval_reference=_string(data["approval_reference"], field=f"{field}.approval_reference"),
    )


def _provenance_from_dict(value: object, *, index: int) -> Provenance:
    field = f"provenance[{index}]"
    data = _mapping(value, field=field)
    _exact_fields(
        data,
        {"field_path", "source_kind", "source_locator", "source_version"},
        field=field,
    )
    try:
        source_kind = SourceKind(_string(data["source_kind"], field=f"{field}.source_kind"))
    except ValueError:
        invalid(code="invalid_enum", field=f"{field}.source_kind", message="is not supported")
    return Provenance(
        field_path=_string(data["field_path"], field=f"{field}.field_path"),
        source_kind=source_kind,
        source_locator=_string(data["source_locator"], field=f"{field}.source_locator"),
        source_version=_string(data["source_version"], field=f"{field}.source_version"),
    )


__all__ = ["DomainValidationError", "case_from_dict", "case_to_dict"]
