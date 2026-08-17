# Local development

Sprint 00 provides a reproducible local stack only. It does not deploy or configure any production cloud resources.

## Prerequisites

- Node.js 24
- pnpm 11
- Python 3.12, 3.13, or 3.14
- Docker Desktop with Docker Compose
- Git

GNU Make and pnpm script aliases are optional. The cross-platform Node task runner is the
canonical entry point on Windows, macOS, and Linux.

## First-time setup

From the repository root:

```text
node scripts/task.mjs setup
```

This installs the pinned web workspace and creates `.venv` for the pinned API dependencies. To select a particular Python installation, set `FINANCIAL_PODS_PYTHON` before running setup.

Playwright needs its browser binary once per machine:

```text
pnpm --dir apps/web exec playwright install chromium
```

## Run the complete stack

```text
node scripts/task.mjs stack-verify
```

Docker Compose builds and starts:

- Web: `http://localhost:3000`
- Web health: `http://localhost:3000/health`
- API health: `http://localhost:8000/health`
- API contract: `http://localhost:8000/docs`
- PostgreSQL with pgvector: `localhost:5432`
- Redis: `localhost:6379`

The application containers wait for PostgreSQL, pgvector, and Redis health checks. The web container waits for the API health check.

`stack-verify` builds the images, waits for all health checks, and runs the cross-service smoke
test. It leaves the stack running for inspection. Stop it with `node scripts/task.mjs down` and
follow service output with `node scripts/task.mjs logs`.

The Sprint 00 `dev` and `up` tasks build and run this same container stack. Source mounts and hot
reload are intentionally deferred; changes require an image rebuild in the current foundation.

## Quality gates

Run the same gates locally and in CI:

```text
node scripts/task.mjs verify
```

The aggregate command checks formatting, lint, types, unit tests, production builds, browser smoke
tests, and immutable artifacts. Individual tasks remain available through `node scripts/task.mjs
<task>`, pnpm aliases, or GNU Make.

## Configuration

The committed `.env.example` contains local-only, non-secret placeholder credentials. Copy it to
`.env` only when overriding defaults; never reuse those values outside local development. Real
`.env*` files are ignored.

PostgreSQL is the future source of record. pgvector is installed only to prove the approved retrieval dependency is available; no retrieval feature uses it in Sprint 00. Redis is present only for future ephemeral cache, session, queue, or rate-limit concerns and stores no authoritative state.

## Troubleshooting and recovery

- If Docker commands cannot connect, start Docker Desktop and wait until the engine reports ready.
- If port 3000, 8000, 5432, or 6379 is occupied, copy `.env.example` to `.env` and change the corresponding host port.
- If Python packages are inconsistent, remove only the repository-local `.venv` directory and rerun `node scripts/task.mjs setup`.
- If JavaScript packages are inconsistent, remove only the repository-local `node_modules` directory and rerun `node scripts/task.mjs setup`.
- To recreate local database state, run `docker compose down --volumes` and then `node scripts/task.mjs stack-verify`. This permanently deletes only the Compose-managed local development volume.
- If Playwright reports a missing browser, rerun `pnpm --dir apps/web exec playwright install chromium`.

Do not add production credentials, customer data, regulatory content, FinBank fixtures, or product functionality while Sprint 00 remains active.
