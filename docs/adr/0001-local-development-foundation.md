# ADR 0001: Sprint 00 local development foundation

- Status: Accepted
- Date: 2026-08-16

## Context

Sprint 00 needs a reproducible local environment for a Next.js web skeleton, a FastAPI API skeleton, PostgreSQL with pgvector, and Redis. Production hosting is intentionally deferred, and the owner has expressed a preference for Google Cloud that is not yet locked.

## Decision

Use Docker Compose as the local orchestration boundary. PostgreSQL is the future system of record, pgvector is installed but unused until an approved retrieval sprint, and Redis is limited to future bounded ephemeral concerns. Use a repository task runner with Node.js as the cross-platform entry point and retain a Makefile as a convenience wrapper. CI runs the same quality-gate commands without production credentials.

No production cloud, networking, identity, secret-management, backup, or disaster-recovery resources are selected or provisioned in Sprint 00.

## Consequences

- Local contributors get consistent service versions and health checks.
- Windows contributors do not require GNU Make.
- Infrastructure choices remain reversible until a production-hosting ADR is approved.
- PostgreSQL, pgvector, and Redis prove connectivity and readiness only; they do not authorize application feature use.
