# Sprint 02 — Generalized Regulatory Classification + Calculation Engine

Status: PLANNING ONLY — NOT ACTIVE

Revision date: 2026-09-08. The project owner approved the product architecture direction, not
regulatory interpretations, Golden Case outputs, source versions, or implementation activation.
No production code may be written under this planning revision.

## Goal

Design a reusable Regulatory Classification + Calculation Engine. Its first eventual executable
slice is the United States standardized corporate-exposure path under an approved, effective-dated
12 CFR Part 217 ruleset. FinBank lending USD 10,000,000 to Alpha Manufacturing is the first Golden
Case, not an engine design constraint. Names and case IDs must never select rules or results.

## Architecture direction

Exposure / counterparty facts -> fact validation -> generic classification/orchestration ->
selected jurisdiction ruleset -> regulatory treatment -> risk weight -> exposure amount / EAD
mapping -> RWA -> capital teaching outputs -> calculation / regulatory trace.

The ruleset is resolved from explicit jurisdiction, regulatory perimeter, as-of date, and exact
approved version before regulatory classification. The generic classifier dispatches through that
provider; it does not first guess a BCBS classification and then override it with U.S. conditions.
The diagram is a conceptual flow, not a requirement that exposure measurement depend on risk weight.

BCBS supplies common terminology, conceptual taxonomy, RWA/capital concepts, and comparison
references. Executable results belong to a selected jurisdiction ruleset. BCBS is not automatically
binding U.S. law and is not a fallback when U.S. rules or facts are missing.

See [proposed ADR 0004](../../docs/adr/0004-generalized-regulatory-engine.md) for diagrams,
provider boundaries, dependencies, and the potential shared-core direction.
[FRAMEWORK_SCOPE.md](FRAMEWORK_SCOPE.md) owns draft source, fact, output, and trace contracts.

## First eventual functional slice

- Explicit U.S. / Federal Reserve Part 217 applicability and version selection.
- Structural validation and jurisdiction-specific fact requirements with typed errors.
- One ordinary, performing, fully drawn, on-balance-sheet corporate term-loan path.
- Corporate classification and treatment resolution from facts, not borrower identity.
- Approved U.S. exposure measure, risk weight, RWA, and narrowly labelled educational capital output.
- Explicit EAD mapping semantics, without importing an advanced-approaches model.
- Versioned classification/result contracts and first-class, source-linked trace.
- Name-invariance and alternate synthetic corporate-case tests demonstrating generic orchestration.
- Source/status/hash/date/reviewer gates; no unapproved executable rules.

Only USStandardizedRuleset is planned for initial implementation after activation. Contracts should
permit BCBSStandardizedRuleset, SAMAStandardizedRuleset, and CBUAEStandardizedRuleset later.
Do not implement placeholder providers with invented regulatory behavior.

## Scope exclusions

No broad Basel III calculator; other exposure classes; IRB/ERBA; advanced-approaches EAD;
off-balance-sheet CCF; derivatives; CRM; guarantees/netting; real-estate, retail, SME-specific,
defaulted, subordinated, equity, bank, or sovereign treatments. These may be recognized as excluded
inputs, not calculated.

No actual capital adequacy ratios, capital composition, portfolio aggregation, buffers, stress/Pillar 2
add-ons, leverage requirements, reporting conclusions, or institution-specific capital advice.
No API business routes, database persistence, UI/Golden Lesson, tutor/LLM, content/video generation,
authentication, billing, cloud deployment, automatic regulatory ingestion, or monitoring.

No extraction to another repository. Potential Regxify Regulatory Core reuse and comparison with the
owner's existing Basel/ERBA engine are later architectural work, not authorization to copy/rebuild it.

## Golden Case policy

Keep the accepted Sprint 01 fixture unchanged. Any regulatory fact enrichment or re-dating requires
a separately versioned fixture and explicit approval. The existing snapshot is 2025-01-01; a source
retrieved in 2026 does not establish its applicability to that snapshot.

The earlier BCBS-first draft, its unrated/non-SME selection logic, and EUR sales threshold are
superseded as Sprint 02 execution proposals. They remain in Git history, not executable assumptions.
U.S. provider fact requirements must be justified from the selected U.S. rule version.

## Activation and human review

Sprint 00, Sprint 01, and Sprint 01 hardening are accepted; PR #2 merged at b0cf3a9 and the
post-merge documentation cleanup merged through PR #3 at 5fcfc5a. Neither activates Sprint 02.

Before implementation, the project owner and a personally named human regulatory reviewer must
explicitly approve the framework, jurisdiction/perimeter, exact source versions/locators, interpretation,
minimum facts and Golden Case assumptions, calculation scope, classification, risk weight, RWA,
capital-teaching outputs, EAD naming, exclusions, and regulatory review process.

AI may assist research or checking but cannot be the accountable regulatory reviewer.
All unresolved items are tracked in FRAMEWORK_SCOPE.md and REVIEW.md. ADR 0004 remains proposed
until activation. Approval of this architecture direction is not approval of a financial result.

## Stop condition for this revision

Revise the four planning controls and proposed ADR, verify documentation-only scope, and push
codex/sprint-02-planning for architecture/regulatory review. Do not merge this branch into main.
Do not activate implementation.

SPRINT 02 REMAINS INACTIVE
