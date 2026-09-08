# Financial Pods Sprint Roadmap Summary

## Roadmap status

- **Sprint 00** is accepted with documented follow-up.
- **Sprint 01** is accepted; no later sprint is currently active.
- **Sprint 01 hardening** is the current authorized integration/correctness task; see its control pack.
- **Sprint 02 through Sprint 05** below are a proposed mapping of the approved implementation phases and updated Growth V1 roadmap. Each requires its own `SPRINT.md`, acceptance criteria, review file, owner, and approval before implementation.
- **After V1** is an expansion phase driven by beta evidence rather than a currently authorized sprint.

## Sprint 00 — Repository foundation

### Goal

Create a reproducible, quality-gated development foundation without implementing product behavior.

### Key deliverables

- Next.js web and FastAPI API skeletons
- PostgreSQL with pgvector and Redis in Docker Compose
- Health endpoint and automated smoke tests
- Lint, formatting, type-checking, unit, integration, and browser-test foundations
- Git, CI workflow, environment conventions, task runner, onboarding, and troubleshooting

### Expected result

One documented command can start and verify the complete local engineering environment. No Golden Lesson, calculation, tutor, or social-publishing functionality exists yet.

### Exit gate

All Sprint 00 acceptance criteria pass and evidence is recorded in `sprints/sprint-00/REVIEW.md`.

## Sprint 01 — FinBank domain model

### Goal

Define the synthetic FinBank and Alpha Manufacturing case using deterministic, typed domain objects.

### Key deliverables

- Synthetic institution, borrower, facility, and exposure fixtures
- Money, currency, percentage, date, identifier, assumption, and provenance types
- Boundary validation and serialization contracts
- Pure domain construction with unit and property tests
- ADRs for unresolved modeling decisions

### Expected result

A tested, framework-independent case model exists, but it does not yet assign risk weights or calculate RWA and capital.

### Exit gate

Sprint 00 is accepted, and detailed Sprint 01 acceptance criteria, terminology, assumptions, and reviewer responsibilities are approved.

## Sprint 02 — Reviewed rules and calculation

### Goal

Implement one reviewed regulatory framework as a deterministic exposure-to-capital calculation slice.

### Key deliverables

- Versioned regulatory sources and rules with exact citations
- One explicitly selected jurisdiction or framework ruleset
- Deterministic exposure classification, risk weight, RWA, and capital path
- Audit trace preserving inputs, rules, intermediate steps, outputs, and citations
- Golden fixtures, boundary tests, and regulatory regression tests

### Expected result

The Alpha Manufacturing case produces a reproducible and reviewable capital result without relying on an LLM.

### Exit gate

An accountable regulatory reviewer approves the ruleset, assumptions, fixtures, expected results, and citations.

## Sprint 03 — Golden Lesson and Growth foundation

### Goal

Turn the deterministic case into the end-to-end learner experience and the governed source for public content.

### Key deliverables

- Golden Lesson scenario walkthrough and calculator presentation
- Checks for understanding, accessibility, progress state, and analytics events
- Regulatory source panel and explanation of calculation steps
- Growth V1 source packets, canonical scripts, channel templates, and approval records
- Draft cornerstone content and derivatives for priority social channels

### Expected result

A learner can complete the Golden Lesson path, and the same approved knowledge can produce controlled public education assets.

### Exit gate

Product behavior and public claims trace to the same approved sources and deterministic calculation fixtures.

## Sprint 04 — Grounded tutor and evaluation

### Goal

Add an AI tutor that teaches from approved content while preserving deterministic calculation authority.

### Key deliverables

- Retrieval over approved lesson and regulatory content
- Tutor modes, citations, uncertainty, and refusal behavior
- Prompt and model version management
- Adversarial, grounding, citation, tool-use, and numerical-fidelity evaluations
- Public-content QA assistance without automatic regulatory approval

### Expected result

The tutor can explain, question, compare, and coach with citations while refusing unsupported claims and using tools for authoritative numbers.

### Exit gate

AI evaluation thresholds pass with no material regulatory-status, citation, or calculation-fidelity failures.

## Sprint 05 — Beta and coordinated initial release

### Goal

Make Product V1 and Growth V1 safe, observable, supportable, and ready for a limited public release.

### Key deliverables

- Identity and consent decisions, observability, security, and performance review
- GCP deployment ADR and production infrastructure plan
- Backups, recovery, support/admin workflows, runbooks, and release controls
- Content and regulatory sign-off for the Golden Lesson
- At least 10 approved Basel assets with owners, CTAs, attribution, review dates, and correction paths
- Limited practitioner beta and product-plus-growth release evidence

### Expected result

The first Financial Pods release is live as one coordinated system: a validated Golden Lesson plus a governed public acquisition engine.

### Exit gate

Product, regulatory, engineering, security, operations, and Growth V1 release evidence are accepted together.

## After V1 — Learn and expand

### Goal

Use beta evidence to improve the first lesson before expanding scope.

### Key deliverables

- Learning, engagement, trust, conversion, and cost review
- Golden Lesson corrections and experience improvements
- Additional jurisdictions, regulatory versions, and exposure classes when approved
- Broader curriculum and content library
- Automated publishing integrations only after measured need and governance approval

### Expected result

Financial Pods scales from evidence rather than assumptions, reusing the validated product and content factory.

### Expansion gate

Each expansion receives its own sprint scope, owner, acceptance criteria, and review evidence.

## Initial release outcome

### Product V1

A learner can move from a corporate loan to a deterministic, cited regulatory-capital result; understand it through the Golden Lesson and grounded tutor; practice; and produce mastery evidence.

### Growth V1

The same approved knowledge produces at least 10 traceable public Basel assets across priority channels, each with human approval, one CTA, attribution, review timing, and a correction path.

## Cloud direction

Local development remains Docker-based and cloud-neutral. GCP is the preferred production candidate, but Cloud Run, Cloud SQL with pgvector, Memorystore, storage/CDN, security, backup, and recovery choices will be locked later through an approved ADR.
