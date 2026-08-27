# ADR 0002: Sprint 01 deterministic domain model

- Status: Accepted
- Date: 2026-08-27
- Decision owners: Project owner and accountable domain/regulatory-scope reviewer

## Context

Sprint 01 needs a small, reproducible FinBank/Alpha Manufacturing case without importing future
regulatory classification or calculation behavior. The finalized references establish a synthetic
USD 10 million term loan but do not define dates, balance semantics, identifiers, precision policy,
or package integration. Those choices must be explicit, deterministic, and testable.

## Decision

1. The pure Python package lives at packages/finance-engine with import package
   financial_pods_finance_engine. It has no runtime third-party dependencies and no imports from
   FastAPI, Pydantic, databases, Redis, browser code, or LLM providers.
2. Money uses Python Decimal with at most two fractional digits. Excess precision is rejected;
   Sprint 01 does not round implicitly. Only USD is supported by currency-policy version
   sprint-01-v1.
3. Percentage uses Decimal with at most six fractional digits. Range constraints are supplied by
   the owning field instead of being universal.
4. Entity identifiers are immutable, type-specific, human-readable opaque values using INS-, CP-,
   PRD-, FAC-, EXP-, and ASM- prefixes.
5. The USD 10 million means original principal. The approved synthetic facility originates on
   2025-01-01, matures on 2030-01-01, and has an exposure snapshot at origination with outstanding
   principal equal to original principal. No amortization, interest, fee, collateral, rating,
   revenue, default, jurisdiction, or regulatory meaning is inferred.
6. Public serialization is strict and versioned. Decimal values serialize as plain strings and dates
   as ISO 8601 date strings. Unknown fields and unsupported schema versions are rejected.
7. The root task runner includes formatting, Ruff, strict mypy, pytest/Hypothesis, and build checks
   for the package.

## Consequences

- The fixture is deliberately narrow but reproducible and traceable.
- Financial precision never depends on binary floating point, locale, or implicit rounding.
- A later sprint may add currencies, accounting attributes, or regulatory inputs only through an
  approved versioned change.
- Regulatory classification, EAD, risk weights, RWA, capital, citations, and jurisdiction adapters
  remain absent.
- Hypothesis becomes a pinned development dependency for property-based tests.
