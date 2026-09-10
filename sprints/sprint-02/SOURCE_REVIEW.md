# Sprint 02 — Point-in-Time Source Review

Status: ACTIVE

Activation date: 2026-09-10. Human decision: **APPROVED_FOR_INTERNAL_PROTOTYPE**.
Reviewer: **Ragunath Selvaraj — Project Owner / Internal Regulatory Reviewer**.
This is the owner's accountable internal-prototype approval, not independent legal counsel,
regulatory certification, production-bank sign-off or real-bank GAAP certification.

Sprint 02: **ACTIVE** on main after PR #4 merged at a89eeb6. The separate narrow implementation
is now present for review; see REVIEW.md and IMPLEMENTATION_RECORD.json. No automatic merge.
The approved source boundary and historical documentary review below are unchanged.

## Current approved boundary

Source-side status: **APPROVED_FOR_INTERNAL_PROTOTYPE**.
The owner approved the exact 2025-01-01 U.S./FRB/US_FRB_PART217_STANDARDIZED source boundary,
interpretations, corporate classification and Golden expectations. See
[ACTIVATION_RECORD.json](ACTIVATION_RECORD.json), [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json)
and [GOLDEN_CASE_APPROVED.json](GOLDEN_CASE_APPROVED.json).

The approval envelope pins [SOURCE_MANIFEST.reviewed-v0.4.json](SOURCE_MANIFEST.reviewed-v0.4.json);
that historical manifest retains every capture-time field, raw hash, retrieval date, amendment
reference and paragraph lineage unchanged. Only six named rule scopes and eight required dependency
scopes become approved execution evidence. Four deeper conditional dependencies remain
NOT_REQUIRED_FOR_GOLDEN_CASE; two groups remain DEFERRED_FUTURE_SCOPE. There are zero
REQUIRED_BUT_UNRESOLVED items. Retaining 71 captures is an audit requirement, not blanket approval.

The date permission is exactly 2025-01-01. UNKNOWN_NOT_OPEN_ENDED remains unchanged; neither an
infinite interval nor permission for another as-of date is inferred. Changed/missing material facts
require re-review. R-1888 remains PROPOSED / executable=false, never 2025 authority.

The reviewer expressly accepts the synthetic USD 10m carrying value, zero allowance/write-offs/
premium/discount/accrued-interest/fee adjustments, PCD=false, CRM=none, past_due=false and
nonaccrual=false. Zero allowance is not inferred from performing status; no CECL estimate or
arbitrary real-loan accounting treatment is approved. All fourteen corporate exclusions and
the outer measurement/treatment negatives are accepted for this fact set only.

Approved expectations are CORPORATE, EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE USD 10m,
risk weight 1.00, RWA USD 10m, and only baseline_total_capital_equivalent at 0.08 / USD 800k.
The last output is educational, not allocated loan capital, economic capital, a complete required
capital amount, institution-specific requirement or capital adequacy conclusion. These are
human-approved expected values, not executed or runtime-verified results.

## Historical documentary assessment — preserved, not current control

The following assessment is retained from planning commit
79b33dbb1f069a89fc6d87336a23268adea08589. Its pending-review/inactive wording describes the
pre-approval state. The approval record and current boundary above supersede that status only;
the evidence findings and limitations are not rewritten. Historical candidate filenames below
remain immutable inputs; GOLDEN_CASE_APPROVED.json is the current approved representation.

Status: PLANNING ONLY — NOT ACTIVE

Review update: 2026-09-10. Captures retain their individual retrieval dates. Regulatory/fact as-of: **2025-01-01**, unchanged.
Source-side status: **READY_FOR_HUMAN_REVIEW**. Internal review: **PENDING_REVIEW**.
This is documentary research, not regulatory approval, classification, calculation or activation.

## Resolved documentary evidence

### Preserved earlier source-chain evidence (2026-09-08)

All 11 raw captures from 4738841 remain unchanged, including their original hashes/retrieval
metadata and the isolated R-1888 record. The unchanged Golden Case candidate and ACTIVATION_RECORD.json
are unchanged. The existing planning branch/history is retained; nothing is merged into main.

The prior source-review-manifest.v0.3-draft source-chain follow-up added:

- 12 official December cumulative **Title 12** LSA captures, 2013–2024. Chapter II amendment
  entries are distinguished from the separate proposed-rule lists. These are edition labels,
  not inferred publication days.
- 30 missing Federal Register final/interim-final/correction/delay/transition documents.
  Every record includes the official URL, raw-byte SHA-256, byte count, publication date,
  stated DATES clause where present, and documentary purpose. Source IDs identify the documents.
- Two official FederalRegister.gov discovery-index responses: 56 RULE results and zero CORRECT
  results. Some correction documents are typed RULE. The zero-hit query does **not** prove an
  absence of corrections. The 1997/2011 demand-deposit Regulation Q results are a different
  regulatory regime and are excluded, notwithstanding the same Part 217 number.
- Four additional dated eCFR sections: **217.12**, **217.202**, **217.38**, and **217.22**.
  The first three support required scope screens; .22 is supporting measurement-exception context,
  not authority to implement a capital-deduction engine.

That follow-up produced **59 registered raw evidence files** (11 original + 48 added). Capturing a
whole document does not place every provision in scope. The six core candidate source IDs remain
unchanged; required dependency records are linked separately. No source is an executable allowlist.

Primary evidence locations:
[GovInfo annual CFR](https://www.govinfo.gov/content/pkg/CFR-2025-title12-vol2/xml/CFR-2025-title12-vol2-part217.xml),
[2019 carrying-value rule](https://www.govinfo.gov/content/pkg/FR-2019-02-14/html/2018-28281.htm),
[effective-date delay](https://www.govinfo.gov/content/pkg/FR-2019-03-29/html/2019-06011.htm),
[2019 simplifications](https://www.govinfo.gov/content/pkg/FR-2019-07-22/html/2019-15131.htm),
[2020 corporate correction](https://www.govinfo.gov/content/pkg/FR-2020-09-17/html/2020-17744.htm).
The manifest supplies all other URLs and local locators, not just these representative links.

### Current minimum material closure (2026-09-10)

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json), now **v0.4-draft**, retains all 59 earlier captures
and adds **12** official captures, for **71** registered raw files. These are four U.S. Code
section editions, two dated Regulation K renditions, two FDIC historical indexes and four
reporting-component/update PDFs. No earlier raw evidence, Golden output or activation field changed.

Earlier source records retain their original capture-time metadata, including pending-chain
observations. The current narrow assessment is in material_closure and dependency_inventory;
historical capture observations are not new unresolved material dependencies. Whole-interval
and human approval remain pending.

[MATERIAL_SOURCE_CLOSURE.md](MATERIAL_SOURCE_CLOSURE.md) records the four resolved documentary
gaps, source locators, dated reconciliation, exact factual boundary and limitations.
[GOLDEN_CASE_SOURCE_BOUNDARY.json](GOLDEN_CASE_SOURCE_BOUNDARY.json) supplies explicit proposed
synthetic facts for human review; it does not overwrite the original candidate/accepted fixture.

- Identity: FDIA 1813 bank/savings-association definitions, Regulation K 211.2(j), credit-union
  identity under 1752, and existing PSE/GSE/sovereign/MDB definitions, paired with explicit
  domestic private manufacturing/non-bank/non-cooperative/non-public facts.
- PPP: 636(a)(36)(A)(ii)-(iii), with 2023/2024 edition reconciliation and explicit non-program
  origination facts. A 2025 snapshot alone cannot prove a loan is non-PPP.
- Accounting: dated amortized-cost components, HFI/allowance/net balance and acquired-PCD gate;
  explicit zero adjustments and measurement exceptions. Zero allowance remains a proposed
  synthetic simplification requiring human acceptance, not a verified CECL result.
- Market risk: dated covered-position outer predicates, footnotes and trading instructions,
  paired with explicit non-trading/non-hedge/non-FX/non-commodity facts.

The 2024 Code edition includes laws through January 6, 2025. Selected-definition amendment notes
and PPP edition comparison reconcile that cutoff to January 1; the edition label is not treated
as a point-in-time guarantee. All 58 Regulation K direct paragraphs agree with annual CFR.

The full FFIEC December PDF's direct download returned 403/CAPTCHA; the required raw passages
were obtained from the official FDIC historical components plus December replacement list.
No access challenge was bypassed, no error page was retained, and no complete reporting-book
or accounting-standard review is claimed. Source collection has stopped at the narrow boundary.

### Paragraph lineage and date semantics

The following are **documented text-version commencement candidates**, not approved regulatory
applicability intervals. Current paragraph text is corroborated at 2025-01-01. For each candidate,
effective_to remains null with **UNKNOWN_NOT_OPEN_ENDED**. This means the legal end was not
established; it does not mean valid forever. documentary_coverage_through is an observation
bound, not a fabricated expiry date. No eligibility after 2025-01-01 is established.

- **Institution perimeter — 217.1(c)(1)(i)(A): 2024-01-01.** The 2013 Board adoption listed
  state member banks at (c)(1)(i). The 2023 insurance rule, instruction 2, rewrote (c)(1) and
  placed that limb at (c)(1)(i)(A), effective January 1, 2024. Intervening SLHC changes in
  2015/2018 do not change the state-member-bank limb. State bank, state member bank and
  Board-regulated institution are defined in the captured 217.2 text. No synthetic-bank
  charter/perimeter finding is approved.
- **Corporate definition — 217.2: composite current text from 2020-04-13.** The 2013 common
  definition plus Board instruction 46 supplied thirteen exclusions. Instruction 26 of
  2019-15131 revised the definition effective October 1, 2019, including the European
  Stability Mechanism / European Financial Stability Facility in (1). Instruction 7 of
  2020-07712 added PPP exclusion (14) and revised (12)–(13) punctuation effective April 13, 2020. Final rule 2020-21894 adopted the interim rule without change effective December 28, 2020. That finalization does not erase the April commencement. The current opening and
  (1)–(11) date from 2019-10-01; (12)–(14) from 2020-04-13.
- **Carrying value — 217.2: 2019-07-01 general commencement.** The CECL final rule
  2018-28281 revised this definition and originally specified April 1, 2019. The March 29
  delay, 2019-06011, replaced that date with July 1, 2019 while preserving optional early
  adoption. Earlier institution-specific adoption needs evidence; neither February publication
  nor April's superseded scheduled date is the selected general commencement.
- **Exposure amount — 217.2 definition (1): 2014-01-01 legal commencement, separate
  standardized compliance timing.** The ordinary on-balance-sheet carrying-value limb is
  in the 2013 adopted text. The relevant later definition-amendment instructions do not rewrite
  this limb. The 2020 SA-CCR final rule changed other definitions and treatment provisions, not
  this definition. Its enumerated exceptions still require a reviewed negative screen.
- **Corporate risk weight — 217.32(f)(1): 2020-09-17 current wording.** The 2013 (f) contained
  100%. The SA-CCR rule 2019-27249 rewrote (f), effective April 1, 2020, adding QCCP
  cash-collateral exceptions. Correction 2020-17744, instruction 9, fixed (f)(1) to refer to
  both (f)(2) and (f)(3); 100% did not change. Notification 2020-06755 allowed optional
  best-efforts early adoption, while expressly retaining April 1 effectiveness and January 1,
  2022 mandatory SA-CCR compliance for advanced-approaches organizations. That methodology
  compliance date is not the start of ordinary corporate treatment.
- **Standardized scope and RWA — 217.30(a)–(b), 217.31(a)(1)–(2): 2014-01-01 legal
  commencement.** These appear in the founding rule and Board adoption. No subsequent targeted
  amendment was identified in the captured 2013–2024 LSA chain. The 2017 eCFR baseline is not
  their original effective date. Institution-specific and standardized compliance timing remain
  separate from the rule's effective date.
- **8% teaching source — 217.10(a)(1)(iii): 2020-01-01 current locator.** The original 8%
  minimum was at (a)(3). CBLR rule 2019-23472, instruction 39, rewrote (a), retained 8% at
  (a)(1)(iii), and added the CBLR exception at (a)(2). Corrections 2019-27717 and
  C1-2019-23472 concern other provisions. This is a bank-level minimum-ratio source; multiplying
  a single loan's RWA by 8% is a proposed educational transformation, not a statutory allocated
  loan-capital requirement or a complete bank-specific requirement.
- **Past-due screen — 217.32(k): 2019-10-01 current version.** Instruction 32 of
  2019-15131 revised (k). Review must explicitly cover 90-or-more days past due **or**
  nonaccrual; a generic performing/defaulted label is insufficient. No defaulted-exposure
  calculation is authorized.
- **CBLR election — 217.12(a)(1), (a)(3), (c): 2020-01-01.** Rule 2019-23472 added
  the framework, opt-in/opt-out, and grace-period conditions. The later temporary threshold
  provision 217.12(a)(4), added by 2020-26138, expressly applied December 2, 2020 through
  December 31, 2021. Its evidenced exclusive end is **2022-01-01**, not null. Its text remains
  printed in 2025, but its relief is expired. The separate temporary CBLR ratio transition
  confirmed in 2020-19922 is not a source for the educational 8% total-capital figure.

The founding final rule's DATES clause specifies January 1, 2014 effectiveness and distinguishes
mandatory compliance for advanced-approaches non-SLHC organizations from other covered organizations
(January 1, 2015). Section 217.1(f) separately contains 2014 substitution/transition provisions
and January 2015 standardized-RWA commencement. Those distinctions must survive any future selector.
The 2023 rule's reporting/submission dates likewise do not replace its January 1, 2024 effectiveness.

### Amendment and definition review boundaries

The manifest's paragraph_lineage, definition_review and amendment_chain_screen record the
paragraphs, exact documents, dates, limitations and PENDING_REVIEW status. The first six sections
are **not** assigned blanket effective dates.

The core definition review covers Board/state-member-bank identity, company, GAAP, corporate
exposure, carrying value and exposure amount (1). Conditional screen definitions include
sovereign/MDB/GSE/PSE, residential mortgage, pre-sold construction, statutory multifamily, HVCRE,
cleared transactions, default funds, securitization, equity, policy loans and separate accounts.
The 2015 residential-mortgage revision and 2020 HVCRE definition are identified; HVCRE's
origination/reclassification transitions are not silently disregarded. QFC-related 2014 interim
and 2017 final amendments to collateral/netting/margin/repo definitions are retained for the
conditional measurement screen. This is not a review of every 217.2 definition.

The LSA 2015 text places some 49103 entries under 217.10 even though actual 2015-18702
instructions 9–10 amend 217.11. Direct amendatory instructions, not this index labeling,
determine the paragraph target. The six core eCFR/annual-CFR direct paragraph sequences had
zero non-whitespace differences in the previous diagnostic comparison. Newly captured dependency
sections are checked in the same way in this follow-up. This is text corroboration, not proof
of legal equivalence or transitive cross-reference closure.

### Final minimum dependency inventory

Every dependency uses an owner-requested label, with source IDs, scope and fact-group references:

- REQUIRED_AND_RESOLVED: **8** — institution, CBLR, external identity, PPP, accounting,
  covered position, unsettled-transaction scope and past-due/nonaccrual.
- REQUIRED_BUT_UNRESOLVED: **0** for the explicit 2025-01-01 internal-prototype boundary.
- NOT_REQUIRED_FOR_GOLDEN_CASE: **4** — downstream AOCI, QCCP, CRM/derivatives and other-class
  conditional treatments. Their outer negative screens remain required and documented.
- DEFERRED_FUTURE_SCOPE: **2 groups** — full positive-treatment/accounting/eligibility engines
  and other dates/jurisdictions, including full legal interval endpoints.

These labels describe documentary readiness, not approved legal/factual findings. Missing,
contradictory or changed facts, or reviewer rejection, reopen the relevant dependency.
Detailed incorporated statutes behind demonstrably absent outer categories are not required.
Neither full Part 217 review nor a broad bank/PPP/CECL/market-risk engine is authorized.

## Remaining human/legal-review items

1. Approve the exact dated source versions, selected locators and interpretations, including the
   minimum boundary rather than every provision in a captured document.
2. Accept or reject every proposed synthetic fact. Specifically review non-institutional and
   non-PPP provenance, CBLR never-election/grace status, measurement and market-risk exclusions.
3. Approve the itemized accounting reconciliation and zero-allowance educational simplification.
   Performing status does not justify zero expected credit loss. Gross amortized cost, net GAAP
   balance and Part 217 carrying value are distinct; no real-loan GAAP compliance is certified.
4. Independently approve classification, 100% weight, USD 10m RWA and sole 8%/USD 800k educational
   output and limitations. Source and planning tests do not verify these regulatory conclusions.
5. Personally complete reviewer identity/authority, responsibilities, date, decision and linked
   evidence. The owner agreed to act as accountable prototype reviewer, but no final approval
   or identity fields were populated. All seven activation fields remain null.
6. Approve final executable version/hash/trace/selector contracts and activation separately.
   Unknown legal endpoints remain unknown, not open-ended; no future-date validity is inferred.

No material documentary gap remains under the explicit candidate boundary. These remaining
items are human acceptance/interpretation and future implementation-contract gates, not an
instruction to expand the legal corpus. A rejected assumption reopens its dependency.

## Hash and verification policy

Raw evidence is hashed over the complete stored response bytes with SHA-256. No HTML/XML,
newline, Unicode or whitespace normalization is applied to raw hashes. HTML in .source.txt is
inert evidence, not executable content. evidence/.gitattributes disables text conversion and
source whitespace checks; authored documents/tests still require formatting and whitespace checks.

Manifest v0.4 adds the bounded source closure and four-way dependency labels while retaining
the earlier raw source metadata, proposal evidence, rule interpretations and unknown-end semantics. Final
approved manifest canonicalization/hash remains a separate contract decision.

The planning-evidence suite checks all registered raw files, proposal isolation, unknown-end
semantics, source/dependency links, inactive status and unchanged reviewer fields. The normal
repository suite validates the unchanged Sprint 00/01 software baseline, not a regulatory engine.
See [REVIEW.md](REVIEW.md) for commands, outcomes and limitations.

The effective-dated regulatory source resolver skill was used unchanged. Its selector tuple,
paragraph granularity, unknown-end and partial-manifest rules already cover the issues encountered;
no interpreter/calculator behavior was added to the skill.

## Activation readiness

**Source side: READY_FOR_HUMAN_REVIEW**. The previous BLOCKED_ON_SOURCE_EVIDENCE status is
superseded only for the documented narrow Golden Case. Resolution is RESOLVED_FOR_NARROW_GOLDEN_CASE;
approval and every review status remain PENDING_REVIEW and every executable flag remains false.
This is not APPROVED, approved GAAP accounting, a complete Part 217 corpus or activation.

R-1888 remains **PROPOSED**, executable=false, isolated from all 2025 source/rule/lineage/dependency
bindings. Neither an alias nor a future finalization may retroactively replace the 2025 evidence.

ACTIVATION_RECORD.json is byte-for-byte unchanged. No reviewer identity/approval/evidence was
invented. No activation PR was created. ADR 0004 remains PROPOSED. No production regulatory engine,
calculation, API, persistence, UI, or source-selection implementation was added.

SPRINT 02 REMAINS INACTIVE
