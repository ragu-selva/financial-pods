# Sprint 02 Acceptance Criteria

Status: Activation draft; not approved. Record objective evidence for completed items in REVIEW.md.

## Activation and governance

- [ ] Project owner approves SPRINT.md, FRAMEWORK_SCOPE.md, and this file together.
- [ ] A personally named accountable regulatory reviewer accepts responsibility for the official
  source interpretation and golden expected results.
- [ ] Every activation decision in FRAMEWORK_SCOPE.md is resolved.
- [ ] Exact source snapshots/hashes and current-version metadata are captured before implementation.
- [ ] Root status documents consistently identify Sprint 02 as active only after approval.
- [ ] Material architecture/rule-contract decisions are recorded in an accepted ADR.

## Regulatory source and rule model

- [ ] The ruleset is explicitly a BCBS canonical baseline and cannot be presented as domestic law.
- [ ] Every executable rule carries authority/framework, jurisdiction, source URL, locator,
  publication/effective/retrieval dates, version/hash, applicability, status, and reviewer provenance.
- [ ] Draft/unapproved/superseded rules are non-executable by default.
- [ ] Legacy CRE20 paragraph numbering is absent from the current executable rule version.
- [ ] Approved rule records and expected results are immutable; corrections create new versions.
- [ ] The candidate ruleset implements only the approved in-scope path and rejects excluded paths.

## Synthetic case and deterministic calculation

- [ ] The Sprint 01 fixture remains reproducible and gains only approved, versioned Sprint 02 facts.
- [ ] Classification requires explicit facts and produces stable rule/reason codes.
- [ ] Exposure amount is calculated deterministically with explicit provision/write-off treatment.
- [ ] Risk weight, RWA, and minimum-total-capital teaching amount match approved golden outputs.
- [ ] The teaching amount is never labelled or exposed as a complete required-capital conclusion.
- [ ] No LLM, database, web framework, Redis, locale, timezone, or current-time input affects results.
- [ ] Decimal precision and undefined-rounding behavior match the approved policy.
- [ ] Invalid, missing, conflicting, or out-of-scope inputs produce typed stable errors with no guessed
  defaults.

## Trace and serialization

- [ ] Each result records run/as-of IDs, input hash, fixture/schema/ruleset/rule versions, exact
  decimals, ordered steps, reason codes, citations, warnings, and exclusions.
- [ ] Serialization is strict, versioned, canonical, and round-trips without losing provenance.
- [ ] Unknown/missing fields, unsupported versions/statuses, tampered hashes, and unapproved rules
  have explicit tested behavior.
- [ ] Re-running identical approved inputs produces byte-equivalent canonical output apart from a
  caller-supplied run ID, if the run ID is part of the contract.

## Tests and engineering integration

- [ ] Unit tests cover every rule branch and representative failure behavior.
- [ ] Golden and regulatory regression tests use reviewer-approved expected outputs.
- [ ] Boundary tests cover the SME threshold, zero/excess provisions, rating states, dates, decimal
  precision, and every scope rejection.
- [ ] Property tests cover multiplication identities and deterministic serialization where valid.
- [ ] Tests prove the finance domain/rule packages have no prohibited framework/provider imports.
- [ ] Root format, lint, type-check, test, and build tasks include all Sprint 02 code and fixtures.
- [ ] Existing Sprint 00 and Sprint 01 contracts continue to pass.

## Completion evidence

- [ ] `node scripts/task.mjs format-check` passes.
- [ ] `node scripts/task.mjs lint` passes.
- [ ] `node scripts/task.mjs typecheck` passes.
- [ ] `node scripts/task.mjs test` passes.
- [ ] `node scripts/task.mjs build` passes.
- [ ] `node scripts/task.mjs e2e` passes if affected; otherwise REVIEW.md records why not.
- [ ] `node scripts/task.mjs verify-artifacts` confirms every finalized reference artifact is
  unchanged.
- [ ] Infrastructure validation runs if affected; otherwise REVIEW.md records why not.
- [ ] `git diff --check` passes.
- [ ] REVIEW.md records command evidence, environment versions, limitations, deferrals, source
  metadata, reviewer provenance, and final acceptance decision.

## Final review

- [ ] Accountable regulatory reviewer approves the implemented interpretation and golden results.
- [ ] Project owner accepts the sprint only after every applicable criterion has evidence.
