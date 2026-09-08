# Financial Pods Current Status

## Current Date

2026-09-08, America/New_York. Documentation-only post-merge cleanup snapshot.

- Sprint 00: **ACCEPTED**.
- Sprint 01: **ACCEPTED**.
- Sprint 01 hardening: **ACCEPTED AND MERGED**.
- PR #2: **MERGED** on 2026-09-08.
- Sprint 02: **PLANNING ONLY — NOT ACTIVE**.

Labels: **IMPLEMENTED** means present in inspected code; **VERIFIED** means an observed passing
check; **PLANNED** means not implemented or authorized here; **BLOCKED** identifies an unmet gate.
Historical acceptance is preserved separately from fresh verification.

## Current Branch

Local `main` was synchronized with `origin/main` at merge commit `b0cf3a9`.
This documentation cleanup is published for review on `codex/post-merge-status-cleanup`, based on
that merged main baseline. No history was rewritten or squashed.
Repository: https://github.com/ragu-selva/financial-pods

[PR #2 — Sprint 01: integrate and harden financial domain model](https://github.com/ragu-selva/financial-pods/pull/2)
was merged into `main` on 2026-09-08 by the project owner.

Main retains the original Sprint 01 implementation and hardening commits through merge history.
The separate Sprint 02 planning branch is not merged into main.

## Latest Commit

Confirmed main merge commit:
`b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183` — merge PR #2, 2026-09-08 12:40:59 -04:00.

Included implementation commit:
`a71d6391daafcb5a9df4f4ce3e2fd19ed1b7274e` —
`Harden Sprint 01 decimal, provenance, and immutable domain contracts`.

Relevant history:

- `2281209` — integrates accepted Sprint 01 onto main's history.
- `03b03ec29f699cd546414a339f7e03ce0cd9eed7` — original accepted Sprint 01 implementation,
  retained unchanged and already published on its original feature branch.
- `46a723b` — hardening status/review evidence; included in PR #2 and the main merge.
- This post-merge cleanup changes documentation only; its branch HEAD identifies the publication commit.

Preserved separately: local `codex/sprint-02-rules-calculation` remains at
`60fad85b78a1559fe61b78e461894587d165a304` (Sprint 02 draft controls).
It remains absent from main ancestry. Published review branch `codex/sprint-02-planning` at
`f90ee1e` retains 60fad85 in its ancestry and contains four planning-only Sprint 02 Markdown files
relative to merged main. Original local `codex/sprint-02-rules-calculation` remains unchanged.

## Completed

- **IMPLEMENTED / VERIFIED:** Original Sprint 00 web/API bootstrap, health endpoints, task runner,
  CI workflow, application tests/builds, and container/Compose definitions.
- **IMPLEMENTED / VERIFIED:** Original Sprint 01 pure Python finance-engine package: typed IDs,
  Currency/Money/Percentage, institution/counterparty/product/facility/exposure types, assumptions,
  provenance, strict schema 1.0 serialization, and approved fixture loader.
- **IMPLEMENTED / VERIFIED:** Versioned synthetic FinBank/Alpha Manufacturing USD 10 million fixture.
  Original principal and outstanding principal are separate concepts; no regulatory EAD meaning.
  Fixture bytes, schema 1.0, fixture 1.0.0, USD policy, dates, and eight provenance entries unchanged.
- **IMPLEMENTED / VERIFIED:** Exact Decimal coefficient/exponent handling replaces context-sensitive
  normalize/quantize. Supported effective precision is enforced without rounding; existing Money
  arithmetic and serialization remain deterministic under hostile Decimal contexts.
- **IMPLEMENTED / VERIFIED:** Explicit supported case-data provenance paths and eight required
  case-fact paths; malformed/nonexistent paths, incomplete coverage, duplicates, and invalid
  assumption references rejected with stable domain errors.
- **IMPLEMENTED / VERIFIED:** Exact-tuple enforcement for direct assumptions/provenance construction.
  JSON arrays still become detached tuples of immutable domain objects.
- **IMPLEMENTED / VERIFIED:** New hardening control pack, ADR 0003, 89 regression/property tests,
  and living-document status updates. Original historical Sprint 00/01 review records unchanged.
- **VERIFIED:** Original Sprint 01 commit ancestry preserved; Sprint 02 branch remains at 60fad85;
  no Sprint 02 files imported, no immutable reference artifacts altered.

## In Progress

- Documentation-only post-merge synchronization of acceptance and publication records.
- Architecture/regulatory review of the separately published Sprint 02 planning pack; no activation
  or regulatory implementation has been authorized.
- Sprint 01 hardening is accepted and merged; no acceptance or merge action remains for PR #2.

## Not Started

All items below are **PLANNED**, not implemented or authorized by this hardening task:

- Basel exposure classification, risk weights, EAD, RWA, CET1, capital ratios, and regulatory rulesets.
- Regulatory source ingestion, approved retrieval indexes, or jurisdiction adapters.
- Golden Lesson UI, calculator experience, assessments, mastery, learner progress, AI tutor.
- Authentication, billing, product database persistence, and API business routes.
- Content/video generation or social publishing integrations/assets.
- Production Terraform/deployment. GCP is the owner's preference, not a locked or deployed architecture.
- Later packages/content directories remain placeholders, not working features.

Sprint 02 draft activation documents exist only on the preserved planning branch. Their existence
is not approval of framework selection, sources, reviewer provenance, or implementation.

## Uncommitted Changes

Sprint 01 hardening code and its evidence are committed and merged into main through PR #2.
This follow-up publishes only documentation from the post-merge cleanup branch. No unrelated local
production edits were found or included; no production files changed during cleanup.

**Preserved and now published:** Sprint 02 planning commit 60fad85 is reachable from remote
`codex/sprint-02-planning`; the original local branch still points to 60fad85. No unpublished
production changes were introduced. The old inventory remains on `codex/current-status-inventory`
(`73860e1`). No branch was deleted.

Planning branch: https://github.com/ragu-selva/financial-pods/tree/codex/sprint-02-planning

Generated caches/build outputs remain ignored. No secrets or real environment files are committed.

## Current Architecture

- **IMPLEMENTED:** Next.js 16.3.1 / React 19.2.8 / strict TypeScript / Tailwind web bootstrap under
  apps/web, with placeholder page and web health route. No domain UI.
- **IMPLEMENTED:** FastAPI 0.141.1 / Pydantic 2.13.4 API under apps/api, with typed health response
  and correlation IDs. No business routes, persistence adapter, or product authentication.
- **IMPLEMENTED:** Framework-independent Python finance-engine under packages/finance-engine,
  eight source modules, no runtime third-party dependencies. Decimal/domain/serialization code
  does not import web frameworks, databases, Redis, or LLM providers.
- **IMPLEMENTED configuration:** Docker Compose web/API plus PostgreSQL 17 with pgvector 0.8.1
  and Redis 7.4.2. PostgreSQL named volume; Redis persistence off; localhost development endpoints.
  **Non-blocking known limitation:** Docker Desktop Linux engine was unavailable during hardening
  verification; local full-stack runtime was not revalidated by this documentation-only cleanup.
- **IMPLEMENTED CI:** .github/workflows/ci.yml runs on main pushes, pull requests, and manual
  dispatch; Ubuntu/Node 24/Python 3.12, PostgreSQL/Redis services, pgvector enable/check, Compose
  validation, artifact checks, formatting/lint/types/tests/builds, and Chromium E2E.
- **PLANNED:** PostgreSQL product persistence, pgvector retrieval, Redis product caching/queues,
  other domain packages, cloud hosting, and external AI/video/social-provider integrations.
  No active provider integration or production deployment is present.

## Current Working Features

- Load the approved synthetic fixture, validate the typed case, serialize it, and restore it.
- Perform exact Money addition/subtraction and Percentage field-bound checks without ambient
  Decimal precision or rounding changing accepted values.
- Reject unsupported precision, currencies/IDs, date/reference inconsistencies, incomplete or
  invalid structural provenance, and mutable direct-constructor collection inputs.
- Demonstrate bootstrap web rendering and health contracts through automated tests.
- Build the web application and both Python distributions.

There is no working Golden Lesson, regulatory capital calculator, AI tutor, or social-publishing
feature. A running Docker demonstration was not available during this task.

## Tests and Verification

**VERIFIED locally, 2026-09-08:**

Post-merge documentation cleanup reran `node scripts/task.mjs verify` to exit 0 on the accepted
main baseline with documentation edits only. Protected historical reviews, reference artifacts,
production code, fixtures, dependencies, and infrastructure are unchanged from b0cf3a9.

- `node scripts/task.mjs verify` — exit 0.
- Formatting: Prettier/web and Ruff/API/finance engine pass.
- Lint: JavaScript syntax, ESLint, Ruff pass.
- TypeScript and strict mypy pass (5 API files, 13 finance-engine files).
- Python: 130 finance-engine tests (41 original + 89 hardening) and 5 API tests pass.
- Web: 3 unit tests and 2 Playwright Chromium smoke tests pass.
- Builds: Next.js production build, API sdist/wheel, finance-engine sdist/wheel pass.
- Artifact checks: all 10 catalogued immutable reference hashes pass.
- `.venv/Scripts/python.exe -m pytest -c packages/finance-engine/pyproject.toml
  packages/finance-engine/tests/test_hardening.py --hypothesis-show-statistics -q` — 89 pass.
  Three new properties each produced 100 passing examples, zero failing examples.
- `docker compose --env-file .env.example config --quiet` — pass (configuration only).
- `git diff --check` and protected-history/content checks pass.

Environment: Windows, Node 24.14.1, Python 3.14.3, pytest 9.1.1, Hypothesis 6.165.10.
Tests cover all eight rounding modes, traps on/off, low precision, tight exponent limits, clamp,
unchanged caller flags, large coefficients, excess precision, fixture round trips, provenance
coverage/path policy, and runtime immutability.

**Hosted CI:** [run 34247265131](https://github.com/ragu-selva/financial-pods/actions/runs/34247265131)
for implementation commit a71d639 is **VERIFIED / PASSED** (Ubuntu, Node 24, Python 3.12).
All quality gates, pgvector setup/check, service health initialization, builds, and browser smoke
tests passed. Hosted service checks are not a substitute for the blocked local four-service stack.
The final PR #2 head `46a723b` also passed
[run 34247638871](https://github.com/ragu-selva/financial-pods/actions/runs/34247638871).
Both hosted runs are retained acceptance evidence. Cleanup PR checks are separate; no unobserved
merge/push CI result is implied by these historical passing runs.

**Non-blocking known local-runtime limitation (recorded during hardening):** `docker info` and
`node scripts/task.mjs stack-check` failed:
`failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine;
open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.`
No stack-verify success is claimed. Containers/infrastructure were not changed. This limitation
does not reopen or block the accepted and merged Sprint 01 baseline.

## Known Problems

- **Non-blocking known limitation:** Local Docker full-stack runtime was unavailable during
  hardening verification. Recheck after Docker Desktop's Linux engine is running.
- **BLOCKED from implementation:** Sprint 02 still requires separate explicit activation approvals.
  PR #2 review, acceptance, and merge are complete.
- Original Decimal/provenance/mutable-list defects are **FIXED / VERIFIED** by the hardening suite.
  This does not certify every future financial rule or arbitrary input boundary.
- Existing non-failing warnings: Starlette/httpx TestClient deprecation, Windows pytest cache
  WinError 183, Next.js slow-filesystem warning, FORCE_COLOR/NO_COLOR notices.
- Existing infrastructure/tooling limitations are unchanged: stack checker assumes default ports
  and .env.example; root Node engine range is broader than the web package's Node 24 requirement;
  CI does not run the complete four-container local stack-health script.
- Provenance checks establish structure and valid assumption links, not truth of source claims.
  Human verification remains necessary. Unused approved assumptions are allowed.
- Sprint 01 remains USD-only; no new magnitude cap, financial rounding policy, or regulatory meaning
  has been invented. Inputs/results must remain within available runtime resources.
- Some historical onboarding/review documents describe an earlier state. They are historical
  evidence, not current authorization. STATUS.md and the hardening control pack govern this snapshot.

## Current Sprint

Sprint 00: **ACCEPTED**. Sprint 01: **ACCEPTED**. Sprint 01 hardening: **ACCEPTED AND MERGED**
through PR #2 at `b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183` on 2026-09-08.
No implementation sprint is active. Sprint 02 is **PLANNING ONLY — NOT ACTIVE**.

## Recommended Next Sprint

The verified Sprint 01 baseline is accepted and on main. Restore Docker and rerun stack verification
when available as a non-blocking local-environment follow-up.

Review the four documents on `codex/sprint-02-planning`. Sprint 02 must not begin until its framework,
jurisdiction, regulatory sources, calculation scope, golden outputs, and regulatory review process
are explicitly approved by the project owner and accountable regulatory reviewer. The preserved
60fad85 draft and its publication are not implementation approval.
Do not begin regulatory calculations merely because the domain hardening tests pass.

## Important Decisions

- Preserve original commits 03b03ec and 60fad85 and the original Sprint 02 branch.
- Never merge Sprint 02 planning/implementation opportunistically with Sprint 01 hardening.
- Synthetic data only; original USD 10 million means facility original principal, not regulatory EAD.
- Domain calculations remain deterministic, typed, tested, and independent of LLMs/frameworks/data stores.
- ADR 0003: exact Decimal tuples, no implicit rounding, fixed Money scale, canonical Percentage,
  eight required case-fact provenance paths, strict runtime tuple rejection; JSON schema unchanged.
- Structural provenance is not regulatory provenance or proof that a source supports a value.
- Reference artifacts and historical reviews remain immutable historical inputs.
- V1 still comprises Product V1 Golden Lesson plus Growth V1 social publishing; both remain later
  work. Manual human-approved publishing is sufficient for that planned release.
- GCP preference is provisional; no AWS/GCP production deployment is locked by this task.
- No automatic PR merge. No Sprint 02 activation in this task.
