from dataclasses import dataclass
from enum import StrEnum

from .errors import invalid
from .identifiers import AssumptionId


class SourceKind(StrEnum):
    FINALIZED_REFERENCE = "finalized_reference"
    APPROVED_ASSUMPTION = "approved_assumption"


class AssumptionStatus(StrEnum):
    APPROVED = "approved"


def _require_text(value: object, *, field: str) -> None:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        invalid(code="invalid_text", field=field, message="must be a non-empty trimmed string")


@dataclass(frozen=True, slots=True)
class Assumption:
    id: AssumptionId
    description: str
    value: str
    status: AssumptionStatus
    approval_reference: str

    def __post_init__(self) -> None:
        if type(self.id) is not AssumptionId:
            invalid(code="invalid_type", field="assumption.id", message="must be an AssumptionId")
        _require_text(self.description, field="assumption.description")
        _require_text(self.value, field="assumption.value")
        if type(self.status) is not AssumptionStatus:
            invalid(
                code="invalid_type",
                field="assumption.status",
                message="must be an AssumptionStatus",
            )
        _require_text(self.approval_reference, field="assumption.approval_reference")


@dataclass(frozen=True, slots=True)
class Provenance:
    field_path: str
    source_kind: SourceKind
    source_locator: str
    source_version: str

    def __post_init__(self) -> None:
        _require_text(self.field_path, field="provenance.field_path")
        if type(self.source_kind) is not SourceKind:
            invalid(
                code="invalid_type",
                field="provenance.source_kind",
                message="must be a SourceKind",
            )
        _require_text(self.source_locator, field="provenance.source_locator")
        _require_text(self.source_version, field="provenance.source_version")
