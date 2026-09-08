from copy import deepcopy
from decimal import Decimal
from pathlib import Path
from typing import cast

import pytest

from financial_pods_finance_engine import (
    DomainValidationError,
    case_from_dict,
    case_to_dict,
    load_case_fixture,
)

FIXTURE_PATH = (
    Path(__file__).resolve().parents[3] / "data" / "finbank" / "alpha_manufacturing_v1.json"
)


def fixture_payload() -> dict[str, object]:
    return case_to_dict(load_case_fixture(FIXTURE_PATH))


def nested_mapping(payload: dict[str, object], key: str) -> dict[str, object]:
    return cast(dict[str, object], payload[key])


def test_case_serialization_round_trip_is_lossless() -> None:
    case = load_case_fixture(FIXTURE_PATH)

    assert case_from_dict(case_to_dict(case)) == case


def test_serialized_financial_values_are_plain_strings() -> None:
    payload = fixture_payload()
    facility = nested_mapping(payload, "facility")
    principal = nested_mapping(facility, "original_principal")

    assert principal == {"amount": "10000000.00", "currency": "USD"}
    assert Decimal(cast(str, principal["amount"])) == Decimal("10000000.00")


def test_unknown_fields_are_rejected() -> None:
    payload = fixture_payload()
    payload["unexpected"] = True

    with pytest.raises(DomainValidationError) as exc_info:
        case_from_dict(payload)

    assert exc_info.value.issue.code == "unknown_field"
    assert "unexpected" in exc_info.value.issue.message


def test_missing_fields_are_rejected() -> None:
    payload = fixture_payload()
    del payload["fixture_version"]

    with pytest.raises(DomainValidationError) as exc_info:
        case_from_dict(payload)

    assert exc_info.value.issue.code == "missing_field"
    assert "fixture_version" in exc_info.value.issue.message


def test_unsupported_schema_versions_are_rejected() -> None:
    payload = fixture_payload()
    payload["schema_version"] = "2.0"

    with pytest.raises(DomainValidationError) as exc_info:
        case_from_dict(payload)

    assert exc_info.value.issue.code == "unsupported_schema_version"


@pytest.mark.parametrize("amount", ["NaN", "Infinity", "1e3", "1.001", "not-a-number"])
def test_malformed_or_unsupported_money_encodings_are_rejected(amount: str) -> None:
    payload = deepcopy(fixture_payload())
    facility = nested_mapping(payload, "facility")
    principal = nested_mapping(facility, "original_principal")
    principal["amount"] = amount

    with pytest.raises(DomainValidationError):
        case_from_dict(payload)


def test_noncanonical_dates_are_rejected() -> None:
    payload = fixture_payload()
    facility = nested_mapping(payload, "facility")
    facility["origination_date"] = "2025-1-1"

    with pytest.raises(DomainValidationError) as exc_info:
        case_from_dict(payload)

    assert exc_info.value.issue.code == "invalid_date"
