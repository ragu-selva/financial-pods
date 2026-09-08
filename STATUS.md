# Financial Pods Current Status

## Current Date

2026-09-08, America/New_York. Sprint 01 integration/hardening snapshot.

Labels: **IMPLEMENTED** means present in inspected code; **VERIFIED** means an observed passing
check; **PLANNED** means not implemented or authorized here; **BLOCKED** identifies an unmet gate.
Historical acceptance is preserved separately from fresh verification.

## Current Branch

`codex/sprint-01-hardening`, tracking `origin/codex/sprint-01-hardening`.
Repository: https://github.com/ragu-selva/financial-pods

[PR #2 — Sprint 01: integrate and harden financial domain model](https://github.com/ragu-selva/financial-pods/pull/2)
targets `main`. Open, non-draft, no merge conflicts observed. Not merged; no automatic merge requested.

The branch was created from refreshed origin/main at
`2781a8ed1c514d1efd6855c425105d6c3415b345`.
It retains the original Sprint 01 commit through a merge, not a squash or replacement.
Main is unchanged by this task.

## Latest Commit

Latest implementation commit:
`a71d6391daafcb5a9df4f4ce3e2fd19ed1b7274e` —
`Harden Sprint 01 decimal, provenance, and immutable domain contracts`.

Relevant history:

- `2281209` — integrates accepted Sprint 01 onto main's history.
- `03b03ec29f699cd546414a339f7e03ce0cd9eed7` — original accepted Sprint 01 implementation,
  retained unchanged and already published on its original feature branch.
- Documentation-only publication of this snapshot/review evidence follows the implementation
  commit; the branch HEAD identifies that publication commit.

Preserved separately: local `codex/sprint-02-rules-calculation` remains at
`60fad85b78a1559fe61b78e461894587d165a304` (Sprint 02 draft controls).
It is not an ancestor of the hardening branch and its Sprint 02 files are absent from this PR.

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

- Accountable reviewer acceptance and manual merge decision for PR #2.
- Hosted GitHub Actions verification passed for the implementation commit; see the evidence below.
- The Sprint 01 hardening implementation is complete. No Sprint 02 implementation is in progress.

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

This task's hardening code is committed and pushed on the PR branch. STATUS.md and the hardening
review/control evidence are published in a documentation-only follow-up commit. No unrelated local
production edits were found or included.

**Local work not pushed:** Sprint 02 planning commit 60fad85 remains on the original local branch;
it was deliberately not published or merged by this task. The old current-state snapshot remains
available on `codex/current-status-inventory` (`73860e1`). No branch was deleted.

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
  **BLOCKED runtime:** Docker Desktop Linux engine unavailable during this verification.
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
Subsequent documentation-only commits trigger fresh PR checks; consult the PR for the latest run.

**BLOCKED local stack:** `docker info` and `node scripts/task.mjs stack-check` fail:
`failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine;
open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.`
No stack-verify success is claimed. Containers/infrastructure were not changed.

## Known Problems

- **BLOCKED:** Local Docker daemon unavailable; full four-service local stack remains unverified
  in this task. Recheck after Docker Desktop's Linux engine is running.
- **BLOCKED pending governance:** PR review/acceptance/manual merge; separate Sprint 02 activation.
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

**Sprint 01 Integration and Hardening** is the current authorized boundary.
The original Sprint 01 is historically accepted; its three discovered correctness gaps have been
fixed and locally verified. The hardening PR awaits review and acceptance. Sprint 00 is no longer
the sole implementation boundary. Sprint 02 remains **PLANNED / NOT ACTIVE**.

## Recommended Next Sprint

First review and accept PR #2, complete the manual merge decision, and establish the verified
Sprint 01 baseline on main. Restore Docker and rerun stack verification when available.

Then consider Sprint 02 activation only through a separately approved control pack covering one
framework/jurisdiction, exact sources/versions/applicability, accountable reviewer, and acceptance
criteria. Preserve and review the draft 60fad85 planning branch rather than treating it as approval.
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
