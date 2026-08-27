import json
from pathlib import Path

from .errors import invalid
from .model import FinBankCase
from .serialization import case_from_dict


def load_case_fixture(path: Path) -> FinBankCase:
    if not isinstance(path, Path):
        invalid(code="invalid_type", field="path", message="must be a pathlib.Path")
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        invalid(code="fixture_read_error", field="path", message=str(exc))
    try:
        payload: object = json.loads(raw)
    except json.JSONDecodeError as exc:
        invalid(code="invalid_json", field="fixture", message=str(exc))
    return case_from_dict(payload)
