# Sprint 02 — Planning Checks and Post-Activation Test Vectors

Status: ACTIVE

## Checks authorized now

Run: node --test sprints/sprint-02/planning-evidence.test.mjs

The planning-evidence suite preserves checks of the unchanged reviewed v0.4 manifest,
historical candidate/fact boundary and former unfilled activation record. It also checks that the
current controls are ACTIVE and ADR 0004 is accepted. Historical inactive records are not current control.

Run also: node --test sprints/sprint-02/activation-evidence.test.mjs

Activation checks enforce the human identity/decision, exact source/fact pins, narrow approval
allowlist, fixed as-of date, proposal rejection, preserved unknown endpoints, unchanged Golden
amounts, synthetic simplifications and preserved activation-time approval. Current implementation
checks separately enforce the merged activation baseline. These are offline artifact
checks, not runtime regulatory calculations and not independent legal review.

## Runtime tests implemented after activation

The runtime suite is packages/finance-engine/tests/test_regulatory.py. These vectors were planned
before activation; current v1 mappings and exact verification counts are in RUNTIME_CONTRACT.md and
REVIEW.md. Exact-date-only execution replaces a general historical interval selector; no later final
ruleset is implemented. Draft v0.2 examples below have been finalized as v1, not silently aliased.

### Measure/result/trace contracts

- Golden result emits regulatory_exposure_measure with exactly amount, currency, measure_type,
  measurement_basis, rule_refs, warnings; U.S. EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE.
- Reject EAD discriminator for this provider and wrong basis/type combinations. Reject top-level
  ead and the former duplicate exposure_amount output. No alias-warning workaround.
- RWA uses the typed measure, not original principal or a hidden alias; carrying-value
  reconciliation is traced and adjustments cannot be double-subtracted.
- Trace v0.2 measurement step emits the typed measure; RWA step inputs bind that output and
  risk_weight, preserving basis, rule version, reason, source locator and warnings.
- Result v0.2 rejects old v0.1/unknown fields; future EAD providers require separate approved contracts.
- Emit exactly baseline_total_capital_equivalent at 0.08; reject CET1/Tier 1 and other teaching names.
  Enforce educational/not-allocated/not-institution-specific/not-adequacy warnings.

### U.S. classification

- Positive corporate fixture: company plus evidence excluding § 217.2 corporate paragraphs (1)-(14).
- Parameterize each paragraph and each named alternative in paragraph (1): YES prevents the
  ordinary corporate path; UNKNOWN/missing/contradictory evidence returns a typed error.
- Generic specialised lending, regulatory retail, BCBS SME and external-rating labels alone
  cannot change corporate status. An approved U.S. mapping is required before using such concepts.
  A contradictory sourced mortgage/HVCRE fact still triggers its U.S. rule, not a generic label.
- § 217.32(f)(2)-(3), (k), § 217.30(b), measurement exceptions and CRM/product restrictions
  cannot be bypassed. Unsupported product scope is not fabricated legal reclassification.
- Changing borrower display name or case ID does not affect financial results.
  Alternate ordinary corporate amount uses identical orchestration and reviewed expected values.

### Ruleset selection and proposal exclusion

- R-1888 by direct ID -> RULESET_STATUS_NOT_EXECUTABLE, no successful financial result.
- R-1888 accidentally assigned CURRENT alias -> reject based on immutable proposal evidence.
- R-1888 with review_status=APPROVED or executable=true -> reject; internal flags cannot change law.
- Proposal rate copied into a current rule without approved final-source evidence -> integrity/
  approval failure, never a silent overwrite.
- A later final rule is a different reviewed immutable record, effective for its selected date;
  it cannot alter a replay of the accepted 2025 snapshot.
- Future-effective rule at 2025-01-01 -> RULESET_NOT_EFFECTIVE. Test before/on/after interval bounds.
- Null interval, incomplete source metadata, hash mismatch, wrong jurisdiction/regime, ambiguous
  version, revoked approval and unapproved source -> typed failure, no fallback.
- Historical CURRENT-as-of policy handles later supersession explicitly, without replacing
  2025 authority with the latest retrieval or ignoring review/validity gates.
- Missing reviewer sign-off or source approval prevents activation; a passing test suite is not sign-off.

### Determinism and safety properties

- Modified Decimal contexts cannot round accepted values; exact ratios/units, no float arithmetic.
- Immutable facts, measures and traces; canonical fact/manifest hashes stable for repeated inputs.
- No wall-clock, random, network, database or LLM effects in the calculation boundary.
- Source citations/trace refs resolve to selected approved U.S. records; no BCBS fallback.
- Accepted Sprint 01 fixture remains byte-identical; separately versioned regulatory enrichment
  retains 2025-01-01 and all material facts/provenance.
- Existing baseline tests, formatting, lint, types, builds and artifact verification remain passing.

Runtime engineering checks are implemented; human implementation review/acceptance remains pending.
Sprint 02: ACTIVE. No automatic implementation PR merge.
