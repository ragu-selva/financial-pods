# Sprint 02 Review

Status: PLANNING ONLY — NOT ACTIVE

Publication is for architecture/regulatory review only, not implementation approval. Sprint 02
must not begin until the framework, jurisdiction, regulatory sources, calculation scope, golden
outputs, and regulatory review process are explicitly approved by the project owner and the
accountable regulatory reviewer. Candidate source claims below are preserved draft material from
2026-08-27, not freshly validated regulatory authority.

Status: Activation draft; implementation not started.

## Activation evidence

- Product owner approval: Pending
- Accountable regulatory reviewer: Pending; must be personally named
- Reviewer role and authority: Pending
- Reviewer acceptance of responsibilities: Pending
- Framework/source snapshot approval: Pending
- Rule interpretation and golden-output approval: Pending
- Approved control-pack date: Pending
- Root status documents updated: No; Sprint 02 is not active

## Drafting evidence

Publication update, 2026-09-08: original planning commit
`60fad85b78a1559fe61b78e461894587d165a304` is retained in this branch's ancestry, and the original
local `codex/sprint-02-rules-calculation` branch remains unchanged. Review branch:
https://github.com/ragu-selva/financial-pods/tree/codex/sprint-02-planning

This planning branch is based on accepted main merge `b0cf3a9`; its only additions relative to
that baseline are the four Sprint 02 control documents. It must not be merged into main as part
of post-merge cleanup. Historical drafting evidence below remains dated 2026-08-27.

- Sprint 01 baseline: Accepted in commit `03b03ec`
- Draft branch: `codex/sprint-02-rules-calculation`
- Draft date: 2026-08-27
- Finalized reference artifacts reviewed: research blueprint, V1 specification, engineering
  playbook, prudential capital change assurance plan, regulatory content policy, and testing strategy
- Primary-source hierarchy applied: Yes; official BCBS sources take precedence over reference
  artifact prose and legacy locators
- Candidate official sources retrieved: BCBS CRE20, BCBS RBC20, and BCBS publication-status guidance
- Regulatory code or fixture changes made: No

## Known source-version issue

Some finalized reference prose cites the older CRE20.17 corporate-exposure rule. The current
consolidated Basel Framework snapshot uses revised corporate-exposure numbering, including CRE20.43
and Table 10 for the candidate unrated path. The activation pack therefore forbids copying the legacy
locator and requires a reviewer-approved current snapshot/hash before any rule becomes executable.

## Candidate golden-output review

- Classification: Pending approval
- Exposure amount: Pending approval
- Risk weight: Pending approval
- RWA: Pending approval
- Minimum-total-capital teaching amount and exclusions: Pending approval

No candidate output is accepted regulatory truth until the accountable reviewer signs off.

## Verification evidence

- Verification date: 2026-08-27
- Markdown/control-pack review: Passed; required files present and no trailing whitespace
- `git diff --check`: Passed on the staged four-file Sprint 02 draft
- `node scripts/task.mjs format-check`: Passed
- `node scripts/task.mjs lint`: Passed
- `node scripts/task.mjs typecheck`: Passed; API 5 files and finance engine 12 files
- `node scripts/task.mjs test`: Passed; Vitest 3, API pytest 5, finance-engine pytest 41
- `node scripts/task.mjs build`: Passed; web production build plus API and finance-engine packages
- `node scripts/task.mjs e2e`: Passed; 2 Chromium smoke tests
- `node scripts/task.mjs verify-artifacts`: Passed; 10 immutable artifacts verified
- Infrastructure validation: Not required; the draft changes only Markdown control files
- Existing non-failing warnings: Starlette TestClient deprecation, pytest cache creation, and
  Playwright `NO_COLOR`/`FORCE_COLOR` notices

## Risks and limitations

- The BCBS Framework is a canonical international baseline, not directly binding domestic law.
- The framework is consolidated and versioned over time; a source hash and current-version metadata
  must be pinned at activation.
- The proposed Alpha Manufacturing regulatory facts are synthetic assumptions awaiting approval.
- The candidate output excludes domestic implementation choices, capital buffers, Pillar 2,
  output-floor calculations, provisions other than zero, CRM, and all other excluded treatments.
- No personally named accountable regulatory reviewer has yet accepted responsibility.

## Deferred work

- Domestic United States, SAMA, CBUAE, and other jurisdiction overlays or comparisons
- Rated corporate, SME, specialised-lending, retail, defaulted, off-balance-sheet, provisions, CCF,
  CRM, collateral, guarantee, and netting paths
- Buffers, Pillar 2, output floor, available capital, ratios, adequacy conclusions, portfolio
  aggregation, and regulatory reporting
- API, database, UI, lesson, tutor, LLM, authentication, billing, and deployment work

## Decision

- [ ] Accepted
- [ ] Accepted with documented follow-up
- [ ] Rework required
- [x] Awaiting activation decision; implementation blocked

Reviewer/date: Pending
