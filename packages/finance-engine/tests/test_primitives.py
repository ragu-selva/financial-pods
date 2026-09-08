from decimal import Decimal

import pytest
from hypothesis import given
from hypothesis import strategies as st

from financial_pods_finance_engine import (
    Currency,
    DomainValidationError,
    Money,
    Percentage,
)


def test_currency_policy_accepts_usd_and_rejects_other_codes() -> None:
    assert Currency("USD").code == "USD"

    with pytest.raises(DomainValidationError) as exc_info:
        Currency("EUR")

    assert exc_info.value.issue.to_dict() == {
        "code": "unsupported_currency",
        "field": "currency",
        "message": "is not supported by policy sprint-01-v1",
    }


@pytest.mark.parametrize("code", ["usd", "US", "US1", " USD", "USD "])
def test_currency_rejects_malformed_codes(code: str) -> None:
    with pytest.raises(DomainValidationError):
        Currency(code)


def test_money_is_exact_and_has_no_implicit_rounding() -> None:
    money = Money(Decimal("10000000"), Currency("USD"))

    assert money.amount == Decimal("10000000.00")
    assert money.to_decimal_string() == "10000000.00"

    with pytest.raises(DomainValidationError) as exc_info:
        Money(Decimal("1.001"), Currency("USD"))

    assert exc_info.value.issue.code == "excess_precision"


def test_money_rejects_binary_floating_point() -> None:
    with pytest.raises(DomainValidationError) as exc_info:
        Money(1.25, Currency("USD"))  # type: ignore[arg-type]

    assert exc_info.value.issue.code == "invalid_type"


def test_money_arithmetic_requires_matching_currency() -> None:
    first = Money(Decimal("10.25"), Currency("USD"))
    second = Money(Decimal("1.75"), Currency("USD"))

    assert first + second == Money(Decimal("12.00"), Currency("USD"))
    assert first - second == Money(Decimal("8.50"), Currency("USD"))


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("0", "0"),
        ("-10.5", "-10.5"),
        ("100", "100"),
        ("0.000001", "0.000001"),
    ],
)
def test_percentage_is_exact_without_a_universal_range(value: str, expected: str) -> None:
    percentage = Percentage(Decimal(value))

    assert percentage.to_decimal_string() == expected


def test_percentage_applies_field_specific_bounds() -> None:
    percentage = Percentage(Decimal("101"))

    with pytest.raises(DomainValidationError) as exc_info:
        percentage.require_range(
            field="test.percentage", minimum=Decimal("0"), maximum=Decimal("100")
        )

    assert exc_info.value.issue.code == "above_maximum"
    assert exc_info.value.issue.field == "test.percentage"


def test_percentage_rejects_excess_precision() -> None:
    with pytest.raises(DomainValidationError) as exc_info:
        Percentage(Decimal("0.0000001"))

    assert exc_info.value.issue.code == "excess_precision"


@given(
    st.decimals(
        min_value=Decimal("-1000000000"),
        max_value=Decimal("1000000000"),
        places=2,
        allow_nan=False,
        allow_infinity=False,
    )
)
def test_money_decimal_serialization_round_trip(value: Decimal) -> None:
    original = Money(value, Currency("USD"))
    restored = Money(Decimal(original.to_decimal_string()), Currency("USD"))

    assert restored == original


@given(
    st.decimals(
        min_value=Decimal("-1000000"),
        max_value=Decimal("1000000"),
        places=6,
        allow_nan=False,
        allow_infinity=False,
    )
)
def test_percentage_decimal_serialization_round_trip(value: Decimal) -> None:
    original = Percentage(value)
    restored = Percentage(Decimal(original.to_decimal_string()))

    assert restored == original
