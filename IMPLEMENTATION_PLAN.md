# Implementation Plan

## Delivery approach

Work proceeds in gated sprints. Each sprint has a narrow outcome, acceptance criteria, review evidence, and explicit deferred work. A later sprint does not begin until the current sprint is accepted.

## Phase 0 — Foundation (Sprint 00)

Bootstrap the monorepo, web and API skeletons, local PostgreSQL/pgvector/Redis, Docker development workflow, environment conventions, task runner, quality gates, CI skeleton, and API health check. No product feature implementation.

## Phase 1 — Deterministic case core (Sprint 01)

Model FinBank, Alpha Manufacturing, loan/exposure inputs, money/percentage primitives, validation, and the first deterministic corporate-exposure domain boundary. Use synthetic data. No AI tutor and no unsupported regulatory conclusion.

## Phase 2 — Regulatory rules and calculation slice

Introduce a reviewed, versioned ruleset for one explicitly selected jurisdiction/framework; implement deterministic exposure-to-capital calculation, audit trace, citations, fixtures, and regulatory regression tests.

## Phase 3 — Golden lesson experience

Build the end-to-end web lesson, scenario walkthrough, calculator presentation, explanations, checks for understanding, accessibility, analytics events, and learner progress for the golden path.

## Phase 4 — Grounded tutor and evaluation

Add retrieval over approved content, tutor boundaries, refusal/uncertainty behavior, citation rendering, prompt/version management, adversarial tests, and repeatable AI evaluations. Calculations remain owned by the finance engine.

## Phase 5 — Beta readiness

Add identity and consent decisions, observability, support/admin workflows, performance and security review, content/regulatory sign-off, deployment infrastructure, backups, runbooks, and a limited public beta.

## Phase 6 — Learn and expand

Use beta evidence to improve the golden lesson before adding jurisdictions, exposure classes, curriculum breadth, commercial features, or channel integrations.

## Gates

- Product gate: acceptance criteria and user value are demonstrable.
- Regulatory gate: claims and rules are reviewed, dated, versioned, and cited.
- Engineering gate: lint, types, tests, builds, security checks, and environment verification pass.
- Release gate: rollback, observability, support, privacy, and known limitations are documented.
