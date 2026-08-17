# AGENTS.md — Instructions for AI Coding Agents

## Mission
Build Financial Pods as a reliable, testable, auditable financial-learning platform. Optimize for correctness and maintainability before feature count.

## Non-negotiable rules
- Never encode regulatory calculations inside prompts or LLM-generated prose when a deterministic tool can calculate them.
- Never publish or modify regulatory source content without source URL, jurisdiction, status, version, effective date, and review state.
- Never allow the tutor to present an uncited regulatory claim as authoritative.
- Keep AI provider SDKs behind adapters. Domain code must not directly depend on one LLM, voice, avatar, or image vendor.
- Do not mix business logic with HTTP handlers, React components, or database ORM models.
- Any new persistent field requires a migration and backward-compatibility review.
- Every user-visible feature requires automated tests and observability events.
- Every AI behavior change requires an evaluation update.
- Every calculation change requires golden-case regression tests.
- Do not introduce Kubernetes, Spark, Neo4j, or another infrastructure component without an ADR and measured need.

## Implementation order
1. Domain model and contracts.
2. Deterministic behavior and tests.
3. API surface.
4. UI.
5. AI orchestration.
6. Observability and cost controls.
7. Documentation.

## Required pre-merge checks
- Backend lint/type/test pass.
- Frontend lint/type/unit/e2e pass for affected flows.
- Migrations reviewed.
- AI eval suite passes if prompts/tools/retrieval changed.
- Golden calculation cases pass if finance logic changed.
- Security/privacy checklist completed for new data flows.
- Docs and ADRs updated when architecture changed.
