# Sprint 02 Acceptance Criteria — Generic Engine, U.S. First

Status: PLANNING ONLY — NOT ACTIVE

Architecture direction approved by the owner on 2026-09-08; these implementation/activation criteria
are proposed and unfulfilled. A checked drafting task in REVIEW.md does not satisfy a regulatory gate.

## Activation and personally accountable review

- [ ] Owner and personally named human regulatory reviewer approve this pack and proposed ADR 0004.
- [ ] Reviewer name, qualifications/role, authority, accepted responsibilities, review date, and
  evidence are recorded. An AI system cannot occupy this role.
- [ ] Framework, jurisdiction/institution perimeter, regulatory sources, calculation scope, golden
  outputs, and review process are explicitly approved together.
- [ ] Golden Case as-of date is reconciled with effective-dated U.S. sources; neither retrieval date
  nor a current compilation substitutes for proof of historical applicability.
- [ ] Exact U.S. locators, interpretations, snapshots/content hashes, publication/amendment metadata,
  effective intervals, statuses, and exclusions are approved.
- [ ] An explicit activation decision changes planning status; architecture approval alone does not.

## Generic architecture and scope

- [ ] Generic facts, validation, classification dispatch, provider selection, treatment, measurement,
  risk weight, RWA, educational outputs, and trace are separate typed contracts.
- [ ] Only the approved USStandardizedRuleset corporate slice is implemented after activation.
- [ ] Generic orchestration has no borrower/case-name logic and no scattered jurisdiction conditionals.
- [ ] BCBS is conceptual context, never an automatic executable U.S. fallback.
- [ ] Provider contracts permit later BCBS/SAMA/CBUAE implementations without implementing them now.
- [ ] No broad Basel calculator, other exposure-class calculators, UI/API business route, persistence,
  LLM/tutor, ingestion, content generation, or repository extraction is introduced.
- [ ] Future analysis of the owner's Basel/ERBA engine is recorded, not substituted by blind recreation.

## Facts and classification

- [ ] All material facts required by the selected U.S. provider are explicit and provenance-linked.
- [ ] Missing/unknown/contradictory material facts produce stable typed errors, never default values.
- [ ] Institution/regulator/regime applicability and CBLR exclusion are explicitly validated.
- [ ] The complete versioned U.S. corporate exclusion screen is approved and cannot be bypassed by
  declaring exposure_class=CORPORATE or naming the borrower.
- [ ] Nonaccrual/past-due/default and excluded exposure/CRM states are rejected by this narrow path.
- [ ] Annual sales/external rating are not imported as BCBS-driven thresholds for ordinary U.S. treatment.
- [ ] The accepted Sprint 01 fixture/schema are unchanged; approved enrichment has a separate version.
- [ ] Classification includes jurisdiction, ruleset/version, class/subclass, reason_codes, rule_refs,
  warnings, and schema version, without borrower-specific logic.

## Measurement, numeric integrity, and outputs

- [ ] Carrying-value treatment is tied to the approved U.S. definition and accounting reconciliation.
  Provisions/write-offs are not blindly subtracted or counted twice.
- [ ] Exposure amount, risk weight, RWA, and teaching outputs match independently approved U.S.
  expected results; numerical agreement with a BCBS example is not validation.
- [ ] Generic EAD field semantics/alias warning are approved; no advanced-approaches EAD is implied.
- [ ] Decimal operations remain exact and context-independent; ratio units are explicit and tested
  against the existing percentage-point primitive. No implicit rounding or guessed rounding policy.
- [ ] Result includes classification, regulatory treatment, exposure_amount, risk_weight, ead, rwa,
  capital_teaching_outputs, ruleset/rule versions, input hash, trace, citations, warnings, and exclusions.
- [ ] Educational equivalents are not labelled actual capital ratios, complete required capital, or
  adequacy conclusions. No unapproved teaching output or buffer is added.

## Effective-dated rules and immutable evidence

- [ ] CURRENT/PROPOSED/FUTURE/SUPERSEDED are distinct from internal reviewer approval.
- [ ] Execution requires APPROVED, effective-for-as-of, permitted legal status, correct jurisdiction,
  and matching source/manifest evidence. No eligible match or overlapping matches are typed errors.
- [ ] Proposal, future, revoked, unapproved, and superseded-as-live-default cases cannot execute.
- [ ] A CURRENT display alias is resolved once to a pinned manifest and recorded; no silent upgrades.
- [ ] Approved content is immutable; lifecycle changes preserve prior manifest/status snapshots.
- [ ] Historical replay policy is explicitly approved before any replay behavior is enabled.

## Trace, serialization, and reproducibility

- [ ] Every trace step has ID/order, operation, rule ID/version or engine-contract ref, reason code,
  source locator, inputs used, typed output, and warnings.
- [ ] Regulatory references resolve to U.S. authority; conceptual BCBS links are separately labelled.
- [ ] Hash and canonical serialization policies are documented and tested, including plain decimals,
  ISO dates, schema versions, stable ordering, and rejection of unknown/missing fields.
- [ ] Repeated identical inputs/versions produce reproducible calculations and evidence without
  network, wall-clock, random, database, or LLM dependencies.
- [ ] Failed requests return typed errors/failure trace and no successful financial outputs.

## Tests required before eventual Sprint 02 acceptance

- [ ] Golden outputs and exclusions are independently signed off by the named human reviewer.
- [ ] Borrower-name/ID invariance and another ordinary corporate amount prove generic orchestration;
  identity metadata may differ, financial outputs may not depend on it.
- [ ] Boundary tests cover missing facts, contradictory balance-sheet flags, carrying-value
  reconciliation, nonzero/out-of-scope adjustments, nonaccrual/past-due states, and each scope guard.
- [ ] Version/status tests cover proposal/current confusion (including the 2026 proposal candidate),
  effective-date boundaries, overlaps, mismatched hashes, revocations, and unapproved rules.
- [ ] Property/regression tests cover exact arithmetic, immutable facts/results, canonical hashes,
  trace/source completeness, and deterministic provider calls.
- [ ] Existing Sprint 00 and hardened Sprint 01 tests continue to pass.
- [ ] Formatting, lint, mypy/TypeScript, tests, builds, artifact hashes, and relevant E2E/infrastructure
  checks pass with exact evidence and limitations in REVIEW.md.

No implementation acceptance is recorded by this document revision.
SPRINT 02 REMAINS INACTIVE
