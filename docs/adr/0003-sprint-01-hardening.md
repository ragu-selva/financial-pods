# ADR 0003: Exact primitives and structural case-data integrity

- Status: Implemented; accountable reviewer acceptance pending the hardening PR
- Date: 2026-09-08
- Authority: Project owner's explicit Sprint 01 Integration and Hardening request
- Supersedes: No historical record; tightens enforcement of ADR 0002's existing promises

## Context

The original 41-test suite passed, but inventory probes found that Decimal.normalize/quantize
could round or produce NaN under caller contexts. FinBankCase accepted incomplete or nonexistent
provenance paths and retained mutable lists despite tuple annotations and frozen dataclasses.

## Decisions

1. Normalize exact Decimal coefficient/exponent tuples without arithmetic. Strip insignificant
   trailing zeros before scale validation, preserving the existing acceptance of 1.2300 as 1.23.
   Money retains exponent -2 and its zero sign; Percentage retains the existing canonical positive
   zero and plain-string format. Reject non-finite values and excess effective fractional scale.
   Do not introduce any new rounding rule or magnitude limit.
2. Existing Money addition/subtraction uses a fresh, fully specified Decimal context with enough
   coefficient precision for the exact result and traps for rounding/inexactness. Caller precision,
   rounding, exponent limits, clamp, traps, and flags cannot change the result. This hardens existing
   primitive arithmetic; it is not a regulatory calculation feature.
3. Schema 1.0 has an explicit supported-path allowlist in model.py. Require the eight original
   fixture fact paths: institution.name, counterparty.legal_name, product.kind,
   facility.original_principal, facility.origination_date, facility.maturity_date,
   exposure.as_of_date, and exposure.outstanding_principal. Money pair paths cover both amount and
   currency; optional child-path entries cannot substitute for that coverage.
4. IDs, references, product display name, version fields, and money subfields may additionally carry
   provenance. Assumption/provenance metadata, arbitrary traversal, collection indices, aggregate
   roots, and future regulatory fields are not supported fact paths. Duplicate paths remain invalid.
   Approved-assumption locators must reference an existing approved assumption. Unused approved
   assumptions are permitted; no new requirement to infer semantic truth or source authority is added.
5. Reject any non-exact-tuple assumptions/provenance input with invalid_type before iterating it.
   This matches existing strict runtime type checks and the annotated public constructor contract.
   Do not consume arbitrary iterators or silently normalize unordered collections. JSON arrays remain
   supported because the existing boundary adapter constructs tuples and immutable domain elements.

## Compatibility and consequences

No JSON field names, version strings, fixture bytes, dependency versions, or public constructor
annotations change. Previously valid complete payloads remain valid. Incomplete provenance and
mutable direct-constructor inputs now fail deliberately; callers must supply complete structural
provenance and exact tuples. Historical Sprint 01 acceptance is not rewritten.

This is structural validation, not proof that a cited source supports a value. Human review and
future regulatory citation/approval/version rules remain separate gates. No Sprint 02 work is
authorized. Regression/property tests cover the newly enforced contract.
