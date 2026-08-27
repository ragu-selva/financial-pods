import re
from dataclasses import dataclass
from typing import ClassVar

from .errors import invalid

_IDENTIFIER_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")


@dataclass(frozen=True, slots=True)
class _Identifier:
    value: str

    prefix: ClassVar[str]

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            invalid(code="invalid_type", field="identifier", message="must be a string")
        if self.value != self.value.strip() or not self.value:
            invalid(code="invalid_identifier", field="identifier", message="must be non-empty")
        if not _IDENTIFIER_PATTERN.fullmatch(self.value):
            invalid(
                code="invalid_identifier",
                field="identifier",
                message="must contain uppercase letters, digits, and hyphen-separated segments",
            )
        if not self.value.startswith(f"{self.prefix}-"):
            invalid(
                code="invalid_identifier_prefix",
                field="identifier",
                message=f"must start with {self.prefix}-",
            )

    def __str__(self) -> str:
        return self.value


class InstitutionId(_Identifier):
    prefix = "INS"


class CounterpartyId(_Identifier):
    prefix = "CP"


class ProductId(_Identifier):
    prefix = "PRD"


class FacilityId(_Identifier):
    prefix = "FAC"


class ExposureId(_Identifier):
    prefix = "EXP"


class AssumptionId(_Identifier):
    prefix = "ASM"
