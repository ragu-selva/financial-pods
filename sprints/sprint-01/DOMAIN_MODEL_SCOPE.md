# Sprint 01 Domain Model Scope

Status: Approved on 2026-08-27 by the project owner acting as accountable domain and
regulatory-scope reviewer.

This document is not a regulatory ruleset and does not authorize regulatory classification or
calculation.

## Reference basis

This Sprint 01 control document derives its product facts from the immutable finalized references:

- docs/reference-artifacts/research/Financial_Pods_Master_Strategy_Research_and_Implementation_Blueprint.docx
- docs/reference-artifacts/specifications/Financial_Pods_V1_Technical_and_Functional_Specification.docx
- docs/reference-artifacts/engineering/Financial_Pods_Engineering_Deployment_and_Coding_Playbook.docx

The live root execution documents and this sprint control pack remain the implementation authority.
The reference artifacts are evidence inputs and must not be modified.

## Approved case facts

- FinBank is a fictional, persistent synthetic bank used only for learning and reproducible tests.
- Alpha Manufacturing is a fictional corporate borrower/counterparty.
- The first case is a USD 10,000,000 term loan from FinBank to Alpha Manufacturing.
- The model keeps institution, counterparty, product, facility, and exposure concepts distinct.
- The case carries an explicit schema version, fixture version, as-of context, assumptions, and
  provenance.
- Sprint 01 models data only. It does not determine a regulatory exposure class, select a
  jurisdiction or ruleset, apply a risk weight, or calculate EAD, RWA, or capital.

## Approved software-domain terminology

- **Institution**: the synthetic FinBank legal entity that owns the case. This is a product-domain
  identity, not a claim about a licensed real-world institution.
- **Counterparty**: the party against which FinBank records a contractual exposure.
- **Borrower**: the counterparty role held by Alpha Manufacturing for this term-loan case.
- **Product**: the reusable product definition describing the case as a term loan.
- **Facility**: the specific contractual arrangement between FinBank and Alpha Manufacturing.
- **Exposure**: a versioned, as-of snapshot of outstanding principal associated with the facility.
  It is not a regulatory classification or regulatory EAD result.
- **Money**: an exact Decimal amount paired with a validated currency; binary floating point is
  prohibited.
- **Percentage**: an exact Decimal percentage whose permitted range is set by the owning field.
- **Assumption**: an explicit synthetic modeling choice with a stable ID, description, status, and
  provenance. An omitted source fact must not become an invisible default.
- **Provenance**: metadata identifying whether a value came from a finalized reference or an
  approved synthetic assumption, including a locator or assumption ID.
- **Fixture version**: the immutable semantic version of a complete synthetic case payload.

These are software-domain meanings for Sprint 01, not regulatory definitions. Future regulatory
terminology belongs to a reviewed and cited ruleset in a later sprint.

## Approved synthetic assumptions

- The USD 10,000,000 source fact means original facility principal.
- The facility originates on 2025-01-01 and matures on 2030-01-01.
- The exposure snapshot is taken on the origination date, 2025-01-01.
- Outstanding principal at that snapshot is USD 10,000,000. This avoids inventing amortization,
  repayments, interest, fees, or valuation changes.
- Rating, revenue, collateral, default status, guarantor, interest rate, committed-versus-undrawn
  amounts, borrower jurisdiction, and booking jurisdiction are deliberately absent.
- The initial supported-currency policy is version sprint-01-v1 and contains USD only.
- Money uses Python Decimal, permits at most two fractional digits, and rejects excess precision.
  Sprint 01 performs no implicit monetary rounding.
- Percentage uses Python Decimal, permits at most six fractional digits, and applies bounds only
  when an owning field explicitly supplies them.
- Identifiers are immutable, type-specific, human-readable opaque strings with entity prefixes:
  INS-, CP-, PRD-, FAC-, EXP-, and ASM-.
- packages/finance-engine owns the pure Python domain package. The root task runner includes this
  package in formatting, lint, strict type-check, test, and build tasks.

Each non-source value above must appear in the fixture assumptions and provenance.

## Modeling constraints

- Domain objects are typed, deterministic, framework-independent, and immutable.
- Construction rejects internally inconsistent states with stable structured errors.
- Dates are date-only ISO 8601 values; implicit current-time, locale, and timezone defaults are
  prohibited.
- Serialized payloads carry schema and fixture versions and round-trip without loss of precision.
- Core domain code has no dependency on FastAPI, Pydantic, databases, Redis, browser code, or LLM
  providers.
- Pydantic may be used only by a future boundary adapter outside the pure domain package.

## Reviewer responsibilities and approval

Accountable reviewer: Approving project owner (user; personal name not provided)
Role: Product owner and accountable domain/regulatory-scope reviewer
Approval date: 2026-08-27
Approval provenance: Explicit approval in the active Codex task.

The reviewer responsibilities are to:

- verify that every fixture value is synthetic, documented, and traceable;
- confirm that software terminology does not masquerade as a regulatory definition;
- reject uncited regulatory assertions or implicit classification/calculation behavior;
- approve assumptions and modeling decisions before implementation;
- review boundary and regression evidence before Sprint 01 acceptance; and
- record the final decision and date in REVIEW.md.

## Decision record

- Product owner decision: Approved
- Reviewer decision: Approved for Sprint 01 implementation
- Decision date: 2026-08-27
- Architecture record: docs/adr/0002-sprint-01-domain-model.md
