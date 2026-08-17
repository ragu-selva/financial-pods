# Sprint 00 Review

Status: Accepted with documented follow-up

## Scope review

- Bootstrap-only boundary respected: Yes. Only application shells, local dependencies,
  verification tooling, and documentation were implemented.
- Existing finalized artifacts unchanged: Yes. The checksum gate verified all 10 finalized binary
  artifacts catalogued in `ARTIFACT_CATALOG.md`.
- Out-of-sprint product work detected: No. There is no FinBank, corporate-exposure, regulatory
  calculation, lesson, tutor, retrieval, account, billing, production deployment, or social-channel
  behavior.

## Verification evidence

Acceptance was run on 2026-08-17 on Windows with Node.js 24.14.1, pnpm 11.19.0,
Python 3.14.3 locally, Python 3.12.11 in the API image, Docker Engine 29.3.1, and Docker
Compose 5.1.0.

- `node scripts/task.mjs verify`: Passed.
  - Prettier and Ruff formatting checks passed.
  - ESLint, JavaScript syntax checks, and Ruff lint passed.
  - TypeScript strict checking and mypy passed for five API source files.
  - Vitest passed two files/three tests; pytest passed five tests.
  - The optimized Next.js production build passed; API sdist and wheel builds passed.
  - Playwright passed two Chromium tests covering the accessible shell and web health route, with
    clean process shutdown.
  - The immutable-artifact gate verified 10 catalogued reference artifacts.
- `node scripts/task.mjs stack-verify`: Passed.
  - Docker rebuilt the web and API images and waited for all four services to report healthy.
  - The integration probe verified the placeholder page, web health, the typed API health payload
    and trace ID, PostgreSQL with pgvector 0.8.1, and Redis `PONG`.
  - The running application is available at `http://localhost:3000`; the API health endpoint is
    available at `http://localhost:8000/health`.
- `.github/workflows/ci.yml`: Static review passed. The workflow installs locked dependencies,
  validates Compose and pgvector, verifies artifacts, and runs lint, formatting, types, tests,
  builds, and browser smoke tests with local CI-only service credentials.
- `.env.example`, `.gitignore`, and `.dockerignore`: Reviewed. Only local placeholder values are
  committed; real environment files, dependency directories, build output, caches, database
  state, secrets, and Terraform state are ignored.
- `scripts/task.mjs`, root package scripts, and `Makefile`: Reviewed. Required setup, dev,
  formatting, lint, type, test, build, browser, Docker lifecycle, artifact, aggregate, and stack
  verification tasks are wired.

## Risks and limitations

- GitHub has not been connected to this local repository, so the CI workflow could not receive an
  actual hosted GitHub Actions run. The local equivalents all passed, and the workflow structure
  is complete.
- GitHub Action references use official major-version tags. Pin them to reviewed commit SHAs when
  the GitHub repository is connected.
- Sprint 00 container development rebuilds images and does not provide source-mounted hot reload.
  Add that developer-experience layer only when an approved sprint schedules it.
- pytest emits one upstream Starlette `TestClient` deprecation warning; all five API tests pass.
- Docker Desktop must be running for the local stack and its integration check.

## Deferred work

All product functionality remains deferred. Connecting GitHub and choosing a production GCP
deployment architecture are separate follow-ups; neither changes the accepted Sprint 00 local
foundation.

## Decision

- [ ] Accepted
- [x] Accepted with documented follow-up
- [ ] Rework required

Reviewer/date: Codex principal engineer and regulatory-scope reviewer / 2026-08-17
