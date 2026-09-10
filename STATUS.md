# Financial Pods Current Status

## Current Date

2026-09-10, America/New_York. Internal-prototype activation governance snapshot.

- Sprint 00: **ACCEPTED**.
- Sprint 01: **ACCEPTED**.
- Sprint 01 hardening: **ACCEPTED AND MERGED**; PR #2 **MERGED**.
- Sprint 02: **ACTIVE** on the activation branch. Implementation: **NOT YET STARTED**.

**IMPLEMENTED** = present software; **VERIFIED** = observed passing check; **PLANNED** = absent software.
**BLOCKED** = unmet execution gate. Human-approved expectations are not runtime-verified results.

## Current Branch

codex/sprint-02-activation, created from fetched origin/main at
5fcfc5a42fc8cb3fc0a8bf53a8659fd60fa6d931 (merged PR #3).
Activation PR: **NOT YET CREATED**. No automatic merge.
Main is not yet activated by this branch. Implementation waits for activation PR review and merge.

## Latest Commit

Base main: 5fcfc5a42fc8cb3fc0a8bf53a8659fd60fa6d931.
PR #2 merge b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183 remains in ancestry.
Original Sprint 01 03b03ec and hardening a71d639 / 46a723b remain preserved.

Published planning commit: 79b33dbb1f069a89fc6d87336a23268adea08589, unchanged, on
codex/sprint-02-planning. Local codex/sprint-02-rules-calculation remains at
60fad85b78a1559fe61b78e461894587d165a304. No history rewritten or wholesale planning merge.
The activation publication commit is the HEAD containing this status; see the activation PR.

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
  during Sprint 01 hardening, no Sprint 02 files were imported; no immutable reference artifacts altered.

- **APPROVED GOVERNANCE, NOT SOFTWARE:** Ragunath Selvaraj, Project Owner / Internal Regulatory
  Reviewer, approved the narrow US/FRB 2025-01-01 sources and synthetic Golden Case for the internal
  prototype. This is not independent legal certification or production-bank sign-off.
- **IMPLEMENTED artifacts / VERIFIED integrity:** Separate approval envelope over unchanged v0.4
  source manifest; 71 unchanged raw captures, six approved rule scopes, eight resolved dependencies,
  zero required unresolved, four not-required and two future groups. Exact-date approval only.
- **APPROVED EXPECTATIONS:** CORPORATE; EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE USD 10m;
  weight 1.00; RWA USD 10m; only baseline_total_capital_equivalent USD 800k at 0.08.
  Explicit synthetic zero adjustments/allowance and negative screens accepted, not GAAP/CECL certification.
- **ACCEPTED:** ADR 0004 generic engine -> registry -> jurisdiction provider, U.S. first.
  Source resolver included unchanged for evidence resolution only. No classifier/calculator implemented.

## In Progress

Activation governance/evidence PR preparation and verification.
The human/source/Golden prerequisites are complete for the internal prototype.
PR review and merge remain required before production implementation.

## Not Started

All items below are **PLANNED**, not implemented by this activation task:

- Basel exposure classification, risk weights, EAD, RWA, CET1, capital ratios, and regulatory rulesets.
- Regulatory source ingestion, approved retrieval indexes, or jurisdiction adapters.
- Golden Lesson UI, calculator experience, assessments, mastery, learner progress, AI tutor.
- Authentication, billing, product database persistence, and API business routes.
- Content/video generation or social publishing integrations/assets.
- Production Terraform/deployment. GCP is the owner's preference, not a locked or deployed architecture.
- Later packages/content directories remain placeholders, not working features.

Sprint 02 engine implementation is the next approved narrow milestone after activation PR merge.
This PR contains governance/evidence/tests only; no successful runtime regulatory result exists.

## Uncommitted Changes

This activation task publishes only approved Sprint 02 control/evidence artifacts, the resolver skill,
ADR, artifact tests, CI evidence checks and living documentation. No unrelated local changes found.
Planning commit 79b33db is already pushed unchanged; the original planning branch/history is preserved.
Generated caches and build outputs remain ignored. No secrets or real environment files are included.
Only the scoped activation changes are prepared for publication; final clean-tree verification follows commit.

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

- **ACCEPTED DESIGN / NOT IMPLEMENTED:** Generic regulatory engine, ruleset registry and jurisdiction
  provider abstraction. First provider: USStandardizedRuleset for the approved ordinary corporate
  path only. BCBS is conceptual, never a U.S. fallback. Other providers/classes and Regxify extraction
  remain future scope. The source approval package is documentary, not executable software.

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

**Fresh activation verification, 2026-09-10:**

- Source/hash + planning/activation checks: **35/35 PASS**; all 71 raw hashes and unchanged snapshots.
- Full repository verification: **PASS / exit 0**. Formatting/lint, TypeScript/mypy, 130 finance-engine tests including properties, 5 API tests, 3 web tests, 2 Playwright tests, Next.js and Python builds, 10 immutable artifact hashes.
- Docker availability rechecked: **BLOCKED**, missing Docker Desktop Linux engine pipe.
  No local stack-runtime pass is claimed.
- Hosted activation CI: **NOT YET RUN** (PR not yet created).

**Retained historical acceptance evidence (not a fresh activation run):**

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
- **BLOCKED from implementation:** Sprint 02 implementation waits for activation PR review and merge; internal-prototype human/source approval is complete.
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
  evidence, not current authorization. STATUS.md, Sprint 02 SPRINT.md and ACTIVATION_RECORD.json govern this snapshot.

- Approved source eligibility is restricted to 2025-01-01; unknown legal endpoints are not open-ended.
  Different dates or changed material facts require review. No general CECL/PPP/market-risk corpus.
- Runtime schemas, canonical input serialization, classifier/provider/trace and all regulatory runtime
  tests remain unimplemented. Approval tests cannot establish legal truth or verify a calculator.

## Current Sprint

Sprint 00: **ACCEPTED**. Sprint 01: **ACCEPTED**. Sprint 01 hardening: **ACCEPTED AND MERGED**.
Sprint 02: **ACTIVE** on the activation branch. Implementation: **NOT YET STARTED**.
The activation PR is governance/evidence only; main execution waits for human review and merge.

## Recommended Next Sprint

Review and merge the activation PR. Then begin the separate
codex/sprint-02-us-corporate-engine milestone: generic contracts/registry, one U.S. corporate
provider, typed exposure amount, weight/RWA, sole educational output, trace and runtime tests.
Do not start that implementation in this task. Restore Docker separately and rerun stack verification.

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
- No automatic PR merge. Activation is internal-prototype governance only; implementation waits for merge.

- Preserve original source evidence and planning snapshots. Approval is a separate pinned package.
- R-1888 remains PROPOSED / executable=false; no proposal/alias can replace 2025 authority.
- The USD 800k output is educational, not allocated/economic capital, a complete regulatory
  requirement, institution-specific requirement or capital adequacy conclusion.
- The personally confirmed reviewer is Ragunath Selvaraj; AI transcribes but cannot sign that approval.
