from dataclasses import dataclass
from typing import NoReturn


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str
    field: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {"code": self.code, "field": self.field, "message": self.message}


class DomainValidationError(ValueError):
    def __init__(self, issue: ValidationIssue) -> None:
        self.issue = issue
        super().__init__(f"{issue.field}: {issue.message}")


def invalid(*, code: str, field: str, message: str) -> NoReturn:
    raise DomainValidationError(ValidationIssue(code=code, field=field, message=message))
