# Financial Pods Agent Contract

## Required reading order

Before planning or changing code, read:

1. `PRODUCT_SCOPE.md`
2. `ARCHITECTURE.md`
3. `IMPLEMENTATION_PLAN.md`
4. The active sprint file, currently `sprints/sprint-00/SPRINT.md`
5. The active sprint acceptance criteria and review file

If these sources conflict, the active sprint is the narrowest execution boundary; stop and document any unresolved product or architecture conflict.

## Non-negotiable delivery rules

- Implement only work explicitly included in the active sprint. Never implement future-sprint features opportunistically.
- Sprint 00 is repository bootstrap only. Do not implement FinBank, corporate-exposure calculations, learning flows, AI tutor behavior, regulatory logic, authentication, billing, or production deployment.
- Keep LLMs outside deterministic financial calculations. Financial formulas, classifications, transformations, and regulatory-capital outputs must be deterministic, typed, testable code.
- Every regulatory assertion must carry jurisdiction, framework/source, citation, publication/effective dates, version, and applicability metadata. Never present uncited model output as regulatory truth.
- Treat files in `docs/reference-artifacts/` and other identified finalized artifacts as read-only unless the user explicitly authorizes an edit.
- Prefer small, reviewable changes. Record material architectural decisions in `docs/adr/`.
- Do not commit secrets. Use `.env.example`; keep real `.env*` files ignored.

## Engineering standards

### Python/API

- Python 3.12+, FastAPI, Pydantic v2, pytest, Ruff, and mypy strict-oriented checks.
- Use explicit types and dependency boundaries. Separate transport, application, domain, and infrastructure concerns.
- Validate external input at boundaries. Return stable structured errors and avoid leaking sensitive details.
- Unit-test deterministic domain behavior without network, database, Redis, or LLM dependencies.

### Web

- Next.js App Router, React, TypeScript strict, and Tailwind CSS.
- ESLint and Prettier are required. Use accessible semantic UI and server/client boundaries deliberately.
- Vitest covers units/components; Playwright covers critical browser journeys when a sprint introduces them.
- Avoid `any`; document any narrow exception.

### Data and infrastructure

- PostgreSQL is the system of record; pgvector is for explicitly approved retrieval use cases; Redis is for bounded cache/queue/session concerns.
- Docker Compose provides reproducible local development. Pin material image/dependency versions.
- Terraform changes must be formatted, validated, reviewed, and isolated from application secrets and state.
- Migrations must be forward-safe and reviewable; never edit an applied migration.

## Definition of done

A task is done only when:

- It is within the active sprint and its acceptance criteria are met.
- Code, tests, configuration, and relevant documentation are updated together.
- No finalized reference artifact was changed.
- Lint, formatting check, type checks, unit/integration tests, and production builds pass for affected components.
- Docker health checks pass when infrastructure is affected.
- Regulatory claims are versioned and cited; deterministic financial logic has boundary and regression tests.
- No secrets, generated caches, build output, or local state are committed.
- The active `REVIEW.md` contains verification evidence, limitations, and deferred work.

## Required completion commands

Use the repository task runner created in Sprint 00. Before declaring completion, run the equivalent of:

```text
make lint
make typecheck
make test
make build
```

Also run `make e2e` and infrastructure validation when the active sprint changes those areas. If a command cannot run, report the exact blocker; never claim it passed.
