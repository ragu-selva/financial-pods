"""Pure regulatory contracts/engine with an explicit local evidence-loading boundary."""

from pathlib import Path

from .contracts import RegulatoryCalculationResult, RegulatoryFactSnapshot
from .engine import RegulatoryEngine, RulesetRegistry
from .errors import ErrorCode, RegulatoryError
from .serialization import error_to_json, result_to_dict, result_to_json, snapshot_from_dict
from .us_sources import load_golden_snapshot, load_us_source_package
from .us_standardized import USStandardizedRuleset


def load_engine(repository: Path) -> tuple[RegulatoryEngine, RegulatoryFactSnapshot]:
    """Composition helper: disk I/O occurs here, never during calculate()."""
    package = load_us_source_package(repository / "sprints" / "sprint-02")
    provider = USStandardizedRuleset(package)
    registry = RulesetRegistry(
        providers=(provider,),
        prohibited_versions=("R-1888-PROPOSAL",),
    )
    return RegulatoryEngine(registry), load_golden_snapshot(repository, package)


__all__ = [
    "ErrorCode",
    "RegulatoryCalculationResult",
    "RegulatoryEngine",
    "RegulatoryError",
    "RegulatoryFactSnapshot",
    "RulesetRegistry",
    "USStandardizedRuleset",
    "error_to_json",
    "load_engine",
    "result_to_dict",
    "result_to_json",
    "snapshot_from_dict",
]
