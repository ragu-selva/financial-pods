# Implementation Plan

## Delivery approach

Work proceeds in gated sprints. Each sprint has a narrow outcome, acceptance criteria, review evidence, and explicit deferred work. A later sprint does not begin until the current sprint is accepted.

## Phase 0 — Foundation (Sprint 00)

Bootstrap the monorepo, web and API skeletons, local PostgreSQL/pgvector/Redis, Docker development workflow, environment conventions, task runner, quality gates, CI skeleton, and API health check. No product feature implementation.

## Phase 1 — Deterministic case core (Sprint 01)

Model FinBank, Alpha Manufacturing, loan/exposure inputs, money/percentage primitives, validation, and the first deterministic corporate-exposure domain boundary. Use synthetic data. No AI tutor and no unsupported regulatory conclusion.

## Phase 2 — Regulatory rules and calculation slice

Sprint 01 integration/hardening is accepted and merged through PR #2.
Sprint 02: ACTIVE on main after PR #4 merged at a89eeb6; narrow implementation present for review.
The owner approved the internal-prototype US / FRB / US_FRB_PART217_STANDARDIZED boundary for
2025-01-01 and its synthetic corporate Golden Case. See sprints/sprint-02/ACTIVATION_RECORD.json.
The planning branch is preserved, not wholesale merged. Implementation started separately from
activated origin/main on codex/sprint-02-us-corporate-engine, as explicitly authorized by the owner.

Implemented the generic engine -> registry -> jurisdiction provider architecture under accepted ADR 0004.
Only the narrow U.S. ordinary corporate path is implemented: typed exposure amount, 100% weight,
RWA, sole 8% educational total-capital equivalent, trace, citations and regulatory regression tests.
No broad Basel engine, other providers/classes, business routes, persistence, UI or tutor in Sprint 02.
Engineering evidence is in the active review. Human implementation PR acceptance/merge remains pending.

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
