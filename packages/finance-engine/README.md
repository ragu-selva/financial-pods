# Financial Pods finance engine

This package contains the Sprint 01 framework-independent domain model for the synthetic FinBank /
Alpha Manufacturing case.

It owns exact money and percentage primitives, typed identifiers, assumptions, provenance, the
institution/counterparty/product/facility/exposure model, strict versioned serialization, and the
approved fixture loader.

It deliberately contains no regulatory classification, risk weights, EAD, RWA, capital logic,
jurisdiction adapters, web framework, database, Redis, or LLM integration.

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
