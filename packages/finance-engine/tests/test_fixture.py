import ast
from pathlib import Path

from financial_pods_finance_engine import (
    AssumptionStatus,
    SourceKind,
    load_case_fixture,
)

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_PATH = REPOSITORY_ROOT / "data" / "finbank" / "alpha_manufacturing_v1.json"
SOURCE_ROOT = (
    REPOSITORY_ROOT / "packages" / "finance-engine" / "src" / "financial_pods_finance_engine"
)


def test_approved_fixture_has_expected_case_identity_and_amount() -> None:
    case = load_case_fixture(FIXTURE_PATH)

    assert case.schema_version == "1.0"
    assert case.fixture_version == "1.0.0"
    assert case.currency_policy_version == "sprint-01-v1"
    assert case.institution.name == "FinBank"
    assert case.counterparty.legal_name == "Alpha Manufacturing"
    assert case.product.kind.value == "term_loan"
    assert case.facility.original_principal.to_decimal_string() == "10000000.00"
    assert case.exposure.outstanding_principal == case.facility.original_principal
    assert case.exposure.as_of_date == case.facility.origination_date


def test_fixture_assumptions_and_provenance_are_complete() -> None:
    case = load_case_fixture(FIXTURE_PATH)
    assumption_ids = {str(item.id) for item in case.assumptions}
    assumed_paths = {
        item.field_path
        for item in case.provenance
        if item.source_kind is SourceKind.APPROVED_ASSUMPTION
    }

    assert assumption_ids == {"ASM-FACILITY-DATES", "ASM-EXPOSURE-SNAPSHOT"}
    assert all(item.status is AssumptionStatus.APPROVED for item in case.assumptions)
    assert assumed_paths == {
        "facility.origination_date",
        "facility.maturity_date",
        "exposure.as_of_date",
        "exposure.outstanding_principal",
    }
    assert len(case.provenance) == 8


def test_domain_package_has_no_forbidden_imports() -> None:
    forbidden_roots = {
        "fastapi",
        "pydantic",
        "sqlalchemy",
        "psycopg",
        "redis",
        "openai",
        "anthropic",
    }
    imports: set[str] = set()

    for source_file in SOURCE_ROOT.glob("*.py"):
        tree = ast.parse(source_file.read_text(encoding="utf-8"), filename=str(source_file))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".", maxsplit=1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".", maxsplit=1)[0])

    assert imports.isdisjoint(forbidden_roots)
