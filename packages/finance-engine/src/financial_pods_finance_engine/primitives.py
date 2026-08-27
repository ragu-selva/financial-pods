from dataclasses import dataclass
from decimal import Decimal
from typing import Self

from .errors import invalid

CURRENCY_POLICY_VERSION = "sprint-01-v1"
SUPPORTED_CURRENCIES = frozenset({"USD"})


def _require_decimal(value: object, *, field: str) -> Decimal:
    if not isinstance(value, Decimal):
        invalid(code="invalid_type", field=field, message="must be a Decimal")
    if not value.is_finite():
        invalid(code="non_finite_decimal", field=field, message="must be finite")
    return value


def _fractional_digits(value: Decimal) -> int:
    normalized = value.normalize()
    exponent = normalized.as_tuple().exponent
    if not isinstance(exponent, int):
        invalid(code="non_finite_decimal", field="decimal", message="must be finite")
    return max(0, -exponent)


@dataclass(frozen=True, slots=True)
class Currency:
    code: str

    def __post_init__(self) -> None:
        if not isinstance(self.code, str):
            invalid(code="invalid_type", field="currency", message="must be a string")
        if len(self.code) != 3 or not self.code.isascii() or not self.code.isupper():
            invalid(
                code="invalid_currency_code",
                field="currency",
                message="must be a three-letter uppercase ASCII code",
            )
        if self.code not in SUPPORTED_CURRENCIES:
            invalid(
                code="unsupported_currency",
                field="currency",
                message=f"is not supported by policy {CURRENCY_POLICY_VERSION}",
            )

    def __str__(self) -> str:
        return self.code


@dataclass(frozen=True, slots=True)
class Money:
    amount: Decimal
    currency: Currency

    def __post_init__(self) -> None:
        value = _require_decimal(self.amount, field="amount")
        if type(self.currency) is not Currency:
            invalid(code="invalid_type", field="currency", message="must be a Currency")
        if _fractional_digits(value) > 2:
            invalid(
                code="excess_precision",
                field="amount",
                message="must have at most two fractional digits",
            )
        object.__setattr__(self, "amount", value.quantize(Decimal("0.01")))

    def __add__(self, other: object) -> Self:
        if type(other) is not type(self):
            return NotImplemented
        if self.currency != other.currency:
            invalid(code="currency_mismatch", field="currency", message="currencies must match")
        return type(self)(self.amount + other.amount, self.currency)

    def __sub__(self, other: object) -> Self:
        if type(other) is not type(self):
            return NotImplemented
        if self.currency != other.currency:
            invalid(code="currency_mismatch", field="currency", message="currencies must match")
        return type(self)(self.amount - other.amount, self.currency)

    def to_decimal_string(self) -> str:
        return format(self.amount, ".2f")


@dataclass(frozen=True, slots=True)
class Percentage:
    value: Decimal

    def __post_init__(self) -> None:
        decimal_value = _require_decimal(self.value, field="percentage")
        if _fractional_digits(decimal_value) > 6:
            invalid(
                code="excess_precision",
                field="percentage",
                message="must have at most six fractional digits",
            )
        canonical = Decimal(0) if decimal_value == 0 else decimal_value.normalize()
        object.__setattr__(self, "value", canonical)

    def require_range(
        self,
        *,
        field: str,
        minimum: Decimal | None = None,
        maximum: Decimal | None = None,
    ) -> None:
        if minimum is not None and self.value < minimum:
            invalid(code="below_minimum", field=field, message=f"must be at least {minimum}")
        if maximum is not None and self.value > maximum:
            invalid(code="above_maximum", field=field, message=f"must be at most {maximum}")

    def to_decimal_string(self) -> str:
        return format(self.value, "f")
