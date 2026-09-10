# Sprint 02 Runtime Contract

Status: ACTIVE

Implementation: IMPLEMENTED, locally VERIFIED, pending implementation PR review.
Contract owner: the Financial Pods finance-engine package. Accepted ADR 0004 is unchanged.
Activation PR #4 merged at a89eeb60727c5f615514f75ecc27f57f19ec23cf.
The source/Golden/human approval artifacts remain byte-identical to that baseline.

## Architecture and module boundary

```text
Typed immutable facts + context
             |
Generic RulesetRegistry (exact version/date, no aliases)
             |
RegulatoryEngine (ordered orchestration, no jurisdiction formulas)
             |
USStandardizedRuleset + pinned in-memory USSourcePackage
             |
Corporate classification -> ordinary treatment -> EXPOSURE_AMOUNT
             |
Risk weight 1.00 -> exact RWA -> sole 0.08 educational equivalent
             |
Immutable 12-step trace + citations + warnings/exclusions
```

- contracts.py: frozen, slotted, runtime-validated domain contracts.
- serialization.py: strict fact ingress, canonical JSON, authoritative input/result hashing.
- engine.py: provider protocol, registry, generic orchestration and failure/success traces.
- us_sources.py: immutable evidence bytes, approval/hash checks and local fixture/evidence loading.
- us_standardized.py: only the approved U.S. institution, corporate and measurement predicates.
- arithmetic.py: isolated exact Decimal multiplication and unsupported-rounding errors.
- errors.py: stable error codes, paths and failure evidence.
- **init**.py: load_engine(repository) composition boundary.

Disk access belongs to the loader before calculation. Loaded calculations use in-memory bytes only:
no network, clock, random, database, Redis, web framework or LLM. Direct public U.S. calculation
methods also revalidate source approval/hashes; they cannot bypass the engine's evidence gate.
Use RegulatoryEngine.calculate for the complete validation, trace and deterministic result contract.
Provider registrations are trusted application composition, not an untrusted Python plugin sandbox.
Only one provider/version is bundled; adding another requires explicit approval and implementation.

## Versioned contracts

- regulatory-facts.v1: context, facts, request metadata and fixture version.
- regulatory-classification.v1: jurisdiction, exact ruleset version, exposure class/subclass,
  reason codes, rule references and warnings.
- regulatory-calculation.v1: classification, treatment, regulatory_exposure_measure, risk_weight,
  rwa, capital_teaching_outputs, jurisdiction/as-of, fixture/fact schema version, exact ruleset ID/
  version, rule versions, manifest hash, catalog snapshot ID, input snapshot hash, trace,
  citations, warnings and exclusions.
- regulatory-trace.v1: ordered immutable steps.
- regulatory-engine.v1: implementation-contract reference for non-regulatory operations.

These finalize the earlier v0.2-draft design, not an alias or backwards-compatible draft decoder.
Nested typed contracts inherit the enclosing v1 schema version. There is no result-deserialization
API in this slice. result_to_dict/result_to_json emit detached JSON representations.
No top-level EAD alias or duplicated authoritative exposure_amount exists.

## Fact contract and approved adapter

Context must explicitly supply jurisdiction=US, regulator=FRB, regime=STANDARDIZED,
as_of_date=2025-01-01 and
ruleset_version=US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1.

Each fact contains path, value and immutable provenance. Values are exact str/bool/int or Money;
JSON Money is {"amount":"10000000.00","currency":"USD"}. Decimal JSON numbers/floats are rejected.
Provenance requires source_ref, source_version, assumption_id and the internal-prototype review status.
The loader derives every required fact from the pinned approved enrichment, not defaults:
institution, counterparty, PPP, accounting, market risk, other scope, exposure and every named
alternative of the fourteen corporate-definition exclusions. Definition assessments become explicit
boolean facts; absent, UNKNOWN and positive excluded assessments fail closed.

The accepted Sprint 01 fixture is read and hash checked; its principal/date fields are reconciled
with approved enrichment. Its names/IDs are request metadata only. The fixture itself is unchanged.
Provenance establishes traceable synthetic assertions, not verified real-world facts or authentication
of a submitter's claim to review. The approved loader is the internal prototype's supported fact origin.

The owner requested an alternate amount with otherwise identical approved assumptions. Eight
correlated monetary fields may vary together: accounting original_principal, outstanding_principal,
gross_amortized_cost, net_balance_sheet_amount_candidate, gaap_based_regulatory_carrying_value_candidate;
exposure original_principal, outstanding_balance and gaap_carrying_value. They must be the same positive
USD amount. This is a zero-adjustment narrow carrying-value reconciliation, not a GAAP/CECL engine.
Accrued interest/fees, premiums/discounts, write-offs and allowance remain explicitly zero; PCD,
AFS/HTM, trading/covered position, PPP, CBLR and other excluded paths remain as approved.
All other material facts must match the approved narrow scope. No materially different case inherits approval.

Optional informational.bcbs_sme, bcbs_external_rating, specialised_lending, regulatory_retail and
annual_sales fields are non-authoritative. They cannot select, veto or reweight U.S. classification.
Unknown non-extension paths and contradictory duplicate facts are rejected.
Direct immutable contracts require exact tuples, not lists or tuple subclasses; strict JSON ingress
converts arrays to detached tuples. Duplicate paths and incomplete/unapproved provenance fail.

## Exact arithmetic and result

Golden result (observed, not merely copied from the approved expected-output artifact):

```text
classification                           CORPORATE / GENERAL_CORPORATE
regulatory_exposure_measure.amount        USD 10,000,000.00
measure_type                             EXPOSURE_AMOUNT
measurement_basis                        US_STANDARDIZED_CARRYING_VALUE
risk_weight                              1.00 (ratio, not percentage points)
rwa                                      USD 10,000,000.00
baseline_total_capital_equivalent         USD 800,000.00
teaching ratio                           0.08
```

A different borrower name/counterparty ID/case ID produces identical authoritative JSON and trace.
USD 5,000,000 with identical scope produces RWA USD 5,000,000 and teaching output USD 400,000.
No name, case ID or either amount selects a branch.

Money remains two decimal places and exact ratios have at most six effective fractional digits.
Insignificant trailing zeros do not introduce rounding. Multiplication uses an isolated sufficient
Decimal context; caller precision/rounding/exponent limits/traps/flags cannot change accepted results.
A teaching amount requiring fractional cents fails with ROUNDING_POLICY_UNDEFINED: no rounding rule
was approved. No magnitude cap was invented; inputs remain bounded by available runtime resources.

Only baseline_total_capital_equivalent is emitted. Warnings identify internal-prototype/educational use
and exclude allocated loan capital, economic capital, complete required regulatory capital,
institution-specific requirements and capital adequacy conclusions. No CET1/Tier 1 outputs.

## Evidence identity and applicability

The approved source manifest SHA-256 is
1a693c8acaee30642e7ff9ed02914296568d3f44fbe8884f96d224e4eddfa5ed.
Catalog snapshot: us-frb-internal-v1:activation-pr-4:a89eeb6.

The loader pins the manifest, reviewed v0.4 baseline, approved Golden Case and activation record;
all 71 capture byte lengths and SHA-256 hashes are checked. Authored JSON hashing normalizes only
CRLF to LF; raw official captures are never normalized. Each calculation rechecks the loaded package.
Only six approved rule scopes and their eight approved required dependencies supply executable
evidence. Whole captures, four conditional exclusions and two deferred groups are not blanket approval.

Source legal status and human review status remain distinct. The documentary manifest's top-level
executable=false is preserved: it is not itself executable software. Its scoped
approved_for_execution_evidence=true rules, exact pins, human approval and provider implementation
jointly authorize this narrow calculation. R-1888 remains PROPOSED/non-executable even if an
adversarial record tries to label it CURRENT, internally approved or a newer corporate rate.

Only 2025-01-01 succeeds. Earlier/later dates, unknown versions, aliases, unsupported perimeters,
ambiguous registrations, revoked approval, unapproved or modified evidence and non-CURRENT
lifecycle fail closed. Unknown effective endpoints stay UNKNOWN_NOT_OPEN_ENDED; there is no general
historical replay engine. A new final rule requires a separate reviewed version and code change.
Rule references retain locators, applicable date, rule version, reviewer/date and source citations.
Legacy supporting captures with no authority field retain null there; primary rule authority is
present, and original metadata/version evidence is preserved rather than invented.

## Trace and determinism

Steps are created while executing, not reconstructed from finished arithmetic:

1. Validate regulatory context.
2. Select the exact approved ruleset/version.
3. Verify source manifest, hashes and approval/lifecycle.
4. Validate institution/perimeter/CBLR facts.
5. Validate definition exclusions, treatment guards and accounting reconciliation.
6. Classify CORPORATE.
7. Resolve ordinary treatment.
8. Determine the complete typed exposure measure.
9. Determine the approved risk weight.
10. Calculate exact RWA from that measure and weight.
11. Calculate the sole educational equivalent.
12. Attach citations, warnings and exclusions.

Each step records sequence, ID, operation, reason, typed output, inputs_used references and warnings.
Regulatory steps carry immutable rule/version/locator/source evidence. Engine steps carry an engine
contract reference, not fabricated legal citations. Input references resolve to the supplied immutable
snapshot or preceding result objects; retain that snapshot with the result for a self-contained audit.

Canonical JSON uses sorted keys, compact UTF-8, plain exact decimals, ISO dates and ordered tuples.
Facts sort by unique path. Input hashing includes facts/provenance, context and schema/fixture
version; names and caller case/counterparty/institution/calculation IDs are excluded.
Authoritative result JSON excludes request_metadata by default; include_metadata=True is explicit.
The same authoritative inputs, package and version therefore reproduce the same trace and result.

RegulatoryError contains a stable code, field_path, message, rule_refs and immutable validation_trace.
A failed engine call returns no successful result envelope. Earlier valid intermediate steps may
remain in its diagnostic trace, including an RWA when only fractional-cent teaching output fails.
No excluded treatment or alternative financial conclusion is fabricated.

## Verification and limits

See REVIEW.md for exact observed commands/results and IMPLEMENTATION_RECORD.json for current
implementation status, separate from historical human activation approval.
The tests cover every required field and definition alternative, material scope failures, incompatible
typed measures/outputs, direct-provider evidence bypass, proposal tampering, all capture hashes,
16 hostile Decimal configurations, amount properties, name invariance and deterministic serialization.

This is internal synthetic education software, not legal/accounting certification or production-bank
sign-off. No source investigation, expanded rule corpus, new human approval, business API,
persistence, UI, tutor, other jurisdiction/class, portfolio aggregation or shared-core extraction
was performed. Final implementation acceptance and PR merge remain human decisions.
