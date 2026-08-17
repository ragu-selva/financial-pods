# Sprint 01 — FinBank and Corporate Exposure Domain Model

Status: Planned; do not implement during Sprint 00.

## Goal

Define the synthetic FinBank / Alpha Manufacturing case and a deterministic, typed corporate-exposure domain model that can later support reviewed regulatory rules and calculations.

## Candidate scope

- Synthetic institution, borrower, and loan/exposure fixtures
- Money, currency, percentage, dates, identifiers, validation, assumptions, and provenance
- Pure domain construction and validation with unit/property tests
- Serialization contract and ADRs for unresolved modeling decisions

## Exclusions

- No LLM-dependent calculation or classification
- No uncited regulatory assertion
- No risk weights, RWA, capital requirement, jurisdictional mapping, or regulatory conclusion until a ruleset is selected and reviewed
- No lesson UI or tutor implementation

## Entry and exit

Sprint 00 must be accepted. The case narrative, regulatory reviewer, terminology, and assumptions must be documented. Detailed acceptance criteria must be approved before implementation; domain tests must be isolated from frameworks, databases, Redis, and LLMs.
