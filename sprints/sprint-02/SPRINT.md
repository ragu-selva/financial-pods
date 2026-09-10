# Sprint 02 — Generalized Regulatory Classification + Calculation Engine

Status: ACTIVE

Activation date: 2026-09-10. Human decision: **APPROVED_FOR_INTERNAL_PROTOTYPE**.
Reviewer: **Ragunath Selvaraj — Project Owner / Internal Regulatory Reviewer**.
This is the owner's accountable internal-prototype approval, not independent legal counsel,
regulatory certification, production-bank sign-off or real-bank GAAP certification.

Sprint 02: **ACTIVE** on main through merged PR #4 at
`a89eeb60727c5f615514f75ecc27f57f19ec23cf`. The owner authorized the separate
`codex/sprint-02-us-corporate-engine` implementation branch. Implementation is present;
engineering verification and implementation PR review are recorded in REVIEW.md.
No automatic merge or broader regulatory scope is authorized.

## Goal

Implement the now-authorized, reusable Regulatory Classification + Calculation Engine. Its first executable
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

See [accepted ADR 0004](../../docs/adr/0004-generalized-regulatory-engine.md) for diagrams,
provider boundaries, dependencies, and the potential shared-core direction.
[FRAMEWORK_SCOPE.md](FRAMEWORK_SCOPE.md) preserves the approved design scope.
[RUNTIME_CONTRACT.md](RUNTIME_CONTRACT.md) finalizes the implemented v1 contracts without changing source approval.

## First implemented functional slice

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

Only USStandardizedRuleset is implemented in this slice. Contracts
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

## Approved Golden Case and source package

Preserve the accepted Sprint 01 fixture and regulatory/fact date **2025-01-01**.
[GOLDEN_CASE_APPROVED.json](GOLDEN_CASE_APPROVED.json) is the versioned internal-prototype
approval representation; the old candidate and source-boundary files remain historical inputs.

The approved synthetic state member bank is US/FRB standardized and has never elected CBLR.
Its ordinary fully drawn on-balance-sheet loan is to a non-financial manufacturing corporation.
All material negative facts and the zero-adjustment/zero-allowance accounting simplification
are explicitly accepted. These are stipulations, not verified real-bank facts or a CECL estimate.

Approved expectations: CORPORATE; EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE USD 10m;
risk weight 1.00; RWA USD 10m; only baseline_total_capital_equivalent USD 800k at 0.08.
The teaching amount is not allocated loan capital, economic capital, complete required regulatory
capital, an institution-specific requirement or a capital adequacy conclusion.

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) approves six rule scopes and eight required dependency
scopes for this exact date. Its pinned v0.4 documentary snapshot and all 71 raw captures remain
unchanged. Four conditional dependencies and two future-scope groups are not execution evidence.
Unknown interval ends stay unknown; R-1888 stays PROPOSED / executable=false.
No changed date, material fact or positive excluded treatment inherits this approval.

## Activation and human review

Sprint 00, Sprint 01 and Sprint 01 hardening remain accepted; PR #2 merged at b0cf3a9 and
post-merge cleanup at 5fcfc5a. PR #4 subsequently merged the activation at a89eeb6.
Ragunath Selvaraj explicitly accepted accountability and the source/Golden boundary for the
internal prototype on 2026-09-10. ACTIVATION_RECORD.json transcribes the human decision.
ADR 0004 is ACCEPTED. The existing source resolver skill is approved for evidence resolution
only; it cannot classify, calculate or grant approval. Its historical planning-run note is not
current sprint control. No AI is the accountable regulatory reviewer.

## Activation PR and implementation sequence — completed authorization gates

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

## Current implementation stop condition

Verify the narrow engine, publish codex/sprint-02-us-corporate-engine and open its review PR against main.
Stop with the implementation PR open; do not merge automatically or start another exposure class/sprint.
ACTIVATION_RECORD.json remains the immutable activation-time approval snapshot. The separate
IMPLEMENTATION_RECORD.json records the merged activation baseline and this authorized implementation.
The owner expressly requested a different-name case and a USD 5 million case with otherwise
identical approved assumptions; variable principal does not authorize other material fact changes.
