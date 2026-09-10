"""Stable fail-closed errors; never substitute a numeric result for a failure."""

from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING, NoReturn

if TYPE_CHECKING:
    from .contracts import CalculationTrace


class ErrorCode(StrEnum):
    INVALID_TYPE = "INVALID_TYPE"
    INVALID_SCHEMA = "INVALID_SCHEMA"
    MISSING_REQUIRED_FACT = "MISSING_REQUIRED_FACT"
    UNKNOWN_FACT = "UNKNOWN_FACT"
    CONFLICTING_FACTS = "CONFLICTING_FACTS"
    UNSUPPORTED_EXPOSURE_SCOPE = "UNSUPPORTED_EXPOSURE_SCOPE"
    INSTITUTION_OUT_OF_SCOPE = "INSTITUTION_OUT_OF_SCOPE"
    UNKNOWN_RULESET = "UNKNOWN_RULESET"
    UNSUPPORTED_JURISDICTION = "UNSUPPORTED_JURISDICTION"
    AMBIGUOUS_RULESET = "AMBIGUOUS_RULESET"
    RULESET_NOT_APPROVED = "RULESET_NOT_APPROVED"
    RULESET_NOT_EFFECTIVE = "RULESET_NOT_EFFECTIVE"
    RULESET_STATUS_NOT_EXECUTABLE = "RULESET_STATUS_NOT_EXECUTABLE"
    SOURCE_EVIDENCE_INCOMPLETE = "SOURCE_EVIDENCE_INCOMPLETE"
    SOURCE_HASH_MISMATCH = "SOURCE_HASH_MISMATCH"
    CURRENCY_MISMATCH = "CURRENCY_MISMATCH"
    EXCESS_PRECISION = "EXCESS_PRECISION"
    ROUNDING_POLICY_UNDEFINED = "ROUNDING_POLICY_UNDEFINED"
    INVALID_PROVENANCE = "INVALID_PROVENANCE"


class RegulatoryError(ValueError):
    def __init__(
        self, code: ErrorCode, field_path: str, message: str, rule_refs: tuple[str, ...] = ()
    ) -> None:
        self.code = code
        self.field_path = field_path
        self.message = message
        self.rule_refs = rule_refs
        self.validation_trace: CalculationTrace | None = None
        super().__init__(f"{code}: {field_path}: {message}")


def fail(code: ErrorCode, field: str, message: str, rules: tuple[str, ...] = ()) -> NoReturn:
    raise RegulatoryError(code, field, message, rules)
