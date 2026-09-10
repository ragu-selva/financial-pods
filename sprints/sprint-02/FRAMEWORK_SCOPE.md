# Sprint 02 Framework, Facts, and Calculation Contracts

Status: ACTIVE

Activation date: 2026-09-10. Human decision: **APPROVED_FOR_INTERNAL_PROTOTYPE**.
Reviewer: **Ragunath Selvaraj — Project Owner / Internal Regulatory Reviewer**.
This is the owner's accountable internal-prototype approval, not independent legal counsel,
regulatory certification, production-bank sign-off or real-bank GAAP certification.

Sprint 02: **ACTIVE** on main through merged PR #4 at
`a89eeb60727c5f615514f75ecc27f57f19ec23cf`. The owner authorized the separate
`codex/sprint-02-us-corporate-engine` implementation branch. Implementation is present;
engineering verification and implementation PR review are recorded in REVIEW.md.
No automatic merge or broader regulatory scope is authorized.

The design contracts below preserve the approved activation-time scope and draft schema history.
GOLDEN_CASE_APPROVED.json and the source approval envelope remain unchanged authoritative inputs.
RUNTIME_CONTRACT.md finalizes the implemented regulatory-facts.v1, regulatory-classification.v1,
regulatory-calculation.v1 and regulatory-trace.v1 contracts. Draft examples below are not runtime
payloads; no old-draft compatibility or EAD alias is provided.

## 1. Separate conceptual authority from executable jurisdiction

**Conceptual authority:** [BCBS Basel Framework](https://www.bis.org/committees/bcbs/basel-framework)
provides the common Basel vocabulary, exposure concepts, RWA/capital concepts, and comparison layer.

**First executable jurisdiction:** United States, Federal Reserve, **12 CFR Part 217**.
The U.S. ruleset owns U.S. definitions, applicability, treatment, measurements, rates, and citations.
There is no automatic BCBS inheritance or numerical fallback. Later BCBS calculation support is a
separate explicitly labelled conceptual/educational provider, never an unlabelled domestic-law result.

This replaces the earlier BCBS-first candidate on this branch. Names such as Alpha Manufacturing,
a fixture ID, external-rating absence, or a BCBS SME sales threshold cannot choose U.S. treatment.

## 2. Approved narrow U.S. rule/source register

Evidence captured on 2026-09-08 for the fixed regulatory/fact date **2025-01-01**.
See [SOURCE_REVIEW.md](SOURCE_REVIEW.md) and [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json).
Raw dated eCFR XML for all six required sections, the GovInfo 2025 annual edition, eCFR version
metadata, two Federal Register source-chain documents, and separate R-1888 evidence are captured
and SHA-256 pinned. Raw captures remain non-executable documents. SOURCE_MANIFEST.json separately approves only the named rule/dependency scopes.

The dated eCFR API succeeded even though the browser-facing dated page did not. The GovInfo
annual-edition XML explicitly carries 2025-01-01 in its publication metadata. The six section
snapshots are the review baseline; FRRS 2026 pages below remain locator/context references only.
No 2026 compilation date proves 2025 applicability. The bounded amendment/LSA and material-source closure is complete and human-approved for 2025-01-01 only. Unknown endpoints remain unknown.

- **US-SCOPE:** [§ 217.1(c)](https://www.federalreserve.gov/frrs/regulations/section-2171-purpose-applicability-reservations-of-authority-and-timing.htm)
  and [§ 217.30](https://www.federalreserve.gov/frrs/regulations/section-21730-applicability.htm).
  Approved internal-prototype use: establish the institution/regime perimeter before invoking this provider.
  Part 217 is not a universal rule for every U.S. institution. Propose synthetic FinBank as an
  in-scope Board-regulated state member bank using standardized treatment, without a CBLR election;
  this is an approved separate synthetic assumption, not a modification of the Sprint 01 fixture.
- **US-CLASS / US-MEASURE:** [§ 217.2](https://www.federalreserve.gov/frrs/regulations/section-2172-definitions.htm),
  definitions of corporate exposure, carrying value, and exposure amount paragraph (1).
  Approved internal-prototype use: test corporate exclusions and measure this ordinary on-balance-sheet loan using
  its eligible carrying value. Do not automatically subtract provisions or write-offs from the
  Sprint 01 outstanding principal. The approved accounting reconciliation is in GOLDEN_CASE_APPROVED.json and MATERIAL_SOURCE_CLOSURE.md.
- **US-CORP-RW:** [§ 217.32(f)(1)](https://www.federalreserve.gov/frrs/regulations/section-21732-general-risk-weights.htm).
  The text inspected specifies 100% for ordinary corporate exposures subject to the exceptions in
  (f)(2)-(3). Those QCCP paths are excluded here. The separate past-due/nonaccrual treatment in
  § 217.32(k) must be screened out rather than silently using the ordinary corporate path.
- **US-RWA:** [§ 217.31(a)(1)-(2)](https://www.federalreserve.gov/frrs/regulations/section-21731-mechanics-for-calculating-risk-weighted-assets-for-general-credit-risk.htm).
  Approved internal-prototype use: exposure measurement and exposure amount times applicable risk weight for this
  single-exposure RWA. No portfolio-total engine is implied.
- **US-TEACHING:** [§ 217.10(a)(1)(iii), with (a)(2) and (b) as context](https://www.federalreserve.gov/frrs/regulations/section-21710-minimum-capital-requirements.htm).
  Approved internal-prototype use: an 8% baseline total-capital educational equivalent. Applying a ratio to one
  exposure's RWA is our teaching transformation, not a calculation of a bank's actual capital ratio
  or complete capital requirement. No capital numerator, adequacy test, buffers, or leverage output.

These locators are approved only within the bounded synthetic case; no broader legal certification is implied.
Approved rules must cite the specific U.S. version; BCBS citations may only be labelled conceptual
context, never the executable justification for a U.S. result.

### Proposal separation

The Board's [R-1888 proposal record](https://www.federalreserve.gov/apps/proposals/FR-2026-0008-01/details)
and [March 19, 2026 notice](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm)
identify a proposed standardized-approach revision.
The [proposal document](https://www.federalreserve.gov/aboutthefed/boardmeetings/files/npr-standardized-approach-20260319.pdf)
describes a corporate-weight revision. The separately captured proposal record links to the
March 27, 2026 Federal Register notice (document 2026-05960). Its manifest entry has
legal_status=PROPOSED and executable=false and is excluded from candidate calculation sources.
It never affects the 2025 case or a CURRENT alias. A subsequent final rule would require its own
independently sourced, versioned, effective-dated and human-approved record, selected for a matching
as-of date; never promote or mutate the proposal snapshot into executable authority.
Tests must reject the proposal even if requested directly, accidentally aliased as CURRENT, or
internally marked approved. See [PLANNED_TESTS.md](PLANNED_TESTS.md).

## 3. Source manifest and approval contract

Every eventual executable rule must have:

- rule_id, rule_version, ruleset_id, ruleset_version, and jurisdiction;
- authority, regulation, section/paragraph, canonical source URL and exact source locator;
- publication/version information, promulgating/amending Federal Register reference;
- effective_from, effective_to (explicitly open-ended when appropriate), legal status;
- retrieval date/time, snapshot identifier, content SHA-256, hash algorithm and normalization basis;
- interpretation, applicability predicates, exclusions, and linked reason codes/golden tests;
- personally named human reviewer, role/authority, review decision, review date, and evidence;
- separate conceptual references, if any, clearly distinguished from executable U.S. authority.

Missing source hashes or effective dates block approval; do not invent them or hash only a URL.
[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records observed hashes and source-version metadata.
The immutable v0.4 snapshot retains capture-time pending dates/statuses and paragraph lineages.
The v1 approval envelope records exact-date human applicability separately; null effective_to
continues to mean UNKNOWN_NOT_OPEN_ENDED, never infinite validity. Use only 2025-01-01.
Editorial dates do not become legal commencement dates. No production ingestion is implemented.

[ACTIVATION_RECORD.json](ACTIVATION_RECORD.json) provides the explicit accountable-human fields:
reviewer_name, reviewer_role, reviewer_qualification_or_authority, responsibilities_accepted,
review_date, review_decision, review_evidence. The project owner explicitly approved these values, including the personally confirmed reviewer name,
on 2026-09-10. AI transcribes the owner's decision; it cannot independently accept responsibility.
The linked immutable source/fact baseline and narrowly approved envelope supply the evidence.

## 4. Ruleset identity, status, and time

Approved family identifier: US_FRB_PART217_STANDARDIZED.
Approved evidence version: US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1.
US_STANDARDIZED_CURRENT may be a display/discovery alias only; every request resolves and records
one exact immutable manifest/version/hash. Alias changes cannot change a replayed result.

Two independent dimensions:

- Legal lifecycle: CURRENT, PROPOSED, FUTURE, SUPERSEDED.
- Internal review: DRAFT, PENDING_REVIEW, APPROVED, REJECTED.

Future execution must require APPROVED_FOR_INTERNAL_PROTOTYPE, an explicitly approved execution-evidence scope, and legal CURRENT **for the selected as-of date**,
matching jurisdiction/regulator/regime, the exact approved date (no inferred open interval), and verified manifest/hash.
Zero or multiple eligible versions are typed errors. The initial date is 2025-01-01, not today's date.
A source now labelled SUPERSEDED can only support that historical date through an explicitly
reviewed historical applicability record; it is never a live CURRENT default. This approved historical
selection policy permits only the pinned date, not broad replay functionality.
PROPOSED never executes; FUTURE cannot execute before its reviewed effective date, and a later
finalization requires a separately sourced final-rule version. No selector is implemented here.

Approved rule content and manifests are immutable. Legal-status transitions, revocations, and
supersession are append-only catalog events/new snapshots, not edits to prior evidence. Capture the
catalog snapshot and selection decision in the trace; no ambient current date affects calculation.

**Date decision fixed by the owner:** preserve the accepted Golden Case regulatory/fact snapshot
2025-01-01. Re-dating is not an activation alternative for Sprint 02. New regulatory enrichment
is separately versioned but retains that date and leaves the Sprint 01 fixture unchanged.
Only approved point-in-time U.S. authority applicable on that date may support this case.

## 5. Generic fact contract — regulatory-facts.v0.1-draft

A new versioned regulatory request/enrichment is planned; the existing Sprint 01 schema 1.0 and
fixture remain untouched. Every material input carries field-level provenance, assumption ID where
applicable, and explicit assessment status. This is not a dictionary of guessed optional booleans.

### Required for the proposed first corporate slice

- Context: jurisdiction, as_of_date, regulator, reporting_regime, institutional applicability facts,
  cblr_elected, exact requested ruleset version, fixture version and fact-schema version.
  Jurisdiction means the reporting regulatory regime, not a guess from borrower name or domicile.
- Identity: opaque institution/counterparty/facility/exposure IDs for traceability; display names
  live in presentation/fixture metadata, outside rule predicates.
- Economic facts: counterparty_type (company and type evidence), product_type, exposure_type,
  on_balance_sheet, off_balance_sheet, and explicit undrawn/contingent component assessment.
- Credit state: performing, defaulted, past_due, days_past_due, nonaccrual; contradictory combinations
  fail validation. The approved first fixture has zero days past due, performing=true, all adverse
  flags=false. Later adverse states are rejected as out of scope, not assigned invented rates.
- Amounts: original_principal, outstanding_balance, gaap_carrying_value, currency, accounting_basis,
  specific_provisions, partial_write_offs, credit_loss_allowance, and explicit reconciliation of
  accrued interest/fees/premium/discount and adjustments already reflected in carrying value.
  No double subtraction; positive/matching USD values and zero adjustments are approved for the
  first fixture only. Nonzero adjustments require review and are outside the initial calculation path.
- Initial product-scope guards: collateral, guarantee, netting, credit_risk_mitigation, security/
  derivative/commitment components and non-ordinary loan features are explicitly assessed.
  None/false is an expressly approved synthetic fact, never an omitted-field default.
  Product-scope rejection means UNSUPPORTED_EXPOSURE_SCOPE, not a different legal classification.
- Classification evidence: a versioned screen must positively address the exclusions in the selected
  corporate definition, including sovereign/supranational, bank/credit-union/PSE/GSE, mortgage and
  construction variants, QCCP/cleared/default-fund, securitization/equity/unsettled, and policy-loan/
  separate-account/PPP categories. Derive checks from granular counterparty/instrument facts; do not
  accept an unsubstantiated caller-supplied exposure_class=CORPORATE as proof.

### U.S.-authority classification screen

USStandardizedRuleset derives corporate status from the selected **2025 version of 12 CFR 217.2**
and applicable Part 217 treatment provisions. The captured definition first requires an exposure
to a company, then excludes the following numbered categories. Proposed screen keys map directly
to these paragraph numbers (not to a BCBS taxonomy):

1. Sovereign; BIS; ECB; European Commission; IMF; ESM; EFSF; MDB; depository institution;
   foreign bank; credit union; or PSE. Every named alternative is assessed, not merely a loose
   "sovereign/supranational" label.
2. GSE.
3. Residential mortgage exposure.
4. Pre-sold construction loan.
5. Statutory multifamily mortgage.
6. HVCRE exposure.
7. Cleared transaction.
8. Default fund contribution.
9. Securitization exposure.
10. Equity exposure.
11. Unsettled transaction.
12. Policy loan.
13. Separate account.
14. Paycheck Protection Program covered loan.

Each assessment records the exact definition paragraph, supporting fact paths, outcome
YES/NO/UNKNOWN, provenance, and review status. The approved NO assessments are recorded in GOLDEN_CASE_APPROVED.json; an unreviewed caller NO is not reviewed NO. All fourteen
need approved evidence for the first successful path; absent/unknown/conflicting material evidence
is a typed error. A positive exclusion prevents the ordinary corporate path but does not implement
the excluded class. Definitions and cross-references must be checked against the captured version.

Separate **treatment/measurement/product-scope** screens must cover § 217.30(b) covered positions;
§ 217.32(f)(2)-(3) QCCP exceptions; § 217.32(k) 90-days-past-due/nonaccrual;
§ 217.2 exposure amount (1) exceptions and carrying-value basis; and CRM/guarantee/netting.
The initial product path additionally accepts only a fully drawn, performing, zero-days-past-due,
non-defaulted ordinary loan. These narrower product restrictions are not new statutory corporate
exclusions. Future unsupported treatments must fail explicitly, not acquire a guessed risk weight.

Specialised lending, generic regulatory retail, BCBS SME, and BCBS external-rating categories
remain vocabulary/extension points. They MUST NOT independently set or veto U.S. corporate status.
Only an explicitly approved mapping to a selected U.S. rule could make such a concept an executable
U.S. predicate. A generic retail/specialised-lending flag alone is not a legal corporate exclusion.
Underlying mortgage/HVCRE or other facts may still trigger a cited U.S. exclusion.

### Extension points, not initial requirements

external_rating_status and annual_sales may be carried as explicitly sourced informational facts,
but are not selection thresholds for the proposed ordinary U.S. path. Remove the old mandatory
EUR 60 million sales assumption and BCBS SME threshold tests. Do not invent a U.S. SME treatment.

Later fact namespaces can cover banks, sovereigns, retail, mortgages, SME, default, special lending,
subordination, equity, off-balance-sheet commitments, and CRM. Versioned provider-required schemas
must distinguish NOT_REQUIRED, UNKNOWN, and an affirmative negative fact. No permissive arbitrary
extensions or silent dropping of material submitted facts; unknown schema fields fail closed.

### Validation errors

Proposed stable envelope: code, field_path, message, rule_refs, and validation_trace.
Examples: MISSING_REQUIRED_FACT, CONFLICTING_FACTS, UNSUPPORTED_EXPOSURE_SCOPE,
INSTITUTION_OUT_OF_SCOPE, UNKNOWN_RULESET, AMBIGUOUS_RULESET, RULESET_NOT_APPROVED,
RULESET_NOT_EFFECTIVE, RULESET_STATUS_NOT_EXECUTABLE, SOURCE_EVIDENCE_INCOMPLETE,
CURRENCY_MISMATCH, EXCESS_PRECISION, and ROUNDING_POLICY_UNDEFINED.
An error contains no successful classification or financial outputs. No zero/default fallback.

## 6. Provider and classification contracts

The generic orchestrator receives validated facts and a resolved provider. It owns call order,
boundary validation, deterministic serialization, hashes, and trace assembly, not jurisdiction logic.
The provider owns additional required facts, regulatory classification, treatment, and formulas.
No scattered jurisdiction if/else branches or borrower-name dispatch.

Conceptual interface only (no implementation in this revision):

- classify_exposure(facts, context) -> ClassificationResult
- resolve_treatment(classification, facts, context) -> RegulatoryTreatment
- determine_regulatory_exposure_measure(facts, treatment, context) -> RegulatoryExposureMeasure
- determine_risk_weight(facts, treatment, context) -> RiskWeight
- calculate_rwa(exposure_measure, risk_weight, context) -> RwaResult
- calculate_capital_teaching_outputs(rwa, context) -> TeachingOutput[]
- generate_trace(step_evidence, context) -> CalculationTrace

These refine the owner's conceptual methods to pass explicit prior results instead of silently
reclassifying/recomputing hidden facts. Providers are stateless; identical facts and approved
versions produce identical results. A generic classifier is a dispatcher/contract, not an
independent source of regulatory truth. Select the provider before invoking regulatory predicates.

Proposed classification schema: regulatory-classification.v0.1-draft.

```json
{
  "schema_version": "regulatory-classification.v0.1-draft",
  "jurisdiction": "US",
  "ruleset": "US_FRB_PART217_STANDARDIZED",
  "ruleset_version": "<approved immutable version>",
  "exposure_class": "CORPORATE",
  "subclass": "GENERAL_CORPORATE",
  "reason_codes": ["US_CORPORATE_DEFINITION_SATISFIED"],
  "rule_refs": ["<versioned US-CLASS reference>"],
  "warnings": []
}
```

Example shape only. GENERAL_CORPORATE is a product taxonomy label mapped to U.S. predicates, not
an invented statutory definition. Successful live outputs must contain actual approved references;
placeholder strings are invalid. Names are absent.

## 7. Calculation result — regulatory-calculation.v0.2-draft

Required successful-result fields:

- schema_version, jurisdiction, as_of_date, calculation_id, fixture_version, fact_schema_version;
- classification and regulatory_treatment;
- regulatory_exposure_measure: RegulatoryExposureMeasure, the single authoritative RWA measure;
- risk_weight: exact decimal ratio with unit=RATIO and rule_refs;
- rwa: exact money plus rule_refs;
- capital_teaching_outputs: ordered named amounts, ratio basis, references, warning/exclusion IDs;
- ruleset_id, ruleset_version, rule_versions, manifest_hash, catalog_snapshot_id;
- input_snapshot_hash, calculation_trace, source_citations, warnings, exclusions.

Money is plain decimal text paired with currency. Risk weight 100% is ratio "1.00"; 8% is "0.08".
Do not silently reinterpret existing Sprint 01 Percentage values (percentage points) as ratios.
Unit conversion belongs to an explicit tested boundary. No floating-point authoritative arithmetic.

### RegulatoryExposureMeasure — regulatory-exposure-measure.v0.1-draft

Typed fields: amount, currency, measure_type, measurement_basis, rule_refs, warnings.

```json
{
  "amount": "10000000.00",
  "currency": "USD",
  "measure_type": "EXPOSURE_AMOUNT",
  "measurement_basis": "US_STANDARDIZED_CARRYING_VALUE",
  "rule_refs": ["US-MEASURE"],
  "warnings": []
}
```

This is an approved expected shape, not an executed result. Rule references must resolve to approved
versioned evidence in a live result. The U.S. slice fixes measure_type=EXPOSURE_AMOUNT and
measurement_basis=US_STANDARDIZED_CARRYING_VALUE. RWA consumes this typed measure and the cited
risk weight. There is no top-level ead field or duplicated authoritative exposure_amount field,
and no EAD label, alias, or conversion is permitted. The old v0.1 result proposal is superseded.

The generic measure discriminator may later admit EAD only when a separate approved provider
actually defines and requires it, with its own measurement basis, rules and tests. This is not
a second implemented variant in Sprint 02. Incompatible type/basis/provider combinations fail.

Exactly one Sprint 02 teaching output: baseline_total_capital_equivalent at ratio "0.08".
No CET1 or Tier 1 educational equivalents in this sprint; those require separate Golden Lesson/
UX-phase review. The 8% transformation is educational, based on the minimum total-capital ratio;
it is not allocated capital for a loan, an institution-specific capital requirement, or a capital
adequacy conclusion. It does not compute a capital numerator or actual bank ratio.
Unknown/additional teaching names must fail the initial provider contract.

Canonical JSON uses a documented key/order policy, ISO dates, exact decimals, stable ordered trace,
and SHA-256 over the normalized fact snapshot including provenance and fact versions. SOURCE_MANIFEST.json records the approved hash/design policy; implement and test it before runtime acceptance. Never hash a Python repr.
Presentation names are outside the computational snapshot; caller-supplied trace IDs cannot affect
financial results. Outputs carry enough provenance to reproduce the selected input/manifest.
Unknown/missing fields or versions fail; immutable versions change when semantics/naming change.

## 8. Golden Case: prove the generic engine

Existing approved facts: synthetic FinBank, synthetic Alpha Manufacturing, USD 10,000,000 original
term-loan principal, outstanding principal equal to original at 2025-01-01. Do not edit that fixture.

Approved separate enrichment: the synthetic FRB state member bank has not elected CBLR;
ordinary fully drawn on-balance-sheet non-financial corporate loan; all fourteen definition
exclusions and treatment negatives accepted; performing, past_due=false, days_past_due=0,
nonaccrual=false, CRM none. GAAP carrying value is USD 10m under the explicitly accepted zero
adjustments/allowance and non-PCD assumptions. No real-loan GAAP or CECL certification.
[GOLDEN_CASE_APPROVED.json](GOLDEN_CASE_APPROVED.json) governs; the candidate and source-boundary
files remain unchanged historical inputs. The accepted Sprint 01 fixture is not edited.

**Approved internal-prototype expected outputs, NOT executed results:** classification CORPORATE / GENERAL_CORPORATE;
regulatory_exposure_measure amount USD 10,000,000, type EXPOSURE_AMOUNT, basis
US_STANDARDIZED_CARRYING_VALUE; risk_weight ratio "1.00"; rwa USD 10,000,000;
baseline_total_capital_equivalent USD 800,000 at ratio "0.08". No EAD output.
RWA follows US-RWA and the educational equivalent follows US-TEACHING plus a clearly labelled
product transformation. Numerical coincidence with the old BCBS example does not transfer authority.

Required exclusions: single-exposure education only; no complete regulatory capital requirement,
bank capital adequacy conclusion, actual capital ratio, buffers, stress/Pillar 2, leverage, capital
composition/deductions, portfolio totals, other institutions/regimes, CRM, or out-of-scope treatments.

Tests must change borrower names and case IDs without changing classification, treatment, rates,
or numeric outputs. Identity-bearing trace metadata may differ. A second synthetic ordinary
corporate fixture with a different amount must run through identical orchestration. Bank, retail,
mortgage, SME, sovereign, and defaulted fixtures remain later scope, not successful current cases.

## 9. First-class calculation / regulatory trace

Proposed trace schema: regulatory-trace.v0.2-draft, an immutable ordered sequence:

1. Select jurisdiction and institution/regime context.
2. Resolve exact approved U.S. provider/version/effective interval.
3. Validate material facts, provenance, and scope screens.
4. Classify exposure using U.S. predicates.
5. Resolve applicable corporate treatment and exclusions.
6. Emit RegulatoryExposureMeasure: EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE.
7. Determine applicable risk weight.
8. Calculate RWA.
9. Emit only baseline_total_capital_equivalent at ratio 0.08.
10. Attach source evidence, warnings, and exclusions; finalize hashes.

Each step contains step_id, sequence, operation, rule_id, rule_version, reason_code,
source_locator/source_refs, inputs_used, typed output, and warnings.
Non-regulatory steps use a versioned engine-contract reference, not a fabricated legal citation.
Regulatory steps must resolve to approved source records; multiple rule_refs are allowed.
Step 6 typed output contains all six measure fields (amount/currency/type/basis/refs/warnings).
Step 8 inputs_used names regulatory_exposure_measure and risk_weight, not ead or an alias.
The trace preserves the measure discriminator and basis, the fixed 2025-01-01 selection date,
the exact manifest and source versions, and the proposal-exclusion decision.
[PLANNED_TESTS.md](PLANNED_TESTS.md) defines negative/schema/trace and later runtime test vectors.

Trace is produced with the computation from structured evidence, not reconstructed by an LLM.
Failed selection/validation returns a typed failure trace without a successful financial result.
No network lookup, clock, random ID generation, or provider side effect inside the deterministic core.

## 10. Activation decision and remaining implementation gates

Human/source/Golden gates are complete for the internal prototype; see ACTIVATION_RECORD.json.
The source envelope pins six rule scopes, eight resolved dependencies and exactly 2025-01-01.
No required source dependency remains unresolved. ADR 0004 is ACCEPTED.

Still NOT IMPLEMENTED: runtime facts/classifier/registry/provider, schema finalization, canonical
serialization/input hashing, typed arithmetic/errors, source selection, trace and all runtime tests.
Implement inside the existing pure finance-engine boundary only after the activation PR is reviewed
and merged, on codex/sprint-02-us-corporate-engine. Do not add a service or extract another repository.
Changed material facts or dates require re-review; future classes/providers remain out of scope.
Sprint 02: ACTIVE. Implementation: NOT YET STARTED.
