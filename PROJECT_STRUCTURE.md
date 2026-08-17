# Detailed Project Structure

```text
financial-pods/
|-- .github/workflows/ci.yml       Continuous integration quality gates
|-- compose.yaml                   Local web/API/PostgreSQL/Redis orchestration
|-- package.json                   Cross-platform root task entry points
|-- pnpm-workspace.yaml            JavaScript workspace and build-script policy
|-- Makefile                       Optional convenience wrapper for root tasks
|-- AGENTS.md                       Codex operating contract and definition of done
|-- README.md                       Human and Codex entry point
|-- PRODUCT_SCOPE.md                Product boundaries and first-product outcome
|-- ARCHITECTURE.md                 Canonical system architecture and boundaries
|-- IMPLEMENTATION_PLAN.md          Phased delivery plan
|-- ROADMAP.md                      Now/next/later roadmap
|-- CONTRIBUTING.md                 Contribution and review workflow
|-- CHANGELOG.md                    Notable repository changes
|-- PROJECT_STRUCTURE.md            This complete navigation guide
|-- ARTIFACT_CATALOG.md             Finalized-artifact inventory and checksums
|-- ARTIFACT_INTAKE.md              Artifact preservation and intake policy
|-- PACKAGE_GUIDE.md                Explanation of historical/source ZIPs
|-- MANIFEST.md                     Canonical project manifest
|-- apps/
|   |-- web/                        Next.js/React/TypeScript/Tailwind application
|   `-- api/                        FastAPI/Python/Pydantic application
|-- packages/
|   |-- ui/                         Shared accessible UI components
|   |-- regulatory/                 Versioned regulatory sources/rules and citations
|   |-- tutor/                      Grounded AI tutor orchestration and safeguards
|   |-- finance-engine/             Deterministic financial calculations
|   `-- learning/                   Lesson, assessment, mastery, and progress logic
|-- content/
|   `-- lessons/corporate-exposure/ First golden-lesson source content
|-- data/
|   `-- finbank/                    Synthetic FinBank and case fixtures
|-- docs/
|   |-- reference-artifacts/        Immutable finalized inputs
|   |   |-- research/               Master research/strategy blueprint
|   |   |-- specifications/         Final V1 functional/technical specification
|   |   |-- engineering/            Engineering and implementation references
|   |   |-- growth/                 Content growth/publishing strategy
|   |   |-- deck/                   Final presentation deck
|   |   |-- prototype/              Final HTML UI prototype
|   |   |-- developer-agent-starter/Extracted starter pack, preserved by relative path
|   |   `-- source-packages/         Original immutable ZIP packages
|   |-- architecture/               Living architecture documentation
|   |-- product/                    Living product decisions and requirements
|   |-- regulatory/                 Living reviewed regulatory research
|   |-- growth/                     Living growth/channel execution documents
|   `-- adr/                        Architecture decision records
|-- prompts/                        Active reviewed product prompts
|-- skills/                         Active project-specific Codex skills
|-- tests/
|   |-- unit/                       Isolated deterministic unit tests
|   |-- integration/                Cross-component and infrastructure tests
|   |-- regulatory/                 Versioned regulatory regression tests
|   `-- ai-evals/                   Repeatable AI behavior evaluations
|-- scripts/
|   |-- task.mjs                    Cross-platform setup and verification runner
|   |-- run-web-e2e.mjs             Cross-platform browser-test lifecycle wrapper
|   `-- verify-reference-artifacts.mjs Immutable-artifact checksum gate
|-- infra/
|   |-- docker/                     Local/container definitions
|   `-- terraform/                  Reviewed infrastructure as code
|-- sprints/
|   |-- sprint-00/                  Current repository-bootstrap sprint
|   |   |-- SPRINT.md               Scope, sequence, and stop condition
|   |   |-- ACCEPTANCE_CRITERIA.md   Objective completion checklist
|   |   `-- REVIEW.md               Verification evidence and acceptance decision
|   |-- sprint-01/                  Planned deterministic domain-model sprint
|   `-- sprint-02..05/               Future placeholders; no authorization implied
`-- archive/
    `-- bootstrap-packages/          Historical generated snapshots, not live source
```

`tests/integration/stack-health.mjs` is the executable four-service health and contract smoke
test. The regulatory and AI-evaluation test locations remain intentionally empty until authorized
by later sprints.

Sprint 00 runtime and onboarding details are documented in `docs/architecture/LOCAL_DEVELOPMENT.md`. Empty domain/content directories remain intentionally unused until an approved sprint authorizes their behavior.

## Where Codex writes code

Yes: all code must remain inside this project root. Frontend code goes in `apps/web`; backend code in `apps/api`; reusable domain and platform code in `packages/*`; tests in `tests/*` or colocated where the established tooling requires it; local/production infrastructure in `infra/*`.

Codex must not write production code into `docs/reference-artifacts/`, an extracted ZIP, the parent `D:\Financial Ai studio` folder, or a second `financial-pods` directory.

## Which documents control work

The active sprint is the narrowest authority. Root execution Markdown provides durable direction. Finalized documents provide requirements/research evidence but do not independently authorize implementation outside the sprint.
