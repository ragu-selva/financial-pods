# Sprint 02 Framework, Facts, and Calculation Contracts

Status: PLANNING ONLY — NOT ACTIVE

Architecture revision: 2026-09-08. Contracts below are proposed, not implemented.
Product direction is approved by the owner; regulatory sources, interpretations, facts, and expected
outputs still require personally named human review. No candidate value here is executable authority.

## 1. Separate conceptual authority from executable jurisdiction

**Conceptual authority:** [BCBS Basel Framework](https://www.bis.org/committees/bcbs/basel-framework)
provides the common Basel vocabulary, exposure concepts, RWA/capital concepts, and comparison layer.

**First executable jurisdiction:** United States, Federal Reserve, **12 CFR Part 217**.
The U.S. ruleset owns U.S. definitions, applicability, treatment, measurements, rates, and citations.
There is no automatic BCBS inheritance or numerical fallback. Later BCBS calculation support is a
separate explicitly labelled conceptual/educational provider, never an unlabelled domestic-law result.

This replaces the earlier BCBS-first candidate on this branch. Names such as Alpha Manufacturing,
a fixture ID, external-rating absence, or a BCBS SME sales threshold cannot choose U.S. treatment.

## 2. Candidate U.S. rule/source register

Research access date: 2026-09-08. These official Federal Reserve pages were read for planning.
Each entry has jurisdiction US, authority Board of Governors of the Federal Reserve System,
regulation 12 CFR Part 217, and review status PENDING; human reviewer, approval date, exact
effective interval, immutable source content/hash, and amendment-chain validation are NOT YET PINNED.

Canonical codification entry point:
[12 CFR Part 217](https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-217).
Direct eCFR section retrieval failed in this session; the Board's Federal Reserve Regulatory Service
(FRRS) provided readable primary-source text. Do not treat this access fallback as an approved
version snapshot. A reviewer must reconcile the chosen dated eCFR/GovInfo text and Federal Register
amendments before activation.

[FRRS Regulation Q index](https://www.federalreserve.gov/frrs/regulations/regulation-q-capital-adequacy-of-bank-holding-companies-savings-and-loan-holding-companies-and-state-member-banks.htm)
labels its compilation as amended effective July 1, 2026. That is compilation metadata, not proof
that every selected paragraph took effect that day or applied on the Golden Case date.

- **US-SCOPE:** [§ 217.1(c)](https://www.federalreserve.gov/frrs/regulations/section-2171-purpose-applicability-reservations-of-authority-and-timing.htm)
  and [§ 217.30](https://www.federalreserve.gov/frrs/regulations/section-21730-applicability.htm).
  Candidate use: establish the institution/regime perimeter before invoking this provider.
  Part 217 is not a universal rule for every U.S. institution. Propose synthetic FinBank as an
  in-scope Board-regulated state member bank using standardized treatment, without a CBLR election;
  this is a new assumption requiring approval, not an existing fixture fact.
- **US-CLASS / US-MEASURE:** [§ 217.2](https://www.federalreserve.gov/frrs/regulations/section-2172-definitions.htm),
  definitions of corporate exposure, carrying value, and exposure amount paragraph (1).
  Candidate use: test corporate exclusions and measure this ordinary on-balance-sheet loan using
  its eligible carrying value. Do not automatically subtract provisions or write-offs from the
  Sprint 01 outstanding principal. The accounting basis and already-reflected adjustments require review.
- **US-CORP-RW:** [§ 217.32(f)(1)](https://www.federalreserve.gov/frrs/regulations/section-21732-general-risk-weights.htm).
  The text inspected specifies 100% for ordinary corporate exposures subject to the exceptions in
  (f)(2)-(3). Those QCCP paths are excluded here. The separate past-due/nonaccrual treatment in
  § 217.32(k) must be screened out rather than silently using the ordinary corporate path.
- **US-RWA:** [§ 217.31(a)(1)-(2)](https://www.federalreserve.gov/frrs/regulations/section-21731-mechanics-for-calculating-risk-weighted-assets-for-general-credit-risk.htm).
  Candidate use: exposure measurement and exposure amount times applicable risk weight for this
  single-exposure RWA. No portfolio-total engine is implied.
- **US-TEACHING:** [§ 217.10(a)(1)(iii), with (a)(2) and (b) as context](https://www.federalreserve.gov/frrs/regulations/section-21710-minimum-capital-requirements.htm).
  Candidate use: an 8% baseline total-capital educational equivalent. Applying a ratio to one
  exposure's RWA is our teaching transformation, not a calculation of a bank's actual capital ratio
  or complete capital requirement. No capital numerator, adequacy test, buffers, or leverage output.

These locators are review candidates, not a finding that all legal prerequisites have been satisfied.
Approved rules must cite the specific U.S. version; BCBS citations may only be labelled conceptual
context, never the executable justification for a U.S. result.

### Proposal separation

The Board's [R-1888 proposal record](https://www.federalreserve.gov/apps/proposals/FR-2026-0008-01/details)
and [March 19, 2026 notice](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm)
identify a proposed standardized-approach revision.
The [proposal document](https://www.federalreserve.gov/aboutthefed/boardmeetings/files/npr-standardized-approach-20260319.pdf)
describes changing the corporate weight from 100% to 95%. Record it as PROPOSED/non-executable;
a comment deadline or publication does not make it a current approved rule. Recheck legal status
and subsequent final/effective amendments at activation. Do not silently replace candidate 100%
with 95%, and do not claim this research proves the absence of all subsequent amendments.

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
Source/version verification remains a human-review prerequisite, not production ingestion work.

## 4. Ruleset identity, status, and time

Draft family identifier: US_FRB_PART217_STANDARDIZED.
Example version pattern: US_FRB_PART217_STANDARDIZED@YYYY-MM-DD.vN (NOT an approved ID).
US_STANDARDIZED_CURRENT may be a display/discovery alias only; every request resolves and records
one exact immutable manifest/version/hash. Alias changes cannot change a replayed result.

Two independent dimensions:

- Legal lifecycle: CURRENT, PROPOSED, FUTURE, SUPERSEDED.
- Internal review: DRAFT, PENDING_REVIEW, APPROVED, REJECTED.

Normal execution requires APPROVED plus legal CURRENT for the explicitly requested as-of date,
matching jurisdiction/regulator/regime, effective interval, and verified manifest/hash. Zero or
multiple eligible versions are typed errors. PROPOSED and FUTURE versions never execute early.
SUPERSEDED versions are not live defaults; later controlled historical replay would need a separate
explicit policy. No such replay feature is implemented by this planning task.

Approved rule content and manifests are immutable. Legal-status transitions, revocations, and
supersession are append-only catalog events/new snapshots, not edits to prior evidence. Capture the
catalog snapshot and selection decision in the trace; no ambient current date affects calculation.

**Date decision pending:** the accepted Golden Case snapshot is 2025-01-01. Prefer preserving it
and obtaining an approved historical U.S. snapshot effective that day. Alternatively approve a new,
separately versioned current-dated fixture. Do not apply a July 2026 compilation as if it were proven
2025 law, silently re-date the original, or blend fact and source-retrieval dates.

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
  fail validation. The first fixture proposes zero days past due, performing=true, all adverse
  flags=false. Later adverse states are rejected as out of scope, not assigned invented rates.
- Amounts: original_principal, outstanding_balance, gaap_carrying_value, currency, accounting_basis,
  specific_provisions, partial_write_offs, credit_loss_allowance, and explicit reconciliation of
  accrued interest/fees/premium/discount and adjustments already reflected in carrying value.
  No double subtraction; positive/matching USD values and zero adjustments are proposed for the
  first fixture only. Nonzero adjustments require review and are outside the initial calculation path.
- Scope guards: collateral, guarantee, netting, credit_risk_mitigation, real_estate_exposure,
  retail_exposure, specialised_lending, and subordinated_exposure are explicitly assessed.
  None/false is an affirmative reviewed fact, never an omitted-field default.
- Classification evidence: a versioned screen must positively address the exclusions in the selected
  corporate definition, including sovereign/supranational, bank/credit-union/PSE/GSE, mortgage and
  construction variants, QCCP/cleared/default-fund, securitization/equity/unsettled, and policy-loan/
  separate-account/PPP categories. Derive checks from granular counterparty/instrument facts; do not
  accept an unsubstantiated caller-supplied exposure_class=CORPORATE as proof.

Proposed scope_assessments keys: sovereign_or_supranational, depository_or_foreign_bank_or_credit_union,
public_sector_entity, gse, residential_mortgage, presold_construction, statutory_multifamily, hvcre,
cleared_transaction, default_fund_contribution, securitization, equity, unsettled_transaction,
policy_loan, separate_account, ppp_loan. Each assessment contains outcome YES/NO/UNKNOWN, supporting
fact paths, and provenance; the first successful path requires evidenced NO for each exclusion.
Additional measurement guards require assessment of securities, OTC derivatives, repo-style/eligible
margin loans, and purchased-credit-deteriorated assets; these treatments are outside this first slice.
The reviewer must approve this proposed complete screen against the selected dated definition.
Unknown or absent assessments fail. Guards do not implement alternative exposure-class formulas.

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
- determine_exposure_amount(facts, treatment, context) -> ExposureMeasure
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

## 7. Calculation result — regulatory-calculation.v0.1-draft

Required successful-result fields:

- schema_version, jurisdiction, as_of_date, calculation_id, fixture_version, fact_schema_version;
- classification and regulatory_treatment;
- exposure_amount: exact money plus measurement_basis and rule_refs;
- risk_weight: exact decimal ratio with unit=RATIO and rule_refs;
- ead: explicit amount/basis mapping, as described below;
- rwa: exact money plus rule_refs;
- capital_teaching_outputs: ordered named amounts, ratio basis, references, warning/exclusion IDs;
- ruleset_id, ruleset_version, rule_versions, manifest_hash, catalog_snapshot_id;
- input_snapshot_hash, calculation_trace, source_citations, warnings, exclusions.

Money is plain decimal text paired with currency. Risk weight 100% is ratio "1.00"; 8% is "0.08".
Do not silently reinterpret existing Sprint 01 Percentage values (percentage points) as ratios.
Unit conversion belongs to an explicit tested boundary. No floating-point authoritative arithmetic.

**EAD contract decision proposed:** retain the generic ead slot with amount equal to exposure_amount
for this fully drawn ordinary U.S. standardized case, basis=US_STANDARDIZED_EXPOSURE_AMOUNT_ALIAS,
and a warning that this is a product-schema alias, not a separate advanced-approaches EAD estimate.
No PD/LGD, maturity model, CCF, or new formula. Human review must approve this mapping and its
terminology before activation. RWA uses the provider's cited exposure_amount, not an unexplained EAD.

First teaching output name proposed: baseline_total_capital_equivalent, carrying ratio "0.08".
The array can later support additional approved educational equivalents; no actual CET1/Tier 1
ratio, capital numerator, or adequacy determination is introduced. Reject unapproved output names.

Canonical JSON uses a documented key/order policy, ISO dates, exact decimals, stable ordered trace,
and SHA-256 over the normalized fact snapshot including provenance and fact versions. Define the
normalization and included/excluded metadata before activation; never hash a Python repr.
Presentation names are outside the computational snapshot; caller-supplied trace IDs cannot affect
financial results. Outputs carry enough provenance to reproduce the selected input/manifest.
Unknown/missing fields or versions fail; immutable versions change when semantics/naming change.

## 8. Golden Case: prove the generic engine

Existing approved facts: synthetic FinBank, synthetic Alpha Manufacturing, USD 10,000,000 original
term-loan principal, outstanding principal equal to original at 2025-01-01. Do not edit that fixture.

Proposed enrichment, all PENDING human approval: in-scope U.S./FRB standardized institution,
non-financial company borrower, ordinary fully drawn on-balance-sheet loan, no undrawn exposure,
performing with zero past-due days/nonaccrual, no excluded categories, no CRM, and reviewed
GAAP carrying value USD 10,000,000 with zero accounting adjustments and loss allowances.

**Conditional candidate outputs, NOT approved golden results:** only if that fact set and the
matching dated U.S. sources are approved, classification CORPORATE / GENERAL_CORPORATE;
exposure_amount USD 10,000,000; risk_weight ratio "1.00"; ead equal to exposure_amount under the
explicit alias; rwa USD 10,000,000; baseline_total_capital_equivalent USD 800,000.
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

Proposed trace schema: regulatory-trace.v0.1-draft, an immutable ordered sequence:

1. Select jurisdiction and institution/regime context.
2. Resolve exact approved U.S. provider/version/effective interval.
3. Validate material facts, provenance, and scope screens.
4. Classify exposure using U.S. predicates.
5. Resolve applicable corporate treatment and exclusions.
6. Determine cited exposure amount and explicit EAD alias.
7. Determine applicable risk weight.
8. Calculate RWA.
9. Calculate approved educational capital equivalent(s).
10. Attach source evidence, warnings, and exclusions; finalize hashes.

Each step contains step_id, sequence, operation, rule_id, rule_version, reason_code,
source_locator/source_refs, inputs_used, typed output, and warnings.
Non-regulatory steps use a versioned engine-contract reference, not a fabricated legal citation.
Regulatory steps must resolve to approved source records; multiple rule_refs are allowed.

Trace is produced with the computation from structured evidence, not reconstructed by an LLM.
Failed selection/validation returns a typed failure trace without a successful financial result.
No network lookup, clock, random ID generation, or provider side effect inside the deterministic core.

## 10. Unresolved activation decisions

- [ ] Personally name the human regulatory reviewer and record role, authority, acceptance, and process.
- [ ] Approve the U.S. institution/perimeter, including standardized versus other regimes/CBLR.
- [ ] Approve historical 2025-01-01 sources or a new dated fixture; capture exact versions, intervals,
  canonical snapshots/hashes, amendment references, and proposal-versus-effective status.
- [ ] Approve the full corporate exclusion-screen contract and rule interpretation.
- [ ] Approve Golden Case accounting/carrying-value reconciliation and all new negative facts.
- [ ] Approve classification, risk weight, EAD alias, RWA, teaching transformation, amounts, and exclusions.
- [ ] Approve fact/classification/result/trace schemas, ratio units, hash policy, and precision/errors.
- [ ] Approve lifecycle/revocation/replay policy and tests preventing proposed/future-rule execution.
- [ ] Approve the control pack and proposed ADR together; explicitly authorize Sprint 02 activation.

Until then: PLANNING ONLY — NOT ACTIVE. AI research is assistance, not regulatory sign-off.
