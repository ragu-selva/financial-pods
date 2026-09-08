# Sprint 02 Framework and Calculation Scope

Status: Candidate control document; not approved and not executable authority.

## Recommendation for approval

Use the current consolidated Basel Committee on Banking Supervision (BCBS) Basel Framework as a
canonical educational baseline, not as a domestic legal requirement. Pin the executable ruleset to a
reviewed source snapshot identified as `BCBS_BASEL_FRAMEWORK_SA_2026_08` and restrict it to one
performing, on-balance-sheet, unrated, non-SME general corporate exposure.

This recommendation follows the finalized project references, which consistently select the BCBS
Framework as the canonical concept layer and require domestic implementations to be separate,
versioned overlays. It also avoids treating legacy paragraph numbering in those references as current
authority.

## Candidate authority and source register

### Source S02-BCBS-CRE20

- Authority: Basel Committee on Banking Supervision
- Framework: Consolidated Basel Framework
- Module: CRE20, Standardised approach: individual exposures
- Jurisdiction: International canonical baseline; not a domestic implementation
- Status: Consolidated Basel Framework source; candidate snapshot pending reviewer approval
- Canonical URL: https://www.bis.org/basel_framework/chapter/CRE/20.htm
- Snapshot/version identifier: `BCBS_BASEL_FRAMEWORK_SA_2026_08`
- Retrieved: 2026-08-27
- Publication/effective metadata: must be captured from the approved current-version selector and
  retained with the source snapshot before activation; the rolling consolidated framework does not
  have one reliable document-wide publication date
- Candidate locators:
  - CRE20.1: standardised-approach RWA equals risk weight multiplied by exposure amount; exposures
    are risk-weighted net of specific provisions, including partial write-offs
  - CRE20.43 and Table 10 in the consolidated PDF snapshot downloaded by BIS on 2026-05-08:
    unrated corporate exposures in jurisdictions permitting external ratings receive a 100% risk
    weight, except qualifying corporate SMEs
- Required review: verify both locators, their status/effective metadata, and their applicability to
  the candidate facts immediately before activation

### Source S02-BCBS-RBC20

- Authority: Basel Committee on Banking Supervision
- Framework: Consolidated Basel Framework
- Module: RBC20, Calculation of minimum risk-based capital requirements
- Jurisdiction: International canonical baseline; not a domestic implementation
- Status: Current
- Canonical URL: https://www.bis.org/basel_framework/chapter/RBC/20.htm
- Effective date: 2023-01-01
- Last update shown by BCBS: 2020-11-26
- Retrieved: 2026-08-27
- Candidate locator: RBC20.1(3), total capital must be at least 8.0% of RWA
- Known future state: BCBS identifies a new RBC20 version effective 2028-01-01; it is outside this
  candidate snapshot and must not be selected implicitly
- Required review: approve use of 8% only as a narrowly labelled teaching relationship, excluding
  buffers, Pillar 2, floors, domestic adjustments, and any assertion about FinBank's adequacy

### Publication-status semantics

- Authority: Basel Committee on Banking Supervision
- URL: https://www.bis.org/bcbs/help/publ_statuses.htm
- Retrieved: 2026-08-27
- Use: interpret `Consolidated` as content integrated into the Basel Framework and `Current` as the
  latest final version in effect; store the source's own status rather than inferring it

## Reference-artifact trace

The following finalized, immutable project artifacts support the proposed boundary but do not replace
the official BCBS sources:

- Master Strategy Research and Implementation Blueprint: sections 5, 6, 10, 13, and 17
- V1 Technical and Functional Specification: sections 7, 8, 15, and 17
- Engineering, Deployment and Coding Playbook: sections 8, 9, 19, and 20
- Prudential Capital Change Assurance Final Implementation Plan: sections 4, 6, 7, 9, and 15
- Developer starter guidance: Regulatory Content Policy and Testing Strategy

The artifacts require official sources, versioned rules, deterministic calculations, exact citations,
golden and boundary tests, and human approval. Some artifact prose cites an older CRE20.17 corporate
rule. That legacy locator must not be copied into the executable current ruleset.

## Candidate Alpha Manufacturing facts

Sprint 01 facts remain unchanged:

- FinBank is synthetic.
- Alpha Manufacturing is synthetic.
- Original principal is USD 10,000,000.
- At the approved 2025-01-01 snapshot, outstanding principal is USD 10,000,000.

The following are new Sprint 02 assumptions and require explicit approval:

- The exposure is a performing on-balance-sheet loan and is not past due or defaulted.
- Specific provisions and partial write-offs are zero.
- The exposure is unsecured and no collateral, guarantee, netting, or other credit risk mitigation is
  recognised.
- Alpha Manufacturing has no eligible external rating for this ruleset and is therefore unrated from
  the bank's regulatory perspective.
- The candidate regime permits external ratings for regulatory purposes.
- Alpha Manufacturing is not a corporate SME. The fixture will support this with synthetic reported
  consolidated annual sales of EUR 60,000,000 for the most recent financial year and explicit
  date/provenance; EUR support is limited to this classification input.
- No sovereign risk-weight floor, supervisory uplift, or national discretion changes the candidate
  risk weight.

No assumption may be silently defaulted. Missing, conflicting, or out-of-scope data must produce a
typed error.

## Candidate deterministic result

Subject to regulatory-review approval:

1. Classification: general corporate, non-SME, performing, on-balance-sheet exposure.
2. Exposure amount: USD 10,000,000, because outstanding principal is USD 10,000,000 and specific
   provisions/partial write-offs are zero; no credit risk mitigation adjustment is in scope.
3. Risk weight: 100%, using the unrated-corporate path in CRE20.43 for a regime permitting external
   ratings, with the corporate-SME exception confirmed inapplicable.
4. RWA: USD 10,000,000 × 100% = USD 10,000,000 under CRE20.1.
5. Minimum-total-capital teaching relationship: USD 10,000,000 × 8% = USD 800,000 under RBC20.1(3).

The final value must be labelled `minimum_total_capital_teaching_amount`, not `required_capital`, and
must carry exclusions stating that it is not a complete legal or prudential capital requirement.

## Candidate rule and result contracts

Every rule version must include:

- stable rule and ruleset IDs;
- authority, framework, jurisdiction, status, publication/effective dates, snapshot/retrieval date,
  canonical URL, exact locator, source hash, applicability, and supersession fields;
- interpretation text and explicit inclusions/exclusions;
- reviewer identity/role, review status, review date, and review evidence;
- required inputs, typed output, stable reason codes, and linked golden/boundary tests.

Every calculation result must include:

- calculation/run ID and as-of date;
- fixture/schema/ruleset/rule versions and input snapshot hash;
- exact decimal inputs and outputs;
- ordered trace steps for classification, exposure amount, risk weight, RWA, and the teaching amount;
- source IDs/locators and reason codes for every rule-derived step;
- warnings/exclusions and deterministic serialization.

Rule records and golden expected outputs become immutable after approval. Corrections create a new
version; they do not rewrite prior evidence.

## Precision and error policy proposed for approval

- Use Decimal only; binary floating point is prohibited in authoritative calculations.
- Percentages use exact decimal ratios (`1.00` for 100%, `0.08` for 8%).
- Intermediate multiplication is exact and is not rounded.
- Monetary results must already satisfy the currency's approved minor-unit precision. If a future
  case produces excess precision, return a typed `ROUNDING_POLICY_UNDEFINED` error until a reviewed
  rounding rule is introduced; do not round implicitly.
- Stable errors cover missing facts, unsupported ruleset/status, ambiguous classification,
  out-of-scope treatment, source/reviewer not approved, and undefined rounding.
- A draft or unapproved rule is non-executable.

## Required tests

- Golden case proving the candidate result and full trace
- Boundaries immediately below, at, and above the EUR 50,000,000 corporate-SME sales threshold
- Missing/invalid rating status, sales, provisions, default/past-due state, ruleset, source, and review
  metadata
- Rejection of collateral, guarantee, off-balance-sheet, specialised-lending, domestic-overlay, and
  other excluded paths
- Decimal, serialization, determinism, input-hash, rule-version, and immutability regressions
- Properties including RWA equals exposure amount multiplied by risk weight and teaching amount
  equals RWA multiplied by the approved teaching ratio for valid in-scope inputs
- Dependency test proving the finance domain/rule packages remain free of web, database, Redis, and
  LLM/provider dependencies

## Activation decisions

All boxes must be resolved and approved together before code changes begin.

- [ ] Approve the consolidated BCBS Framework as a canonical educational baseline, not domestic law.
- [ ] Approve the exact CRE20 and RBC20 source snapshots, hashes, locators, statuses, and dates.
- [ ] Approve `BCBS_BASEL_FRAMEWORK_SA_2026_08` as the ruleset identifier.
- [ ] Approve the narrow unrated, non-SME, performing on-balance-sheet corporate path.
- [ ] Approve every new Alpha Manufacturing assumption, including EUR 60,000,000 annual sales.
- [ ] Approve 100% risk weight, USD 10,000,000 RWA, and USD 800,000 teaching amount as golden
  expected results.
- [ ] Approve the output label/exclusions and the no-implicit-rounding policy.
- [ ] Identify a personally named accountable regulatory reviewer with authority to approve the
  interpretation and expected results.
- [ ] Record the project-owner and regulatory-reviewer approval date and provenance.

## Stop conditions

Stop implementation and document the conflict if the current official source, a domestic rule, or
the accountable reviewer's interpretation differs from this candidate scope. Do not broaden the
sprint to resolve an excluded treatment.
