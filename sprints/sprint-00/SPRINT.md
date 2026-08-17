# Sprint 00 — Repository Bootstrap

## Goal

Create a reproducible, quality-gated development foundation for Financial Pods. This sprint contains infrastructure and application skeletons only.

## In scope

- Monorepo/workspace conventions and dependency pinning strategy
- Next.js App Router + React + TypeScript strict + Tailwind skeleton in `apps/web`
- FastAPI + Python 3.12+ + Pydantic skeleton in `apps/api`
- `GET /health` returning a stable response with service status/version
- Local PostgreSQL with pgvector and Redis configuration
- Dockerfiles and Docker Compose development setup with health checks
- `.env.example`, ignored local environment files, and documented configuration
- Ruff, mypy, pytest; ESLint, Prettier, Vitest, Playwright
- Unit/integration test skeletons and health smoke tests
- CI workflow skeleton for install, lint, typecheck, test, and build
- Cross-platform Makefile or equivalent documented task runner
- Minimal developer onboarding and troubleshooting notes

## Explicitly out of scope

All product behavior: FinBank, Alpha Manufacturing, corporate exposure, regulatory rules/calculations, lesson UI, tutor/LLM, retrieval, user accounts, analytics, billing, production Terraform resources, and social-channel integrations.

## Deliverables

- Runnable web and API skeletons
- Healthy local dependency services
- One-command documented setup and verification path
- Automated quality gates and CI structure
- Completed `ACCEPTANCE_CRITERIA.md` and evidence in `REVIEW.md`

## Recommended sequence

1. Establish workspace, ignores, environment contract, and task runner.
2. Scaffold API and health test.
3. Scaffold web and smoke/unit test.
4. Add PostgreSQL/pgvector/Redis and Docker development orchestration.
5. Add lint, format, typing, testing, and build commands.
6. Add CI skeleton and documentation.
7. Run the full acceptance suite and record evidence.

## Stop condition

Stop when every Sprint 00 acceptance criterion passes. Do not begin Sprint 01.
