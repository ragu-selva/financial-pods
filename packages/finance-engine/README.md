# Financial Pods finance engine

This package contains the accepted Sprint 01 framework-independent domain model and the
Sprint 02 narrow US/FRB ordinary corporate regulatory engine (implementation pending PR review).

It owns exact money and percentage primitives, typed identifiers, assumptions, provenance, the
institution/counterparty/product/facility/exposure model, strict versioned serialization, and the
approved fixture loader.

It also owns immutable regulatory facts/results, deterministic registry/orchestration, one approved
U.S. provider, exact RWA and an educational total-capital equivalent with source-linked trace.
It contains no EAD alias, other regulatory treatments, web framework, database, Redis or LLM integration.

## Hardened schema 1.0 contract

Money (two fractional digits) and Percentage (six) reject excess effective precision without
rounding. Insignificant trailing zeros remain accepted. Validation, serialization, and existing
Money addition/subtraction are independent of caller Decimal precision, rounding, traps, and
exponent limits. Money serializes to two decimal places; Percentage uses canonical plain strings.

FinBankCase requires exact tuples of immutable Assumption and Provenance objects for direct Python
construction. Lists, sets, mappings, iterators, and tuple subclasses are rejected with invalid_type.
The JSON adapter still accepts arrays and converts them into tuples; schema/fixture versions and
the approved fixture remain unchanged.

Provenance paths must belong to model.SUPPORTED_PROVENANCE_PATHS. All eight paths in
model.REQUIRED_PROVENANCE_PATHS must occur exactly once. These are the existing fixture's names,
product kind, principal pairs, and dates. Principal-pair entries cover amount and currency together;
optional subfield entries do not replace the required pair. Invalid paths fail with
unsupported_provenance_path; incomplete nonempty coverage fails with missing_provenance_coverage
and a sorted missing-path list. Existing duplicate and assumption-reference errors are retained.

See docs/adr/0003-sprint-01-hardening.md at the repository root for rationale, the optional-path
policy, compatibility implications, and the distinction between structural and regulatory provenance.

## Sprint 02 calculation demonstration

From the repository root, with the package source on PYTHONPATH, run:

```python
from pathlib import Path
from financial_pods_finance_engine.regulatory import load_engine, result_to_json

engine, facts = load_engine(Path.cwd())
result = engine.calculate(facts)
print(result.classification.exposure_class)  # CORPORATE
print(result.rwa.amount)  # 10000000.00
print(result.capital_teaching_outputs[0].amount)  # 800000.00
print(result_to_json(result))  # authoritative result, trace and citations
```

For a one-command PowerShell demonstration without installation or environment changes:

```powershell
.venv/Scripts/python.exe -c 'import sys; sys.path.insert(0, "packages/finance-engine/src"); from pathlib import Path; from financial_pods_finance_engine.regulatory import load_engine; engine, facts = load_engine(Path.cwd()); result = engine.calculate(facts); print(result.classification.exposure_class, result.rwa.amount, result.capital_teaching_outputs[0].amount, len(result.calculation_trace.steps))'
```

The adapter requires this repository's approved local Sprint 02 evidence files; the wheel does not
embed the legal corpus. Calculation itself is in-memory and makes no external calls.
Only US/FRB standardized at 2025-01-01 with the exact approved version is supported.
The 8% amount is educational, not allocated loan capital or a complete bank capital requirement.
See sprints/sprint-02/RUNTIME_CONTRACT.md for v1 schemas, exclusions, exact arithmetic,
approved source pins and alternate-case rules. Runtime tests: tests/test_regulatory.py.
