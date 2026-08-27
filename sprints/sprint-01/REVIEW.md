# Sprint 01 Review

Status: Accepted.

## Activation evidence

- Product owner approval: Approved in the active Codex task on 2026-08-27
- Accountable reviewer: Approving project owner (user; personal name not provided)
- Reviewer role: Product owner and accountable domain/regulatory-scope reviewer
- Reviewer acceptance of responsibilities: Approved
- Modeling decisions resolved: Yes; DOMAIN_MODEL_SCOPE.md and ADR 0002
- Root status documents updated consistently: Yes
- Approved control-pack date: 2026-08-27

## Scope review

- FinBank/Alpha Manufacturing domain boundary implemented: Yes
- Only approved synthetic facts and assumptions used: Yes
- Regulatory classification/calculation exclusions respected: Yes
- Framework/database/Redis/LLM independence verified: Yes
- Out-of-sprint work detected: No
- Finalized reference artifacts unchanged: Yes; all 10 catalogued artifacts verified

## Acceptance-criteria evidence

### Governance and ADRs

- SPRINT.md, DOMAIN_MODEL_SCOPE.md, and ACCEPTANCE_CRITERIA.md were approved together.
- ADR 0002 records package, precision, identifier, fixture, and serialization decisions.
- PRODUCT_SCOPE.md, README.md, MANIFEST.md, PROJECT_STRUCTURE.md, ROADMAP.md, and the sprint
  roadmap summary identify Sprint 01 consistently.

### Synthetic fixture and provenance

- data/finbank/alpha_manufacturing_v1.json is schema 1.0 / fixture 1.0.0.
- It models FinBank, Alpha Manufacturing, a term-loan product, facility, and as-of exposure as
  distinct concepts.
- USD 10,000,000 is original principal. Outstanding principal equals that amount only at the
  approved origination-date snapshot.
- Two approved assumptions cover dates and the exposure snapshot. Eight field-level provenance
  entries distinguish finalized-reference facts from approved synthetic assumptions.
- tests/test_fixture.py verifies identity, amount semantics, assumptions, provenance, and forbidden
  dependency absence.

### Primitives and domain invariants

- identifiers.py implements immutable type-specific IDs with INS-, CP-, PRD-, FAC-, EXP-, and ASM-
  prefixes.
- primitives.py implements the sprint-01-v1 USD policy, exact Decimal money with two-digit maximum
  precision and no implicit rounding, and six-digit exact percentages with field-specific bounds.
- model.py enforces positive facility principal, date ordering, as-of boundaries, currency
  consistency, cross-entity references, approved assumptions, and provenance references.
- errors.py provides stable code/field/message validation issues.

### Serialization contract

- serialization.py implements strict schema 1.0 serialization with exact field sets.
- Money serializes as fixed plain decimal strings; dates serialize as canonical ISO 8601 strings.
- Unknown/missing fields, unsupported versions, noncanonical dates, non-finite/scientific decimals,
  excess precision, and invalid cross-field states are tested.
- Fixture serialization round-trips without loss.

### Unit, boundary, and property tests

- Finance-engine pytest: 41 tests passed.
- Hypothesis 6.165.10 property tests cover Money and Percentage decimal serialization round trips.
- Boundary tests cover malformed/unsupported currency, wrong identifier types/prefixes, zero
  principal, invalid date ranges, cross-reference errors, missing provenance, missing assumption
  references, malformed decimals, unknown fields, and unsupported schemas.
- AST dependency test verifies the domain package imports no FastAPI, Pydantic, database, Redis, or
  LLM-provider modules.

### Task-runner and regression integration

- scripts/task.mjs includes finance-engine Ruff format/lint, strict mypy, pytest, and package build.
- apps/api/pyproject.toml, requirements-dev.lock, and uv.lock pin Hypothesis and its resolved
  sortedcontainers dependency.
- The existing web and API tests/builds remain green.

## Verification evidence

Verification date: 2026-08-27
Environment: Node.js 24.14.1, pnpm 11.19.0, Python 3.14.3

- node scripts/task.mjs format-check: Passed for web, API, and finance engine
- node scripts/task.mjs lint: Passed for scripts, web, API, and finance engine
- node scripts/task.mjs typecheck: Passed; API 5 files and finance engine 12 files
- node scripts/task.mjs test: Passed; Vitest 3, API pytest 5, finance-engine pytest 41
- node scripts/task.mjs build: Passed; Next.js production build, API sdist/wheel, and finance-engine
  sdist/wheel
- node scripts/task.mjs e2e: Passed; 2 Chromium smoke tests
- node scripts/task.mjs verify-artifacts: Passed; 10 immutable artifacts verified
- git diff --check: Passed
- Docker/infrastructure validation: Not required; no Compose, container, database, Redis, or
  infrastructure behavior changed

## Risks and limitations

- The accountable reviewer is identified by role and task provenance because no personal name was
  provided.
- USD is the only supported currency in Sprint 01.
- Facility and exposure dates are explicit synthetic assumptions, not reference-artifact facts.
- Money rejects excess precision and performs no implicit rounding; later calculation rules must
  introduce reviewed rounding behavior explicitly.
- The existing API test suite still emits the documented upstream Starlette TestClient deprecation
  warning and a non-failing pytest cache warning on this Windows workspace.
- Browser verification reported a slow-filesystem warning and FORCE_COLOR/NO_COLOR notices; tests
  passed.
- No hosted CI run was available; the complete local CI-equivalent verification passed.

## Deferred work

The following remain excluded from Sprint 01:

- regulatory exposure classification or jurisdiction mapping;
- risk weights, credit-conversion factors, regulatory EAD, RWA, or capital calculations;
- cited regulatory rulesets and regression fixtures;
- lesson UI, learner progress, assessment, tutor, or LLM behavior;
- authentication, billing, production deployment, and social publishing.

## Decision

- [x] Accepted
- [ ] Accepted with documented follow-up
- [ ] Rework required
- [ ] Ready for accountable reviewer decision

Reviewer/date: Approving project owner / 2026-08-27
