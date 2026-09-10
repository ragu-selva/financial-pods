# Sprint 03 — Proposed Lesson API and Service Contract

Status: PLANNING ONLY — NOT ACTIVE

## Scope and ownership

This is a proposed v1 presentation contract, not an implemented route or schema.
One read-only endpoint: `GET /api/v1/lessons/corporate-exposure/golden-case`.
One Next.js route: `/lessons/corporate-exposure`.

```text
Accepted fixture + approved local evidence bundle
  -> existing load_engine(repository) -> engine.calculate(snapshot)
  -> Python lesson application service
  -> explicit learner-safe DTO projection + exact display formatting
  -> existing FastAPI application
  -> Next.js server fetch (API_BASE_URL)
  -> seven read-only lesson sections / disclosures
```

The engine alone selects rules, validates facts/evidence, classifies, calculates and generates trace.
The lesson service selects the one approved fixture and invokes the unchanged engine. The mapper
owns reviewed teaching copy, allowlisting and formatting only. Next.js renders the DTO and manages
disclosures; no regulatory engine imports, weight table, formulas or LLM-generated explanations.

The endpoint accepts no body, case ID, borrower, amount, date, ruleset or jurisdiction selectors.
Reject query parameters rather than silently ignoring apparent calculation inputs. POST/PUT/PATCH/
DELETE are not supported. Alternate-case engine proofs stay regression tests, not learner controls.

## Server-side dependency prerequisites — future work only

The API currently has a health endpoint but no finance-package dependency or lesson service.
The finance engine is a separate pure package; `load_engine(Path)` also needs the unchanged fixture
and approved files under `sprints/sprint-02/`. Do not copy its regulatory implementation into API code.

For later implementation, explicitly install the local repository package (editable for development
or its locally built wheel), not a same-named package fetched from a public registry. Supply an
operator-configured trusted bundle root, never a request-controlled path or a fragile working-directory
guess. Load and verify the accepted fixture/evidence using the existing engine loaders; retaining
immutable objects in process is not database persistence or a Redis cache.

The snapshot carries borrower metadata but not all institution/product display names. Bind those
labels to the same accepted fixture via the existing fixture loader, reconcile IDs/principal with
the validated snapshot and retain the approved fixture-integrity check. Do not invent names from
internal IDs, load unverified alternative bytes or hard-code names into regulatory logic. Presentation
copy may say "Corporate term loan" only for the validated corporate/term-loan result.

The existing API Docker build context/image does not include the finance package or evidence.
Minimal local development/CI wiring must be agreed before implementation; existing container support
must not be falsely claimed. No Docker, deployment, package or configuration changes occur in this
planning task. Production image/deployment design remains excluded.

A future synchronous FastAPI handler/service can run the bounded synchronous engine work in the
framework's thread pool rather than block an async event loop. Failures loading or calculating the
lesson must not become an apparently successful result or silently change the existing health contract.

## Proposed public envelope

Proposed `schema_version = golden-lesson.v1`; final naming is pending owner approval.
Use explicit typed, immutable DTOs with forbidden extra fields. All fields below are required unless
marked otherwise. Because consumers reject unknown fields, even additive wire changes need an explicit
contract-version/compatibility review; do not silently change the pinned v1 payload. Changes to meaning,
types or lesson scope require a new version and owner review.

| Field                          | Meaning / allowed source                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| schema_version                 | Presentation schema version, not a source-manifest dump                                                                        |
| content_version                | Version of approved explanatory copy; no content hash                                                                          |
| lesson_id, title               | Stable public lesson slug and reviewed title                                                                                   |
| context                        | US, FRB, standardized approach, regulatory as-of date, exact accepted ruleset ID/version, synthetic/internal educational label |
| loan                           | Fixture-bound institution name, borrower name, product label, principal as MoneyDisplay; no internal case/counterparty IDs     |
| classification                 | Returned code/label, reviewed summary, grouped reasoning items and citation IDs bound to actual accepted facts/trace           |
| exposure_measure               | Returned type, basis, MoneyDisplay and learner label "Regulatory Exposure Amount"                                              |
| risk_weight                    | Returned ratio as RatioDisplay and supporting citation IDs                                                                     |
| rwa                            | Returned RWA as MoneyDisplay and supporting citation IDs                                                                       |
| educational_capital_equivalent | Only baseline_total_capital_equivalent; returned MoneyDisplay, RatioDisplay and supporting citation IDs                        |
| warnings                       | All mandatory engine warning meanings, public warning IDs and reviewed readable messages                                       |
| trace                          | Twelve ordered learner-safe step records bound to the actual engine trace                                                      |
| citations                      | Deduplicated public citation records referenced by the lesson and regulatory trace steps                                       |

`MoneyDisplay`: `{ "value": "10000000.00", "currency": "USD", "display": "USD 10,000,000" }`.
`RatioDisplay`: `{ "ratio": "1.00", "display": "100%" }`.
Authoritative decimals travel as exact strings, never JSON floating-point numbers. Formatting occurs
on the server with exact decimal-safe presentation operations; it must not recalculate financial
outputs. Browser components use the supplied display strings, not Number/parseFloat or ratio × 100.
The raw strings support contract validation; they are not permission for frontend arithmetic.

Numeric subsection example only (not a complete response; context, warnings, trace and citations
remain mandatory):

```json
{
  "classification": { "code": "CORPORATE" },
  "exposure_measure": {
    "type": "EXPOSURE_AMOUNT",
    "basis": "US_STANDARDIZED_CARRYING_VALUE",
    "label": "Regulatory Exposure Amount",
    "amount": {
      "value": "10000000.00",
      "currency": "USD",
      "display": "USD 10,000,000"
    }
  },
  "risk_weight": { "ratio": "1.00", "display": "100%" },
  "rwa": {
    "value": "10000000.00",
    "currency": "USD",
    "display": "USD 10,000,000"
  },
  "educational_capital_equivalent": {
    "kind": "baseline_total_capital_equivalent",
    "amount": {
      "value": "800000.00",
      "currency": "USD",
      "display": "USD 800,000"
    },
    "ratio": { "ratio": "0.08", "display": "8%" }
  }
}
```

Validate the private result against the exact accepted context:
`US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1`, US/FRB, as-of 2025-01-01.
No CURRENT alias, live-date substitution, proposal or R-1888 influence. EAD/CET1/Tier 1 fields are
absent. Original loan principal and regulatory exposure measure remain semantically separate even
when the same dollars appear in this case.

## Reasoning, trace, citations and warning projection

A reasoning item has a public ID, reviewed label/explanation, confirmed case outcome and citation IDs.
It may group the accepted negative corporate-definition screen for readability; it must not re-run
classification or omit relevant distinctions between definition exclusions and product/treatment guards.
Bind every item to a known accepted fact/operation/rule version. A missing mapping fails closed rather
than manufacturing a successful check.

A trace item has sequence, stable public step ID, learner title, explanation, optional already-returned
display values, warning IDs and citation IDs. Preserve all twelve actual steps in order; use the
mapping in [UX_FLOW.md](UX_FLOW.md). Empty citations are valid for non-regulatory context/verification
steps, which must not invent statutory authority. Required regulatory steps retain their sources.
Do not expose raw operation input maps, raw trace JSON or arbitrary dataclass serialization.

A citation record contains public ID, friendly title, authority, readable legal locator, canonical
official HTTPS URL and a dated-source/as-of label. Select from evidence bound to the actual rule
references, not a global bibliography or the first arbitrary citation. In particular, the risk-weight
card must identify 12 CFR 217.32(f)(1) and the dated 2025-01-01 official section, with relevant exception
screen context in the disclosure. Structured/raw source locator metadata is not learner copy.
No runtime source scraping or newly researched legal interpretation is needed for this lesson.

Mandatory warning meanings are internal prototype, educational only, not allocated loan capital,
not economic capital, not complete required regulatory capital, not institution-specific requirement
and not capital adequacy. Carry all seven through the DTO and render the educational warning and
five capital limitations next to the amount without requiring expansion.

## Privacy and validation boundary

Build an allowlisted projection; never return `result_to_dict(...)` plus a few removed fields.
Keep source hashes, absolute/relative filesystem paths, reviewer names/approval evidence, manifest
structures, raw retrieval metadata, input snapshot hashes and internal debug fields server-side.
This applies to HTTP JSON, rendered HTML, React server-component payloads, hydration and DOM attributes.
Public legal locators/ruleset identity are intentional context, not internal implementation metadata.

Use existing correlation-ID middleware for support, with sanitized logs/errors. Validate citation URLs
against the approved official-source hosts/schemes and escape all text. Do not accept arbitrary URLs,
embed raw source HTML, add a debug endpoint or fetch external citations through the server on demand.
The browser follows an official link only when the learner chooses it.

## Errors, loading and caching

Proposed statuses:

- 200: complete validated lesson DTO only; never a partially successful financial result.
- 400: unsupported query parameters or invalid request shape.
- 405: unsupported method, with no mutations.
- 503: lesson unavailable, including missing/tampered evidence, invalid/unapproved engine context or
  inability to map a required result/citation/warning. No fallback fixture, rule or stale result.
- 500: unexpected internal failure, sanitized; never expose exception text or filesystem details.

Stable public error example:
`{ "error": { "code": "LESSON_UNAVAILABLE", "message": "This lesson is temporarily unavailable." }, "trace_id": "<correlation-id>" }`.
Other failures get equally safe typed codes. Never include a partial result in an error.

Next.js uses server-only API_BASE_URL, an explicit bounded fetch timeout (proposed 10 seconds) and
no-store. API success/error responses use Cache-Control: no-store for this first slice. No polling,
Redis, persistent progress, automatic source refresh or silent stale cache. Loading/error UI can
retain the title but not invented financial values; a Retry action reloads the read-only request.
Malformed/unsupported DTOs are unavailable, not coerced into plausible numbers.

See [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) for proposed contract/integration proofs.
No endpoint, schema implementation, package wiring or tests are added by this document.

SPRINT 03 REMAINS INACTIVE
