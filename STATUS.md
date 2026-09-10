# Financial Pods Current Status

## Current Date

2026-09-10, America/New_York. Sprint 02 post-merge acceptance snapshot.

Sprint 00: ACCEPTED. Sprint 01: ACCEPTED. Sprint 01 hardening: ACCEPTED AND MERGED.
PR #2: MERGED. Sprint 02: ACCEPTED AND MERGED. Activation PR #4 and implementation PR #5: MERGED.
U.S. corporate regulatory engine: IMPLEMENTED AND VERIFIED. Sprint 03: NOT ACTIVE / NOT STARTED.
IMPLEMENTED means present software; VERIFIED means an observed passing check; PLANNED means
not implemented; BLOCKED names a concrete unmet prerequisite. Tests are not human acceptance.

## Current Branch

Local main was fast-forwarded to origin/main at 979dda66a3cc3424d1bf244680ef719a879680e1.
Current cleanup branch: codex/sprint-02-post-merge-cleanup, created from that synchronized main.
Implementation PR [#5](https://github.com/ragu-selva/financial-pods/pull/5) is MERGED.
The cleanup is a separate documentation-only PR; no automatic merge or Sprint 03 work.

## Latest Commit

Accepted main merge: 979dda66a3cc3424d1bf244680ef719a879680e1 (PR #5), merged 2026-09-10
at 21:00:17 UTC / 17:00:17 America/New_York. The owner confirmed review and acceptance.
Activation merge: a89eeb60727c5f615514f75ecc27f57f19ec23cf (PR #4).
Implementation 0f386d2f4d880a0cfb1fd4ab8eb6283b47634d65 and publication
2fa438062977e15651ca4ad79d74795df820edec remain unchanged in main history.
See the cleanup branch head for the documentation-only publication commit.
Accepted Sprint 01/hardening history, PR #2 merge b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183,
and cleanup PR #3 remain in ancestry. Original 03b03ec and 60fad85 are preserved.
codex/sprint-02-planning remains separately published at 79b33dbb1f069a89fc6d87336a23268adea08589.

## Completed

- IMPLEMENTED / VERIFIED: Sprint 00 web/API bootstrap, health contracts, CI/task runner,
  container definitions, application tests and builds.
- IMPLEMENTED / VERIFIED: Accepted Sprint 01 immutable domain model, typed IDs, USD Money/
  Percentage, assumptions/provenance, strict serialization and original synthetic fixture.
- IMPLEMENTED / VERIFIED: Sprint 01 hardening for context-independent exact decimals, supported/
  required provenance paths, duplicate/reference checks and runtime tuple immutability.
- APPROVED / PRESERVED: Internal-prototype source/Golden approval by Ragunath Selvaraj,
  accepted ADR 0004, six rule scopes, eight resolved dependencies, 71 unchanged source captures.
  Four dependencies remain not required; two groups remain deferred. No required evidence gap.
- IMPLEMENTED / VERIFIED: Generic immutable regulatory contracts, exact-version registry,
  orchestration, one U.S. provider, classification, treatment, typed exposure measure, RWA,
  sole educational output, ordered trace, canonical serialization and stable typed failures.
- ACCEPTED AND MERGED / IMPLEMENTED AND VERIFIED: exact ruleset
  US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1, US/FRB standardized, as-of 2025-01-01.
- VERIFIED AT RUNTIME after merge: CORPORATE; EXPOSURE_AMOUNT /
  US_STANDARDIZED_CARRYING_VALUE USD 10,000,000.00; risk weight 1.00;
  RWA USD 10,000,000.00; baseline_total_capital_equivalent USD 800,000.00 at 0.08.
  The result contains a 12-step immutable, source-linked calculation trace.
- IMPLEMENTED / VERIFIED: Different-name/IDs invariance, USD 5m -> USD 5m RWA/USD 400k teaching,
  hostile Decimal contexts, all required fields/exclusions, source/proposal tampering and direct
  provider safeguards. Original accepted fixture and source/human approval artifacts unchanged.

## In Progress

Documentation-only post-merge cleanup and its separate review PR.
Sprint 02 implementation review, acceptance, merge and hosted CI are complete.
No Sprint 03 implementation is in progress.

## Not Started

PLANNED: Other rulesets/jurisdictions/classes, EAD/CCF/IRB/ERBA, CRM, mortgage/default/bank/
sovereign treatments, portfolio aggregation, actual bank capital adequacy, CET1/Tier 1 teaching.
PLANNED: Golden Lesson UI, business API routes, persistence, assessments/progress, tutor,
authentication/billing, content/video/social publishing, regulatory monitoring and deployment.
GCP remains a preference, not a locked or deployed production architecture.

## Uncommitted Changes

This cleanup changes only STATUS.md, ROADMAP.md and sprints/sprint-02/REVIEW.md.
No production code, tests, source evidence, approved Golden Case, reviewer evidence or infrastructure
changes. No unrelated local changes were found. Generated outputs remain ignored; publication
checks verify the committed/pushed branch and clean working tree. All original branches/history remain.

## Current Architecture

- IMPLEMENTED: Next.js/React/strict TypeScript web bootstrap; no domain UI.
- IMPLEMENTED: FastAPI/Pydantic health API; no product/business routes.
- IMPLEMENTED: Pure Python finance-engine domain package, plus eight regulatory modules under
  src/financial_pods_finance_engine/regulatory. No runtime third-party dependencies.
- IMPLEMENTED: Local source/fixture adapter -> immutable facts -> registry/orchestration ->
  USStandardizedRuleset -> classified treatment/EXPOSURE_AMOUNT/weight/RWA/education/trace.
  Source loading is outside calculation; no calculation network, clock, random, DB, Redis or LLM.
- IMPLEMENTED configuration: Compose web/API, PostgreSQL 17/pgvector 0.8.1 and Redis 7.4.2.
  BLOCKED runtime: Docker Desktop Linux engine pipe unavailable locally.
- IMPLEMENTED CI: .github/workflows/ci.yml checks formats/lint/types/tests/builds, source/
  activation evidence, reference artifacts, service setup/pgvector and Chromium E2E.
- PLANNED: Product DB persistence/retrieval/cache/queues, other packages and external providers.
  The regulatory evidence is repository-local; packages/regulatory remains a placeholder.

## Current Working Features

Load/reconstruct the unchanged Sprint 01 case and perform its exact primitive operations.
Calculate the approved dated ordinary U.S. corporate path in Python with twelve immutable trace
steps and citations. Change permitted identity metadata or consistently vary the ordinary loan
amount without changing orchestration. Reject unsupported or unverified paths with typed failures.
Bootstrap web/health endpoints work in tests; no Golden Lesson or calculator UI exists yet.
See packages/finance-engine/README.md for a runnable local calculation example.

## Tests and Verification

Post-merge local verification, 2026-09-10, against accepted main 979dda6:

- node scripts/task.mjs verify: PASS / exit 0.
- Formatting, JavaScript/ESLint/Ruff lint, TypeScript and strict mypy: PASS.
- Python finance engine: 429 PASS (130 preserved baseline + 299 regulatory tests).
- Python API: 5 PASS. Web unit: 3 PASS. Chromium E2E: 2 PASS.
- Next.js production build and both Python sdist/wheel builds: PASS.
- Immutable reference artifacts: all 10 hashes PASS.
- Source/activation/planning checks: 35 PASS; all 71 raw hashes and approved pins unchanged.
- Retained implementation property evidence: 50 generated examples PASS, zero failures;
  1 test passed / 298 deselected. The full property/regression suite also reran after merge.
- git diff --check: PASS; protected fixture, source and historical paths unchanged.
- Docker Compose configuration: PASS; Docker runtime: BLOCKED, no stack-runtime pass.
- Hosted implementation CI: VERIFIED / PASSED, [run 34515138968](https://github.com/ragu-selva/financial-pods/actions/runs/34515138968),
  status completed / conclusion success for PR #5 head 2fa438062977e15651ca4ad79d74795df820edec.
  Cleanup-PR CI is a separate run; that pass is not assumed.

Retained historical acceptance evidence: Sprint 01/hardening 130 finance tests, 5 API, 3 web,
2 browser tests and full gates passed on 2026-09-08. Hosted hardening runs
[34247265131](https://github.com/ragu-selva/financial-pods/actions/runs/34247265131) and
[34247638871](https://github.com/ragu-selva/financial-pods/actions/runs/34247638871) passed.
Activation recorded 35 source/approval checks and all 71 raw captures before PR #4 merge.
These historical runs are not the implementation branch's hosted CI result.

## Known Problems

- Non-blocking local runtime limitation: docker info failed to connect to the Docker API at
  npipe:////./pipe/dockerDesktopLinuxEngine; open //./pipe/dockerDesktopLinuxEngine:
  The system cannot find the file specified. No Docker runtime pass claimed.
- Exact approved 2025-01-01 only; no general historical replay or current alias.
  R-1888 remains PROPOSED / non-executable; no regulatory coverage expansion.
- Synthetic zero-adjustment/zero-allowance assumptions are not real-bank GAAP/CECL certification.
  Different material assumptions or positive excluded facts need separate review; no fallback.
- Fractional-cent teaching results fail with ROUNDING_POLICY_UNDEFINED. No rounding policy or
  magnitude cap invented. Runtime resources bound practical input sizes.
- Provenance is traceability, not truth verification or submitter authentication.
- Existing non-failing warnings: Starlette/httpx TestClient deprecation, Windows pytest cache
  WinError 183, Next.js slow filesystem, FORCE_COLOR/NO_COLOR notices.
- Historical approval/planning and pre-merge implementation records retain prior-time wording.
  ACTIVATION_RECORD.json and IMPLEMENTATION_RECORD.json are unchanged snapshots, not current
  delivery status. This STATUS.md and the post-merge section in REVIEW.md supersede their
  pending-review/acceptance labels and earlier control-document execution labels.
- No production-bank, legal, accounting or final implementation acceptance is implied by tests.

## Current Sprint

Sprint 02: ACCEPTED AND MERGED through PR #5 at 979dda6; activation PR #4 also merged.
The approved U.S. corporate engine is IMPLEMENTED AND VERIFIED, with hosted CI passed.
Sprint 00/01/hardening remain accepted. Sprint 03 is NOT ACTIVE / NOT STARTED.

## Recommended Next Sprint

First agree and approve a bounded Sprint 03 Golden Lesson integration control pack and acceptance
criteria. Recommended first vertical slice: present the unchanged approved case facts, exact engine
result, educational warnings and source-linked 12-step trace through a thin application/API boundary
and a read-only learner screen. Reuse the accepted engine; do not recalculate in the browser or
broaden rulesets, dates or exposure classes. Tutor, persistence and wider lesson features need scope approval.
This is a recommendation only: no Sprint 03 files or implementation were created here.
Restore Docker Desktop separately and rerun node scripts/task.mjs stack-verify; the current limitation
is non-blocking for accepted Sprint 02 and this documentation-only cleanup.

## Important Decisions

- Preserve all accepted history and separate Sprint 02 planning/activation branches.
- Accepted ADR 0004: generic core, jurisdiction provider boundary, U.S. first; BCBS conceptual,
  never a silent U.S. fallback; Alpha Manufacturing is a fixture, not a rule predicate.
- Only US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1 executes.
- Preserve source/raw capture hashes, original Sprint 01 fixture and human approval fields.
- EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE; no EAD alias.
- Only baseline_total_capital_equivalent at 0.08; never allocated/economic/complete required/
  institution-specific capital or a capital adequacy conclusion.
- Exact decimals, immutable tuples and deterministic canonical results; no authoritative LLM output.
- Regxify extraction and existing Basel/ERBA-engine integration analysis remain future work.
- V1 still includes Product V1 Golden Lesson + Growth V1 human-approved social publishing later.
- GCP direction is provisional. No automatic PR merge or expanded implementation authority.
