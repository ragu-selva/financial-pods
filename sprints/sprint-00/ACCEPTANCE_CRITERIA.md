# Sprint 00 Acceptance Criteria

Mark items complete only with evidence in `REVIEW.md`.

- [x] Existing finalized artifacts are unchanged.
- [x] `apps/web` starts and renders a minimal accessible placeholder without product features.
- [x] TypeScript strict, ESLint, Prettier, Vitest, and Playwright configurations execute.
- [x] The production web build succeeds.
- [x] `apps/api` runs on Python 3.12+ with FastAPI and Pydantic.
- [x] `GET /health` returns HTTP 200 with a documented typed payload and automated test.
- [x] Ruff, mypy, and pytest execute successfully.
- [x] PostgreSQL with pgvector and Redis report healthy locally.
- [x] Docker orchestration starts web, API, PostgreSQL/pgvector, and Redis with health checks.
- [x] `.env.example` contains no secrets; local secret/state files are ignored.
- [x] The task runner covers setup, dev, lint, format-check, typecheck, test, build, e2e, up, down, and logs (or equivalents).
- [x] Unit/integration locations are wired; regulatory and AI-eval suites remain placeholders.
- [x] CI runs install, lint, typecheck, test, and build without production secrets.
- [x] Onboarding documents prerequisites, startup, verification, and recovery.
- [x] `make lint`, `make typecheck`, `make test`, and `make build` (or equivalents) pass.
- [x] No FinBank, corporate-exposure, regulatory-calculation, lesson, or tutor feature was implemented.
