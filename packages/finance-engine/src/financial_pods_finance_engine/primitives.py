from dataclasses import dataclass
from decimal import (
    MAX_EMAX,
    MIN_EMIN,
    ROUND_HALF_EVEN,
    Context,
    Decimal,
    Inexact,
    InvalidOperation,
    Overflow,
    Rounded,
    localcontext,
)
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


def _canonical_parts(value: Decimal) -> tuple[int, tuple[int, ...], int]:
    """Strip insignificant zeros without context-sensitive Decimal arithmetic."""
    sign, digits, exponent = value.as_tuple()
    if not isinstance(exponent, int):
        invalid(code="non_finite_decimal", field="decimal", message="must be finite")
    if value.is_zero():
        return sign, (0,), 0
    end = len(digits)
    while end > 1 and digits[end - 1] == 0:
        end -= 1
        exponent += 1
    return sign, digits[:end], exponent


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
        sign, digits, exponent = _canonical_parts(value)
        if exponent < -2:
            invalid(
                code="excess_precision",
                field="amount",
                message="must have at most two fractional digits",
            )
        # The tuple constructor ignores precision, rounding, and context exponent limits.
        fixed_digits = (0,) if value.is_zero() else digits + (0,) * (exponent + 2)
        object.__setattr__(self, "amount", Decimal((sign, fixed_digits, -2)))

    def __add__(self, other: object) -> Self:
        if type(other) is not type(self):
            return NotImplemented
        if self.currency != other.currency:
            invalid(code="currency_mismatch", field="currency", message="currencies must match")
        return self._combine(other, subtract=False)

    def __sub__(self, other: object) -> Self:
        if type(other) is not type(self):
            return NotImplemented
        if self.currency != other.currency:
            invalid(code="currency_mismatch", field="currency", message="currencies must match")
        return self._combine(other, subtract=True)

    def _combine(self, other: Self, *, subtract: bool) -> Self:
        # Both operands have exponent -2. One extra coefficient digit covers any carry.
        # Isolate arithmetic from the caller's traps, rounding, clamp, and exponent limits.
        precision = max(len(self.amount.as_tuple().digits), len(other.amount.as_tuple().digits)) + 1
        context = Context(
            prec=precision,
            rounding=ROUND_HALF_EVEN,
            Emin=MIN_EMIN,
            Emax=MAX_EMAX,
            capitals=1,
            clamp=0,
            flags=[],
            traps=[InvalidOperation, Overflow, Inexact, Rounded],
        )
        with localcontext(context):
            amount = self.amount - other.amount if subtract else self.amount + other.amount
        return type(self)(amount, self.currency)

    def to_decimal_string(self) -> str:
        return format(self.amount, ".2f")


@dataclass(frozen=True, slots=True)
class Percentage:
    value: Decimal

    def __post_init__(self) -> None:
        decimal_value = _require_decimal(self.value, field="percentage")
        sign, digits, exponent = _canonical_parts(decimal_value)
        if exponent < -6:
            invalid(
                code="excess_precision",
                field="percentage",
                message="must have at most six fractional digits",
            )
        canonical = Decimal(0) if decimal_value.is_zero() else Decimal((sign, digits, exponent))
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
