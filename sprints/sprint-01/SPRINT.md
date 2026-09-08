# Sprint 01 — FinBank and Corporate Exposure Domain Model

Status: Accepted by the accountable project owner/reviewer on 2026-08-27.

## Goal

Define the synthetic FinBank / Alpha Manufacturing case and a deterministic, typed corporate-
exposure domain model that can later support reviewed regulatory rules and calculations.

## Scope

- Synthetic institution, borrower, and loan/exposure fixtures
- Money, currency, percentage, dates, identifiers, validation, assumptions, and provenance
- Pure domain construction and validation with unit/property tests
- Serialization contract and ADRs for unresolved modeling decisions

The detailed boundary, approved facts, terminology, assumptions, and decisions are recorded in
DOMAIN_MODEL_SCOPE.md. ACCEPTANCE_CRITERIA.md is the completion contract.

## Exclusions

- No LLM-dependent calculation or classification
- No uncited regulatory assertion
- No risk weights, RWA, capital requirement, jurisdictional mapping, or regulatory conclusion until
  a ruleset is selected and reviewed
- No lesson UI or tutor implementation

## Entry and exit

Sprint 00 is accepted with documented follow-up in ../sprint-00/REVIEW.md.

The project owner approved SPRINT.md, DOMAIN_MODEL_SCOPE.md, and ACCEPTANCE_CRITERIA.md together on
2026-08-27 and accepted the accountable domain and regulatory-scope reviewer role. Activation
decisions are resolved in DOMAIN_MODEL_SCOPE.md and ADR 0002. Root current-status documents must
remain consistent with this active sprint.

Domain tests must remain isolated from web frameworks, databases, Redis, and LLM providers. Sprint
completion requires every acceptance criterion to pass with evidence in REVIEW.md.
