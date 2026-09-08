# Sprint 02 — Reviewed Regulatory Rules and Calculation Slice

Status: PLANNING ONLY — NOT ACTIVE

Publication is for architecture/regulatory review only, not implementation approval. Sprint 02
must not begin until the framework, jurisdiction, regulatory sources, calculation scope, golden
outputs, and regulatory review process are explicitly approved by the project owner and the
accountable regulatory reviewer. Candidate source claims below are preserved draft material from
2026-08-27, not freshly validated regulatory authority.

Status: Activation draft; not active. Implementation is blocked until every activation decision in
FRAMEWORK_SCOPE.md is approved and an accountable regulatory reviewer accepts the review role.

## Goal

Introduce one reviewed, versioned Basel Framework ruleset and use it to calculate the narrow Alpha
Manufacturing worked case deterministically from exposure amount through risk weight, risk-weighted
assets (RWA), and an explicitly labelled minimum-total-capital teaching relationship.

## Candidate scope

- Current consolidated BCBS Basel Framework as a canonical, non-jurisdictional teaching baseline
- One on-balance-sheet, performing, unsecured, unrated, non-SME general corporate term loan
- A versioned rule record, exact source locators, reviewer provenance, and immutable rule status
- Deterministic exposure classification, exposure amount, risk weight, RWA, and teaching output
- Structured calculation trace, stable reason/error codes, serialization, and reproducible fixtures
- Unit, boundary, property, golden, regression, and dependency-isolation tests

FRAMEWORK_SCOPE.md defines the candidate source snapshot, case assumptions, calculation boundary,
unresolved decisions, and approval record. ACCEPTANCE_CRITERIA.md is the completion contract.

## Explicit exclusions

- No claim that the BCBS baseline is directly binding law in any country
- No United States, SAMA, CBUAE, or other domestic implementation or comparison
- No IRB, specialised lending, corporate SME, regulatory retail, defaulted exposure, provisions,
  off-balance-sheet item, credit conversion factor, collateral, guarantee, netting, or other credit
  risk mitigation treatment
- No capital buffers, Pillar 2 add-ons, output-floor computation, deductions, available-capital
  adequacy conclusion, portfolio aggregation, or regulatory reporting mapping
- No database, API, UI, lesson, tutor, LLM, authentication, billing, or deployment feature
- No automatic source monitoring, rule ingestion, or publication workflow implementation

## Entry and activation gates

Sprint 01 is accepted and preserved in commit `03b03ec`. Sprint 01 hardening is accepted and
merged through PR #2 at `b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183` on 2026-09-08.
That acceptance does not activate Sprint 02.

This sprint becomes active only after the project owner and an accountable regulatory reviewer
approve SPRINT.md, FRAMEWORK_SCOPE.md, and ACCEPTANCE_CRITERIA.md together. Approval must resolve the
framework snapshot, case assumptions, rule interpretation, outputs, precision, and reviewer identity.
Root current-status documents are updated only after activation.

## Exit

Every acceptance criterion must pass with evidence in REVIEW.md. The accountable regulatory
reviewer must approve the source interpretation and golden expected results before the sprint can be
accepted.
