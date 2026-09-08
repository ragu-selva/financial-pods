# Sprint 01 Hardening Review

Status: Local verification complete; PR publication/hosted CI pending. Not yet accepted.

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
- BLOCKED: `docker info` and `node scripts/task.mjs stack-check` failed because
  `npipe:////./pipe/dockerDesktopLinuxEngine` is absent: `open //./pipe/dockerDesktopLinuxEngine:
  The system cannot find the file specified.` No running-stack success is claimed; stack-verify
  was not attempted after daemon unavailability was established. Infrastructure is unchanged.
- VERIFIED: `git diff --check`; original 03b03ec ancestry; 60fad85 excluded from ancestry;
  original Sprint 02 branch still at 60fad85; no Sprint 02 files in this branch.
- VERIFIED: data/finbank, docs/reference-artifacts, and Sprint 00/01 records match 03b03ec exactly.

During development, the first full verify stopped at mypy because deliberate invalid-constructor
test inputs lacked arg-type annotations. This was corrected and the complete suite rerun to success.
Non-failing environment warnings remain: upstream Starlette/httpx TestClient deprecation, Windows
pytest cache WinError 183, Next.js slow-filesystem warning, and FORCE_COLOR/NO_COLOR notices.

## Hosted review

PR number and hosted CI evidence will be recorded after publication. Local success is not presented
as hosted CI success. Historical Sprint 01 review records remain unchanged.

## Deferred work and decision

All Sprint 02 calculations and later product work remain unauthorized. Historical Sprint 00 and
Sprint 01 review records are preserved. Accountable reviewer acceptance is pending the PR review.
