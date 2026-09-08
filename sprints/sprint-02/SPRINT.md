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
selected jurisdiction ruleset -> regulatory treatment -> risk weight + typed regulatory exposure
measure -> RWA -> baseline_total_capital_equivalent -> calculation / regulatory trace.

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
- Corporate classification from the selected 2025 § 217.2 definition and applicable Part 217 rules,
  not borrower identity or generic BCBS retail/SME/rating/specialised-lending labels.
- Approved U.S. exposure measure, risk weight, RWA, and narrowly labelled educational capital output.
- RegulatoryExposureMeasure uses EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE; no EAD alias.
- Exactly one educational output at ratio 0.08; no CET1 or Tier 1 equivalents.
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

Keep the accepted Sprint 01 fixture unchanged and preserve regulatory/fact as-of **2025-01-01**.
Only separately versioned enrichment at that same date is proposed; re-dating is not an alternative.
Dated eCFR sections and a GovInfo annual edition are captured in SOURCE_MANIFEST.json, with raw-byte
SHA-256 evidence. Effective intervals, full relevant amendment history and interpretation remain
human-review gates. A 2026 retrieval/compilation is not proof of 2025 applicability.

The final candidate is a synthetic Board-regulated state member bank, U.S./Federal Reserve,
US_FRB_PART217_STANDARDIZED, CBLR not elected, ordinary fully drawn on-balance-sheet corporate
term loan to a synthetic non-financial company, USD 10 million GAAP carrying value, zero past-due
days and nonaccrual=false, reviewed exclusion negatives and no CRM in scope.
Candidate outputs: CORPORATE, risk-weight ratio 1.00, regulatory exposure measure USD 10 million
(EXPOSURE_AMOUNT), RWA USD 10 million, baseline_total_capital_equivalent USD 800,000 at ratio 0.08.
All regulatory assumptions/results are PENDING named human approval. The 8% transformation is
educational, based on the minimum total-capital ratio, not allocated loan capital, an institution-
specific requirement, or a capital adequacy conclusion.

The earlier BCBS-first draft, its unrated/non-SME selection logic, and EUR sales threshold are
superseded as Sprint 02 execution proposals. They remain in Git history, not executable assumptions.
U.S. provider fact requirements must be justified from the selected U.S. rule version.

## Activation and human review

Sprint 00, Sprint 01, and Sprint 01 hardening are accepted; PR #2 merged at b0cf3a9 and the
post-merge documentation cleanup merged through PR #3 at 5fcfc5a. Neither activates Sprint 02.

Before implementation, the project owner and a personally named human regulatory reviewer must
explicitly approve the framework, jurisdiction/perimeter, exact source versions/locators, interpretation,
minimum facts and Golden Case assumptions, calculation scope, classification, risk weight, RWA,
the typed exposure measure, the sole capital-teaching output, exclusions, and regulatory review process.
ACTIVATION_RECORD.json leaves all seven accountable-reviewer fields null for owner-supplied approval.
AI must not populate the identity, accept responsibilities, or sign off.

AI may assist research or checking but cannot be the accountable regulatory reviewer.
All unresolved items are tracked in FRAMEWORK_SCOPE.md and REVIEW.md. ADR 0004 remains proposed
until activation. Approval of this architecture direction is not approval of a financial result.

## Activation PR and implementation sequence

1. Complete human-approved control documents, source/interpretation manifest, all source hashes
   and effective dates, Golden Case assumptions/expected outputs and accountable reviewer record.
2. Only after every prerequisite is complete, create codex/sprint-02-activation from current main.
   Transfer only approved control documents, accepted ADR 0004, approved source manifest/evidence,
   Golden Case regulatory assumptions/expected outputs and activation decision/status changes.
   Do not wholesale merge the planning branch or include regulatory engine implementation.
3. Open a review PR targeting main; do not merge automatically. A draft pack or blank reviewer
   record is not a ready activation PR.
4. Only after review and merge may implementation start on codex/sprint-02-us-corporate-engine
   from the activated main baseline: generic contracts, registry, one U.S. provider, corporate
   classification, regulatory exposure amount, approved 100% weight, RWA, 8% educational total-
   capital equivalent, trace, source/version enforcement, Golden/alternate-name/alternate-amount
   cases and regulatory regression/property tests. No other jurisdictions or exposure classes.

## Stop condition for this preparation

Revise the controls/ADR and non-executable review artifacts, run planning-evidence checks and
baseline verification, and push codex/sprint-02-planning. Any missing regulatory approval blocks
activation PR creation. Do not merge this planning branch into main or activate implementation.

SPRINT 02 REMAINS INACTIVE
