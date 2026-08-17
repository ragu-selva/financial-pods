# Financial Pods Agent Contract

## Required reading order

Before planning or changing code, read:

1. `PRODUCT_SCOPE.md`
2. `ARCHITECTURE.md`
3. `IMPLEMENTATION_PLAN.md`
4. The active sprint `SPRINT.md`, acceptance criteria, and review file
5. `PROJECT_STRUCTURE.md`
6. `ARTIFACT_CATALOG.md`
7. Finalized reference artifacts relevant to the active sprint

The active sprint is the narrowest execution boundary. Stop and document unresolved conflicts among sources.

## Repository and artifact rules

- `D:\Financial Ai studio\financial-pods` is the only live project root. Write all new code inside it.
- Never develop inside a ZIP or overwrite the live repository with a package snapshot.
- Files below `docs/reference-artifacts/` are immutable inputs. Do not modify them.
- The extracted developer starter pack is reference guidance; its nested root files do not override this contract or live root documents.
- Implement only work explicitly included in the active sprint. Never implement future-sprint features opportunistically.
- Sprint 00 is bootstrap only: no FinBank, corporate-exposure calculations, learning flow, tutor, regulatory logic, authentication, billing, or production deployment.
- Do not commit secrets. Use `.env.example`; ignore real `.env*` files.

## Financial and regulatory integrity

- Keep LLMs outside deterministic financial calculations. Formulas, classifications, transformations, and capital outputs must be typed, deterministic, and tested.
- Every regulatory assertion requires jurisdiction, authority/framework, source/citation, publication/effective dates, version, applicability, status, and reviewer provenance.
- Never present uncited model output as regulatory truth.

## Engineering standards

- API: Python 3.12+, FastAPI, Pydantic v2, pytest, Ruff, mypy, explicit types, boundary validation, and stable structured errors.
- Web: Next.js App Router, React, TypeScript strict, Tailwind, ESLint, Prettier, Vitest, Playwright, accessible semantic UI, and deliberate server/client boundaries.
- Data: PostgreSQL as system of record; pgvector only for approved retrieval; Redis only for bounded ephemeral concerns.
- Infrastructure: reproducible Docker Compose; pinned material versions; formatted/validated Terraform with no secrets or state committed.
- Domain packages must not depend on web frameworks, databases, Redis, or LLM providers.
- Record material architectural decisions in `docs/adr/`.

## Definition of done

A task is done only when it is in sprint, acceptance criteria are met, docs/tests/configuration are updated, reference artifacts are unchanged, and required checks pass. Regulatory changes require citations/versioning; deterministic financial behavior requires boundary and regression tests. Record evidence, limitations, and deferrals in the active `REVIEW.md`.

Before completion run the task-runner equivalents of:

```text
make lint
make typecheck
make test
make build
```

Also run E2E and infrastructure validation when affected. If a command cannot run, report the exact blocker and never claim it passed.
