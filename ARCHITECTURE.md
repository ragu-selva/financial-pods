# Architecture

## System shape

- `apps/web`: Next.js/React/TypeScript/Tailwind learner experience
- `apps/api`: Python 3.12+/FastAPI/Pydantic API
- `packages/finance-engine`: deterministic financial and capital calculations
- `packages/regulatory`: versioned regulatory source models, applicability, and citations
- `packages/tutor`: grounded tutor orchestration and safeguards
- `packages/learning`: lesson, assessment, and mastery domain logic
- `packages/ui`: shared accessible presentation components
- PostgreSQL: authoritative application data
- pgvector: approved semantic retrieval indexes, never calculation logic
- Redis: bounded ephemeral cache/queue/session concerns

## Dependency direction

Transport/UI -> application services -> domain packages -> explicit infrastructure adapters. Domain packages must not depend on web frameworks, databases, Redis, or LLM providers.

## Deterministic calculation boundary

Inputs are validated and normalized, an explicit ruleset version is selected, typed pure functions calculate outputs, and an audit record preserves inputs, ruleset, intermediate values, output, and citations. LLMs may explain a completed result but cannot choose formulas, alter numeric outputs, or become a fallback calculator.

## Regulatory knowledge model

Every assertion or rule must include a stable ID, jurisdiction, authority/framework, source title and URL/document locator, pinpoint citation, publication/effective dates, version, applicability conditions, status, and reviewer provenance. Superseded rules remain reproducible. Retrieval answers must distinguish source text, interpretation, and product explanation.

## API conventions

- Version public routes under `/api/v1` when product endpoints begin.
- Sprint 00 exposes only a health endpoint.
- Use Pydantic request/response models, structured errors, correlation IDs, and explicit timeouts.
- Generate or validate an API contract before cross-app integration.

## Security and privacy

Least privilege, no secrets in source, dependency scanning, secure defaults, input validation, auditability for regulated-content changes, and synthetic data by default. Threat modeling and authentication are introduced only in scheduled sprints.

## Deployment direction

Local development uses Docker Compose. CI verifies formatting, lint, types, tests, and builds. Production infrastructure is defined later with Terraform after an ADR selects hosting, networking, identity, secrets, observability, backup, and disaster-recovery choices.

## Architecture decisions

Material decisions must be captured as numbered ADRs in `docs/adr/` with context, decision, consequences, and status.

## Sprint 02 implemented narrow domain slice

ADR 0004 is ACCEPTED for the internal prototype: generic regulatory engine -> ruleset registry ->
jurisdiction provider -> USStandardizedRuleset first. BCBS supplies concepts, not binding U.S.
numerical defaults; other providers and Regxify core extraction are future work.
The approved evidence package is pinned to US / FRB / US_FRB_PART217_STANDARDIZED / 2025-01-01.
Only the approved ordinary corporate Golden Case boundary is covered; borrower names cannot
choose rules. Source resolution never performs classification/calculation or human approval.
PR #4 merged at a89eeb6; the authorized implementation lives inside
packages/finance-engine/src/financial_pods_finance_engine/regulatory. Generic immutable contracts,
canonical serialization and registry/orchestration are separate from us_sources/us_standardized.
The adapter loads pinned local evidence and the unchanged Sprint 01 fixture before calculation.
The in-memory engine emits a 12-step trace, exact exposure amount/1.00 weight/RWA and the sole
0.08 educational equivalent. Only the exact approved ruleset/date can execute; no EAD alias.
No calculation network, clock, random, database, Redis or LLM calls. Other package directories,
product persistence and business routes remain planned. See sprints/sprint-02/RUNTIME_CONTRACT.md.
