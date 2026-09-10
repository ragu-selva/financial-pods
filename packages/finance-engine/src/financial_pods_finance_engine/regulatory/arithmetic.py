"""Exact multiplication with an isolated context and no monetary rounding."""

from decimal import (
    MAX_EMAX,
    MIN_EMIN,
    Context,
    Decimal,
    Inexact,
    InvalidOperation,
    Overflow,
    Rounded,
    localcontext,
)

from ..errors import DomainValidationError
from ..primitives import Money
from .contracts import ratio
from .errors import ErrorCode, fail


def multiply_money(value: Money, factor: Decimal) -> Money:
    if type(value) is not Money or type(factor) is not Decimal:
        fail(ErrorCode.INVALID_TYPE, "multiplication", "Expected Money and Decimal ratio")
    ratio(factor)
    precision = len(value.amount.as_tuple().digits) + len(factor.as_tuple().digits) + 1
    context = Context(
        prec=precision,
        Emin=MIN_EMIN,
        Emax=MAX_EMAX,
        clamp=0,
        flags=[],
        traps=[InvalidOperation, Overflow, Inexact, Rounded],
    )
    with localcontext(context):
        result = value.amount * factor
    try:
        return Money(result, value.currency)
    except DomainValidationError as exc:
        if exc.issue.code == "excess_precision":
            fail(
                ErrorCode.ROUNDING_POLICY_UNDEFINED,
                "amount",
                "Exact output has fractional cents; no rounding is approved",
            )
        fail(ErrorCode.INVALID_TYPE, "amount", exc.issue.message)
