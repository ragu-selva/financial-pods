# Financial Pods Current Status

## Current Date

2026-09-08, America/New_York. Inventory of the local repository at
`D:\Financial Ai studio\financial-pods`, with live GitHub branch/PR checks and fresh local verification.

Labels used throughout: **PLANNED** means documented intent without working implementation;
**IMPLEMENTED** means inspected source/configuration exists; **VERIFIED** means an observed check
passed during this inventory unless explicitly dated as historical. Prior sprint acceptance is a
recorded decision, not proof that every possible boundary case is correct.

## Current Branch

`codex/sprint-02-rules-calculation`. No upstream is configured for this branch.

Remote: `https://github.com/ragu-selva/financial-pods.git`.
Live remote heads: `main` at `2781a8ed1c514d1efd6855c425105d6c3415b345`,
`codex/sprint-01-domain-model` at `03b03ec29f699cd546414a339f7e03ce0cd9eed7`, and
`codex/sprint-00-bootstrap` at `7531b812493b58e6a20cbcaf708bd5433bfc390c`.
The current Sprint 02 branch is absent remotely.

Sprint 01 is pushed on its feature branch, but its commit is not in remote main's ancestry.
GitHub reports the two branches diverged (one commit ahead, one behind; common ancestor `7531b81`).
The current local branch inherits Sprint 01 and adds the unpublished Sprint 02 draft.
No fetch, checkout, merge, commit, or push was performed during this inventory.

## Latest Commit

`60fad85b78a1559fe61b78e461894587d165a304` — `Draft Sprint 02 activation controls`,
2026-08-27 13:44:58 -04:00. This commit adds only four Markdown files under `sprints/sprint-02/`.
It is local-only, not advertised by any remote branch.

Recent local history, newest first:

- `60fad85` — Draft Sprint 02 activation controls (2026-08-27).
- `03b03ec` — Implement accepted Sprint 01 domain model (2026-08-27): 31 files changed;
  domain package, fixture, tests, toolchain integration, ADR, and sprint/status documentation.
- `7531b81` — Bootstrap Financial Pods Sprint 00 (2026-08-17).
- `0acc6e9` — Initial commit (2026-08-17).

## Completed

- **IMPLEMENTED / VERIFIED:** Sprint 00 Next.js placeholder page and web health route; FastAPI
  typed health endpoint with validated/generated correlation IDs; application tests and builds.
- **IMPLEMENTED:** Dockerfiles, four-service Compose configuration, PostgreSQL/pgvector extension
  initialization, Redis configuration, health checks, loopback port bindings, non-root application
  containers, environment examples and secret/cache/state ignore rules. Compose configuration is
  **VERIFIED** today; full container health was verified historically on 2026-08-17, not today.
- **IMPLEMENTED / VERIFIED:** root Node task runner, Make/pnpm aliases, formatting, lint, strict
  typing, unit/property tests, browser smoke tests, Python package builds, and checksum gate for
  ten catalogued reference artifacts.
- **IMPLEMENTED:** GitHub Actions workflow. Sprint 00 PR #1 is merged and its hosted CI run #1
  succeeded; this historical result was rechecked through GitHub today.
- **IMPLEMENTED / VERIFIED:** Sprint 01 pure Python `financial_pods_finance_engine` package,
  with no third-party runtime dependencies. Includes typed entity IDs; USD currency policy;
  Decimal Money and Percentage primitives; Money addition/subtraction; institution, counterparty,
  product, facility, exposure and case models; assumption/provenance records; structured validation
  errors; fixture loading; strict schema-field checks and dictionary serialization.
- **IMPLEMENTED / VERIFIED:** `data/finbank/alpha_manufacturing_v1.json`, schema `1.0`, fixture
  `1.0.0`: FinBank lends USD 10,000,000 original principal to Alpha Manufacturing; origination and
  exposure snapshot are 2025-01-01, maturity is 2030-01-01, and outstanding principal at that snapshot
  is USD 10,000,000. Two assumptions and eight provenance entries are present. Fixture round-trip,
  normal validation and the existing 41 finance-engine tests pass.
- **IMPLEMENTED:** accepted ADR 0002, Sprint 01 control/acceptance/review pack, and root documents
  recording Sprint 01 acceptance on 2026-08-27. Fresh probes found gaps described below; existing
  acceptance records were not changed by this inventory.

## In Progress

- **PLANNED; documentation implemented:** Sprint 02 activation package exists:
  `SPRINT.md`, `FRAMEWORK_SCOPE.md`, `ACCEPTANCE_CRITERIA.md`, and `REVIEW.md`.
  All activation/completion checks remain unchecked; it explicitly says not active.
- Its proposed BCBS educational ruleset, source register, case additions, trace contract and golden
  outputs await source snapshot/hash completion, owner approval and a personally named accountable
  regulatory reviewer. Numbers in that document are candidate expectations, not calculated results
  or independently verified regulatory assertions in this inventory.
- Sprint 01 delivery is published on a feature branch. No Sprint 01 PR or PR-triggered CI run was
  returned by the GitHub queries; hosted verification for that commit remains unconfirmed.
- No partially implemented Sprint 02 production module was found.

## Not Started

- **PLANNED:** executable regulatory sources/rulesets, regulatory classification, risk weights,
  EAD, RWA, capital teaching calculations, calculation trace, reviewed golden/regulatory tests,
  domestic jurisdiction overlays and rule approval/ingestion workflows.
- **PLANNED:** domain API routes, database schema/migrations/repositories, persisted cases,
  learner state, API-to-domain integration and web-to-domain product flows.
- **PLANNED:** Golden Lesson, calculator UI, assessments, mastery, progress, analytics, grounded
  tutor, retrieval, voice/video generation, identity, billing, and production deployment.
- **PLANNED:** Growth V1 approved source packets/scripts, channel templates, at least ten public
  educational assets, publication records, CTAs and attribution. Automated publishing is deferred.
- `packages/regulatory`, `packages/tutor`, `packages/learning`, `packages/ui`, `content/`,
  `prompts/`, `skills/`, `infra/terraform`, `docs/growth`, and `docs/regulatory` contain no files.
- Sprint 03, 04 and 05 directories exist but are empty. Their roadmap descriptions are proposals.

## Uncommitted Changes

- Before this task: clean working tree; no staged changes, unstaged changes or untracked files.
- After this task: only the new untracked `STATUS.md` inventory. No production code was edited.
- **Committed but not pushed:** `60fad85`, containing the four Sprint 02 control documents.
  This is separate from uncommitted work and must not be overlooked because Git status was clean.
- **Pushed:** `03b03ec` matches the remote Sprint 01 feature branch exactly.
- Ignored local dependencies/build outputs/caches include `.venv`, `node_modules`, `.next`,
  Python `dist`, pytest/mypy/Ruff caches, Hypothesis data and Playwright test output. Existing
  checks refreshed generated files; these are not new implementation work. The final tracked
  source diff remained empty.

## Current Architecture

- `apps/web`: Next.js 16.3.1 / React 19.2.8 / TypeScript / Tailwind. Only an accessible foundation
  page at `/` and JSON `/health` are implemented; the page still displays Sprint 00.
- `apps/api`: FastAPI 0.141.1, Pydantic 2.13.4, Uvicorn 0.52.3; package version 0.1.0.
  Only business-independent `GET /health`, correlation middleware and generated OpenAPI/docs
  are present. Health reports process status, service, version and trace ID; it does not probe DB
  or Redis. No `/api/v1` product routes or finance-engine import is present.
- `packages/finance-engine`: eight Python source modules and four test modules plus project
  metadata/README. It is a standalone case model used by tests, not a connected application service.
  Other package directories are empty placeholders.
- `data/`: one versioned FinBank JSON fixture. `content/`, root `prompts/` and root `skills/`
  have no active assets. Reference-pack prompt/skill examples are immutable guidance only.
- `docs/`: two accepted ADRs, local development instructions, roadmap summary and preserved
  reference artifacts (research/specifications/playbooks/growth documents/deck/HTML prototype/ZIPs
  and extracted starter guidance). The reference HTML is not the running Next.js application.
  Planning and reference files are not evidence of implemented features.
- `tests/`: executable `integration/stack-health.mjs` plus four README files; application and
  domain tests are colocated in their owners. Regulatory and AI-evaluation directories contain
  descriptions only.
- `scripts/`: task runner, browser-server lifecycle wrapper, ten-artifact SHA-256 checker.
- `infra/`: Docker notes and PostgreSQL `CREATE EXTENSION IF NOT EXISTS vector` initialization;
  Terraform directory empty. Compose configures PostgreSQL 17 with pgvector 0.8.1, Redis 7.4.2,
  API on port 8000 and web on 3000; DB/Redis host ports 5432/6379. PostgreSQL has a named volume;
  Redis persistence is disabled. No application tables or adapters are implemented.
- CI: `.github/workflows/ci.yml` runs install, checks, builds and browser smoke tests; PostgreSQL
  and Redis are service containers. Triggers: main pushes, PRs, manual dispatch. It does not run
  the complete application Docker-stack integration probe.
- External integration actually present: GitHub repository/Actions and package/container registries
  for tooling. No runtime OpenAI/other LLM, speech, avatar, payment, social-platform or GCP provider
  integration exists. GCP is a preference for later design, not a deployed environment.
- `AGENTS.md` remains the live operating contract; `apps/web/AGENTS.md` contains generated Next.js
  guidance. Archived/nested reference contracts do not supersede the live root. Root `architecture/`,
  `prototype/` and `src/` also contain no tracked implementation files.

## Current Working Features

- **VERIFIED:** load and validate the Alpha Manufacturing fixture with `load_case_fixture`;
  inspect distinct institution/borrower/product/facility/exposure records; serialize and reconstruct
  the case with `case_to_dict` / `case_from_dict` without losing the approved fixture values.
- **VERIFIED:** ordinary USD Money operations, typed-ID and date/reference validation, schema
  rejection, and structured error reporting within the tested boundaries.
- **VERIFIED in tests:** browser renders the foundation page and web health response; API health
  and correlation-ID behavior work through FastAPI tests. Browser verification used a temporary
  server on port 3100 and shut it down afterward.
- The complete Docker stack is not currently demonstrated: Docker engine access failed. This
  inventory does not assert that localhost:3000 or localhost:8000 is currently serving.
- There is no learner-facing financial lesson or working regulatory calculator yet.

## Tests and Verification

Fresh checks on 2026-09-08, current commit `60fad85`, using Windows, Node 24.14.1,
Python 3.14.3, Git 2.47.1.windows.1, Docker CLI 29.3.1 and Compose 5.1.0:

- **VERIFIED PASS:** `node scripts/task.mjs verify` exited 0. Its component commands all passed:
  `format-check`, `lint`, `typecheck`, `test`, `build`, `e2e`, `verify-artifacts`.
- Formatting: web Prettier; API Ruff (6 files); finance-engine Ruff (13 files).
- Lint: helper JS syntax, ESLint, API and finance-engine Ruff. Types: TypeScript plus strict mypy
  (5 API files; 12 finance-engine files).
- Tests: Vitest 3, API pytest 5, finance-engine pytest 41 (49 total), including Hypothesis
  decimal serialization properties and an AST dependency-isolation check.
- Builds: Next.js production build; API and finance-engine source distributions and wheels.
- Browser: 2 Chromium tests passed (page and web health). Artifact gate: 10 checksums matched.
- **VERIFIED PASS:** `docker compose --env-file .env.example config --quiet`.
- **VERIFIED PASS:** `git diff --check` and `git diff --cached --check` on the baseline.
- **FAILED / ENVIRONMENT BLOCKED:** `node scripts/task.mjs stack-check`: Docker Linux-engine
  named pipe unavailable. `stack-verify` was deliberately not run because it starts/rebuilds services.
- Additional read-only, in-memory Python probes verified fixture round-trip and reproduced the
  precision, provenance and mutable-container failures below. No new regression test file was added.
- Historical hosted evidence: [Sprint 00 CI run #1](https://github.com/ragu-selva/financial-pods/actions/runs/32058855687)
  succeeded. The PR-filtered workflow query for Sprint 01 returned no runs; this does not establish
  the absence of every possible manual/main workflow run.

## Known Problems

- **VERIFIED correctness gap — Decimal context:** `primitives.py` uses context-sensitive
  `normalize()` and `quantize()`. With `decimal.localcontext().prec = 3`, constructing
  `Money(Decimal('1.001'), Currency('USD'))` accepts and rounds to `1.00` instead of rejecting
  excess precision; `Percentage(Decimal('12.3456'))` becomes `12.3`. The current tests miss this
  violation of the no-implicit-rounding/exactness contract. Resolve before adding regulatory math.
- **VERIFIED provenance gap:** replacing the fixture's provenance with a single entry, or with
  an entry whose field path is `does.not.exist`, succeeds. Construction checks nonempty records,
  duplicate paths and assumption references, but not complete coverage or valid case paths.
- **VERIFIED runtime immutability gap:** direct construction via `dataclasses.replace(case,
  assumptions=list(case.assumptions))` accepts a mutable list despite the tuple annotation.
  Clearing it mutates the supposedly frozen case after validation. JSON deserialization uses tuples,
  so this is specifically a direct Python construction boundary gap.
- Existing tests all pass despite these probes; accepted Sprint 01 records overstate full invariant
  coverage. Acceptance provenance identifies the reviewer by role/task, not a personal name.
- Local sandbox shell launch fails with `setup refresh had errors`; approved escalated commands
  worked for this inventory. Docker's `dockerDesktopLinuxEngine` pipe is missing, blocking live
  stack verification; no container resources were changed.
- API tests emit Starlette TestClient deprecation and Windows pytest cache warnings. Browser checks
  report slow-filesystem and `NO_COLOR`/`FORCE_COLOR` warnings. They did not fail the suite.
- Test/build tooling covers the existing environment; a fresh dependency install and installed-wheel
  runtime smoke test were not performed. Current local verification is not hosted CI evidence.
- `stack-health.mjs` hard-codes default ports, database/user and `.env.example`, so it does not honor
  documented custom `.env` overrides. Root Compose `dev`/`up` has no source-mounted hot reload.
- GitHub Actions use major-version tags; Docker images use version tags, not digest pins. Root Node
  engine range permits 22 while web requires 24; documentation recommends 24 and this audit used 24.
- Sprint 00 review still says GitHub is unconnected; that is historical/stale. Root architecture and
  structure documents list future packages as though they form the system; actual file presence
  is distinguished above. Some test/onboarding descriptions also still speak only about Sprint 00.
- Sprint 02 source metadata, approved hashes, named reviewer and approval evidence are incomplete.
  Its own review flags outdated CRE20 locators in reference prose. Official sources were not
  revalidated in this repository-inventory task; candidate regulatory claims remain PLANNED.
- Checksum automation covers ten catalogued artifacts, not the entire extracted reference tree.
  No tracked reference files were changed during this task.

## Current Sprint

Sprint 00 no longer defines the latest implemented boundary. Sprint 01 implementation exists and
its control/review records mark it accepted on 2026-08-27. `PRODUCT_SCOPE.md` explicitly states
Sprint 01 is accepted and no later sprint is active.

Sprint 02 planning has begun, but executable regulatory work has not. The current branch name does
not activate the sprint: `sprints/sprint-02/SPRINT.md` and `REVIEW.md` explicitly block implementation
pending activation decisions and accountable regulatory review. Sprint 03-05 are empty directories.
This inventory records evidence and defects without changing any acceptance/activation decision.

## Recommended Next Sprint

**PLANNED recommendation: a small Sprint 01 validation-hardening follow-up before Sprint 02 math.**

1. Add meaningful regressions and fix Decimal context dependence, complete provenance/path
   validation and immutable collection enforcement at direct construction boundaries.
2. Preserve the approved USD case and public schema; rerun the existing gates plus the new
   regressions and record concrete evidence. Reconcile Sprint 01 delivery with remote main and
   obtain hosted verification through a reviewable PR.
3. Complete Sprint 02's source snapshots, precise scope, named reviewer and approval record.

After those gates, the smallest product milestone is one reviewed, versioned corporate-exposure
calculation with a deterministic trace and golden/boundary tests under the proposed Sprint 02 pack.
Lesson UI, tutor, new jurisdictions and social-platform integrations should follow their own scope.
No hardening, sprint activation, merge or implementation was performed by this inventory.

## Important Decisions

- The live root is `D:\Financial Ai studio\financial-pods`; immutable reference artifacts and
  archive snapshots are inputs, not alternative live repositories.
- Financial values and regulatory calculations belong to deterministic typed domain code; an LLM
  must not select authoritative formulas or change results. Domain code stays independent of web,
  database, Redis and model-provider dependencies.
- Preserve USD-only currency policy `sprint-01-v1`, schema `1.0`, fixture `1.0.0`, original-versus-
  outstanding principal semantics and the explicitly approved synthetic dates. Additional currencies
  and regulatory facts require explicit versioned decisions; absent facts are not defaults.
- Exact Decimal semantics, rejection of excess precision, typed IDs, explicit dates, provenance and
  versioned serialization are intended contracts. The demonstrated bugs do not authorize weakening them.
- Regulatory rules require dated/versioned official citations, applicability and accountable review.
  Sprint 02 proposes a BCBS educational baseline, not domestic law; its approval is still pending.
- PostgreSQL is the planned system of record; pgvector is only for approved retrieval; Redis is
  ephemeral. Their container presence does not imply application persistence/retrieval is implemented.
- Local orchestration remains Docker Compose. GCP is preferred but not locked or provisioned;
  production design must be captured in a later ADR.
- Initial release remains one focused Golden Lesson plus Growth V1 using the same reviewed knowledge.
  At least ten public assets are planned; manual human-approved publishing is sufficient for V1.
- No secrets in source. Sprint scope and evidence gates remain authoritative; a directory or branch
  name is not proof of implementation or authorization.
