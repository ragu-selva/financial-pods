# Financial Pods

This folder is the single canonical Codex project for the Financial Pods product.

## Current status

Sprint 00 is accepted with documented follow-ups. It provides the development foundation only:
minimal web and API applications, local PostgreSQL/pgvector and Redis, Docker Compose, automated
quality gates, and a CI workflow. Product, regulatory, lesson, tutor, and social-publishing
behavior remain out of scope.

## Quick start

Prerequisites are Node.js 24, pnpm 11, Python 3.12-3.14, Git, and Docker Desktop.

```text
node scripts/task.mjs setup
node scripts/task.mjs stack-verify
```

Then open `http://localhost:3000` for the placeholder web application or `http://localhost:8000/health` for the API health contract. Run all local gates with:

```text
node scripts/task.mjs verify
```

`stack-verify` builds the four containers, waits for their health checks, and verifies the API,
web, PostgreSQL/pgvector, and Redis contracts. The stack remains running for local inspection.

See `docs/architecture/LOCAL_DEVELOPMENT.md` for setup, service endpoints, configuration, and recovery guidance.

## Open this folder in Codex

Open `D:\Financial Ai studio\financial-pods` directly. Do not extract or open any of the ZIP packages as a separate project.

Before implementation, read `AGENTS.md`, `PRODUCT_SCOPE.md`, `ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, the active sprint file, `PROJECT_STRUCTURE.md`, and `ARTIFACT_CATALOG.md`.

## What lives here

- `apps/` — runnable web and API applications; all new application code goes here.
- `packages/` — shared UI, regulatory, tutor, finance-engine, and learning code.
- `content/` and `data/` — lesson content and synthetic FinBank data created in scheduled sprints.
- `docs/reference-artifacts/` — unchanged finalized research, specifications, deck, prototype, and source packages.
- `docs/architecture/`, `docs/product/`, `docs/regulatory/`, `docs/growth/`, `docs/adr/` — living project documentation derived or authored during implementation.
- `prompts/` and `skills/` — active prompt and Codex-skill assets when scheduled and reviewed.
- `tests/` — unit, integration, regulatory regression, and AI evaluation suites.
- `infra/` — Docker and Terraform configuration.
- `sprints/` — the controlling execution boundary. Sprint 00 is current.
- `archive/` — historical package snapshots; these are not the live codebase.

## Source-of-truth policy

The root Markdown execution documents and active sprint control implementation. Finalized binaries under `docs/reference-artifacts/` are preserved unchanged and used as research inputs. If a finalized artifact conflicts with the active execution documents, stop and record the discrepancy rather than silently choosing one.

See `PROJECT_STRUCTURE.md` for the complete tree and `PACKAGE_GUIDE.md` for the purpose of each ZIP.
