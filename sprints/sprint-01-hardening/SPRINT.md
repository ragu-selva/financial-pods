# Sprint 01 — Integration and Hardening

Status: Accepted and merged through PR #2 on 2026-09-08 at
`b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183`. No later sprint is activated.

## Goal and boundary

Establish a trustworthy Sprint 01 baseline on current origin/main. Preserve accepted commit
03b03ec through a history-preserving merge. Preserve commit 60fad85 and the local
codex/sprint-02-rules-calculation branch without importing its planning files.

Fix only ambient Decimal context dependence, structural case-data provenance validation, and
mutable collections accepted by direct domain construction. Add regression/property tests and
record fresh local and hosted verification evidence. Historical sprint reviews remain unchanged.

## Explicit exclusions

No regulatory classification, risk weights, EAD, RWA, CET1, capital ratios, regulatory rulesets or
source ingestion, lesson UI, tutor, content/video generation, persistence, or API business routes.
Sprint 02 remains planning only and is not activated by this work.

## Stop condition

Completed: the project owner accepted and merged PR #2. The original implementation stop condition
below is retained as historical scope; it is not an outstanding merge or acceptance task.

Push codex/sprint-01-hardening and create a review-ready PR targeting main. Record the PR and CI
status in STATUS.md. Do not merge automatically or begin Sprint 02.
