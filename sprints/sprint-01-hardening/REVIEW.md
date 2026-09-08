# Sprint 01 Hardening Review

Status: Accepted and merged

Acceptance date: 2026-09-08.
Acceptance provenance: project owner's PR #2 merge and explicit post-merge cleanup instruction.
Merged PR: https://github.com/ragu-selva/financial-pods/pull/2
Merge commit: `b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183` (2026-09-08 12:40:59 -04:00).

## Authorization and integration

Project owner explicitly authorized this bounded hardening task on 2026-09-08. Branch
codex/sprint-01-hardening starts at origin/main 2781a8e. Merge 2281209 preserves original Sprint 01
commit 03b03ec. The original local Sprint 02 branch remains at 60fad85; its files are excluded.

## Defects and decisions

The current-state inventory found context-sensitive Decimal normalization/quantization, incomplete
case provenance coverage/path checks, and lists accepted into frozen tuple-typed fields. These
are correctness defects in the accepted Sprint 01 implementation, not new Sprint 02 scope.

ADR 0003 records the compatibility decisions: exact Decimal tuple canonicalization; isolated
exact arithmetic for existing Money operators; eight required schema 1.0 case-fact paths with
an explicit supported-path allowlist; rejection of non-tuple collections. JSON arrays and the
approved fixture remain unchanged. No regulatory provenance semantics have been introduced.

Before fixes, the new hostile-context fixture regression failed (serialized principal became NaN
with traps disabled). All 16 selected coverage/collection regression cases failed against the
original implementation. The complete new regression module now passes 89 tests.

## Verification

Date: 2026-09-08. Environment: Windows, Node.js 24.14.1, Python 3.14.3,
pytest 9.1.1, Hypothesis 6.165.10. Commands below ran against the integrated hardening worktree.

- VERIFIED: `node scripts/task.mjs verify` exited 0. Formatting (Prettier/Ruff), lint
  (JavaScript/ESLint/Ruff), TypeScript, strict mypy (API 5 files; finance engine 13 files),
  tests, builds, browser smoke tests, and reference artifact checks passed.
- VERIFIED: 130 finance-engine tests (original 41 plus 89 hardening cases), 5 API tests,
  3 web unit tests, and 2 Chromium smoke tests passed.
- VERIFIED: Next.js production build and API/finance-engine sdist and wheel builds passed.
- VERIFIED: `node scripts/task.mjs verify-artifacts` checked all 10 catalogued immutable artifacts.
- VERIFIED: `.venv/Scripts/python.exe -m pytest -c packages/finance-engine/pyproject.toml
  packages/finance-engine/tests/test_hardening.py --hypothesis-show-statistics -q` passed 89 tests.
  Each of the three new properties produced 100 passing examples. The subset generator discarded
  26 invalid draws, not failed examples. Tests exercise all eight rounding modes, low precision,
  restricted exponent limits, clamp, traps on/off, unchanged context flags, 50-digit coefficients,
  excess precision, signed zero, fixture round trips, provenance paths/coverage, and tuple integrity.
- VERIFIED: `docker compose --env-file .env.example config --quiet` passed (syntax/model only).
- NON-BLOCKING KNOWN LOCAL-RUNTIME LIMITATION: `docker info` and `node scripts/task.mjs stack-check` failed because
  `npipe:////./pipe/dockerDesktopLinuxEngine` is absent: `open //./pipe/dockerDesktopLinuxEngine:
  The system cannot find the file specified.` No running-stack success is claimed; stack-verify
  was not attempted after daemon unavailability was established. Infrastructure is unchanged.
  This environmental limitation does not block or reverse Sprint 01 hardening acceptance.
- VERIFIED: `git diff --check`; original 03b03ec ancestry; 60fad85 excluded from ancestry;
  original Sprint 02 branch still at 60fad85; no Sprint 02 files in this branch.
- VERIFIED: data/finbank, docs/reference-artifacts, and Sprint 00/01 records match 03b03ec exactly.

During development, the first full verify stopped at mypy because deliberate invalid-constructor
test inputs lacked arg-type annotations. This was corrected and the complete suite rerun to success.
Non-failing environment warnings remain: upstream Starlette/httpx TestClient deprecation, Windows
pytest cache WinError 183, Next.js slow-filesystem warning, and FORCE_COLOR/NO_COLOR notices.

## Hosted review

Post-merge documentation cleanup, 2026-09-08: `node scripts/task.mjs verify` reran successfully
(exit 0; 130 finance, 5 API, 3 web, 2 Chromium tests; formats/lint/types/builds/artifact checks).
Only living Markdown acceptance/publication records changed. Production code, fixtures,
dependencies, infrastructure, reference artifacts, and historical Sprint 00/01 reviews are unchanged.
Local Docker runtime was not retested because this cleanup changes no runtime or infrastructure.

[PR #2](https://github.com/ragu-selva/financial-pods/pull/2) was merged from
codex/sprint-01-hardening into main at `b0cf3a95c97c80fc73d5dbf1b12b59b45cac6183`.
The original commits and history remain preserved; no squash or history rewrite occurred.

VERIFIED: [GitHub Actions run 34247265131](https://github.com/ragu-selva/financial-pods/actions/runs/34247265131)
passed for implementation commit a71d639 on Ubuntu/Node 24/Python 3.12. All workflow steps passed,
including PostgreSQL/Redis service initialization, pgvector enable/check, Compose validation,
artifact hashes, lint, formatting, types, tests, builds, and Chromium smoke tests. Local Docker
remains a non-blocking known local-runtime limitation. The final PR head `46a723b` also passed
[run 34247638871](https://github.com/ragu-selva/financial-pods/actions/runs/34247638871).
These are observed hosted CI results, not an assertion about uninspected later runs.
Historical Sprint 00 and Sprint 01 review records remain unchanged.

## Deferred work and decision

All Sprint 02 calculations and later product work remain unauthorized. Historical Sprint 00 and
Sprint 01 review records are preserved. Acceptance and merge are complete on 2026-09-08.
Sprint 02 remains PLANNING ONLY — NOT ACTIVE. Its separately published planning branch is for
architecture/regulatory review only and is not merged into main.
