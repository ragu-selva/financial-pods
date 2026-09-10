# Sprint 03 — Planning Review

Status: PLANNING ONLY — NOT ACTIVE

Review date: 2026-09-10.

## Authority and actual Git baseline

The project owner closed Sprint 02 as ACCEPTED AND MERGED and authorized only this Sprint 03
planning pack. No Sprint 03 implementation or approval is implied.

Created codex/sprint-03-golden-lesson-planning from fetched origin/main at
979dda66a3cc3424d1bf244680ef719a879680e1, the implementation PR #5 merge. No history was rewritten.

The owner's request says PR #6 is merged. GitHub checks during this task instead report
[PR #6](https://github.com/ragu-selva/financial-pods/pull/6) open, merged=false, merged_at=null;
a repeat git fetch leaves origin/main at 979dda6. Its cleanup head remains c2b86e7 on its separate
branch. GitHub's prospective merge_commit_sha is not proof of merge. This discrepancy has been
reported to the owner; no merge is attempted here. The accepted engine is present through PR #5,
so planning proceeds from the requested actual remote baseline. Root status/roadmap and Sprint 02
records are deliberately not edited or copied into this five-file pack.

## IMPLEMENTED — existing dependency, not Sprint 03 work

- Accepted pure Python U.S. corporate engine with exact ruleset
  US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1 and approved local source/fixture loaders.
- Runtime Golden result: CORPORATE; EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE USD 10,000,000;
  weight 1.00; RWA USD 10,000,000; baseline_total_capital_equivalent USD 800,000 at 0.08.
- Twelve actual ordered source-linked trace steps, immutable results, exact arithmetic,
  alternate-name/amount proofs and fail-closed source/context guards.
- FastAPI health-only scaffold; Next.js bootstrap shell and health endpoint.
- R-1888 remains PROPOSED/non-executable. Approved regulatory coverage is unchanged.

## PLANNED — this pack, not implemented features

Five Markdown documents specify one read-only Golden Lesson, seven learner sections, a thin Python
application service, a learner-safe DTO, proposed GET endpoint, exact-value presentation, accessible
reasoning/source disclosures and future acceptance tests.

No lesson route, UI component, service, API business endpoint, runtime DTO, integration dependency,
test implementation, production code or infrastructure configuration was added. No source, fixture,
reviewer evidence, approval or regulatory-calculation code changed.

## Inspected design inputs

Repository AGENTS, current scope/architecture/implementation and sprint controls, project structure,
artifact catalog, accepted generalized-engine ADR 0004, Sprint 02 runtime contract, engine contracts/
loaders/fixture and current API/web/package/container boundaries informed this plan.

The immutable HTML Golden Lesson prototype was inspected only as visual reference. Its broader
SAMA/75%/EAD/calculator/tutor/voice/video/progress capabilities are not adopted. User-defined narrow
scope and accepted U.S. runtime take precedence. No new regulatory research or source capture occurred.

## VERIFIED — current baseline and planning artifacts

- node scripts/task.mjs verify: PASS / exit 0 on the fetched baseline during this task.
- Finance: 429 tests PASS, including accepted regulatory/property and generic-engine proofs.
- API: 5 tests PASS; web: 3 tests PASS; Chromium browser: 2 tests PASS.
- Formatting, ESLint/Ruff, mypy, TypeScript, Next.js production build and both Python source/wheel
  builds: PASS. Ten immutable reference artifacts verified.
- node --test sprints/sprint-02/planning-evidence.test.mjs sprints/sprint-02/activation-evidence.test.mjs:
  35 PASS, including preserved approved pins and all 71 captured-source hashes.
- Five planning Markdown files: Prettier PASS; inactive banners, local links, fenced JSON syntax
  and pinned Golden-value strings PASS. Exact five-file scope and unchanged tracked baseline PASS.
  Git whitespace and staged five-file scope checks PASS; these are rechecked before commit.

These are existing implementation checks plus document checks, not evidence of an implemented
Sprint 03 lesson/API. Hosted CI for this new planning branch is not claimed here.

## Known limitations and pending review

- PR #6 merge-state discrepancy remains a repository-control follow-up; do not silently claim a
  merge or merge it from this task. Reconcile main before any later implementation branch.
- Last recorded Docker runtime check could not open //./pipe/dockerDesktopLinuxEngine. This is a documented
  non-blocking accepted limitation, not a new stack-runtime pass. This planning task does not change
  infrastructure or claim container-based lesson integration.
- Existing non-failing tool warnings include Starlette/httpx deprecation, Windows pytest-cache
  WinError 183, Next.js filesystem-speed notice and NO_COLOR/FORCE_COLOR conflict.
- API package/evidence-bundle availability and bounded local/CI wiring need agreement before future
  implementation; current image does not supply the engine/evidence bundle.
- UX choices, explanatory copy, DTO naming, source-link behavior and error/exposure policy remain
  proposed. See UX_FLOW.md and API_CONTRACT.md. No human approval fields have been populated.

## Next action and stop boundary

Owner reviews this five-file planning pack and resolves the open UX/integration choices. A later,
explicitly approved task may activate a bounded implementation branch; no activation, PR, merge or
implementation is performed by this planning task.

SPRINT 03 REMAINS INACTIVE
