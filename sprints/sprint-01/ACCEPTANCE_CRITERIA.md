# Sprint 01 Acceptance Criteria

Status: Approved on 2026-08-27. Record objective evidence for every completed item in REVIEW.md.

## Activation and governance

- [x] Product owner approves SPRINT.md, DOMAIN_MODEL_SCOPE.md, and this file as one control pack.
- [x] An accountable domain and regulatory-scope reviewer is identified and accepts the
  responsibilities in DOMAIN_MODEL_SCOPE.md.
- [x] Every activation decision in DOMAIN_MODEL_SCOPE.md is resolved without inventing unsupported
  regulatory conclusions.
- [x] Root status documents consistently identify Sprint 01 as accepted and no later sprint active.
- [x] Material modeling decisions are recorded in accepted ADR 0002 under docs/adr/.

## Synthetic case and provenance

- [x] A versioned FinBank/Alpha Manufacturing fixture exists under data/finbank/ and contains only
  approved synthetic facts and assumptions.
- [x] The fixture represents FinBank, Alpha Manufacturing, a term-loan product, a facility, and an
  as-of exposure as distinct typed concepts.
- [x] The USD 10,000,000 source fact is original principal; no code assigns it an unapproved
  regulatory EAD meaning.
- [x] Every non-source fixture value links to a documented, approved assumption with provenance.
- [x] The fixture has stable identifiers, a schema version, a fixture version, and explicit date
  and as-of semantics.
- [x] Real customer data, institution-confidential data, credentials, and secrets are absent.

## Deterministic primitives

- [x] Typed identifiers cannot be empty and cannot be accidentally interchanged across entity types.
- [x] Currency construction follows policy sprint-01-v1 and rejects malformed or unsupported codes
  with stable validation errors.
- [x] Money uses exact Decimal values, at most two fractional digits, no binary floating point, and
  no implicit rounding.
- [x] Percentage uses exact Decimal values, at most six fractional digits, and field-specific bounds.
- [x] Date and as-of invariants reject inconsistent ranges and do not depend on current time, locale,
  or timezone.
- [x] Assumption and provenance types preserve stable IDs, source kind, locator/reference, status,
  and version context.

## Pure domain model

- [x] Institution, counterparty/borrower, product, facility, and exposure aggregates enforce the
  approved invariants at construction boundaries.
- [x] Domain construction is deterministic and immutable.
- [x] The pure domain package has no imports from FastAPI, Pydantic, databases, Redis, browser code,
  or LLM/provider SDKs.
- [x] The model performs no regulatory classification and contains no risk-weight, EAD, RWA,
  capital, jurisdiction-adapter, tutor, lesson, authentication, billing, or deployment logic.
- [x] Invalid and incomplete inputs produce typed, stable, field-local errors without guessed
  defaults.

## Serialization contract

- [x] A documented, versioned serialization contract exists for every public Sprint 01 domain type.
- [x] Serialize-deserialize round trips preserve identifiers, dates, currencies, exact numeric
  values, assumptions, provenance, schema version, and fixture version.
- [x] Unknown fields, missing required fields, unsupported versions, malformed decimals, and invalid
  cross-field states have explicit tested behavior.
- [x] Serialized field names and numeric encodings are stable and independent of display formatting.

## Tests and engineering integration

- [x] Unit tests cover normal construction, every invariant, and representative failure behavior.
- [x] Boundary tests cover zero, negative, maximum scale, excessive precision, malformed IDs and
  currencies, date-order errors, missing provenance, and cross-entity reference errors.
- [x] Property-based tests cover round trips and applicable arithmetic/ordering invariants using a
  pinned test dependency.
- [x] Tests demonstrate independence from locale, timezone, current time, and binary floating point.
- [x] The root task runner includes the Sprint 01 package in formatting, lint, type-check, test, and
  build tasks.
- [x] Python 3.12+, Ruff, strict mypy, pytest, explicit types, and pinned material dependencies are
  maintained.
- [x] Existing Sprint 00 API and web contracts continue to pass.

## Completion evidence

- [x] node scripts/task.mjs format-check passes.
- [x] node scripts/task.mjs lint passes.
- [x] node scripts/task.mjs typecheck passes.
- [x] node scripts/task.mjs test passes.
- [x] node scripts/task.mjs build passes.
- [x] node scripts/task.mjs e2e passes.
- [x] node scripts/task.mjs verify-artifacts confirms every finalized reference artifact is
  unchanged.
- [x] Docker/infrastructure validation is run only if affected; otherwise REVIEW.md records why it
  was not required.
- [x] REVIEW.md records command summaries, environment versions, limitations, deferrals, reviewer
  provenance, and the final acceptance decision.
