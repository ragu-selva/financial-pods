# Sprint 02 — Point-in-Time Source Review

Status: PLANNING ONLY — NOT ACTIVE

Review/capture date: 2026-09-08. Regulatory/fact as-of: **2025-01-01**, unchanged.
Source-side status: **BLOCKED_ON_SOURCE_EVIDENCE**. Internal review: **PENDING_REVIEW**.
This is documentary research, not regulatory approval, classification, calculation or activation.

## Resolved documentary evidence

### Preserved baseline and new evidence

All 11 raw captures from 4738841 remain unchanged, including their original hashes/retrieval
metadata and the isolated R-1888 record. The accepted Golden Case and ACTIVATION_RECORD.json
are unchanged. The existing planning branch/history is retained; nothing is merged into main.

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json), now source-review-manifest.v0.3-draft, adds:

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

There are **59 registered raw evidence files** in total (11 preserved + 48 new). Capturing a
whole document does not place every provision in scope. The six core candidate source IDs remain
unchanged; required dependency records are linked separately. No source is an executable allowlist.

Primary evidence locations:
[GovInfo annual CFR](https://www.govinfo.gov/content/pkg/CFR-2025-title12-vol2/xml/CFR-2025-title12-vol2-part217.xml),
[2019 carrying-value rule](https://www.govinfo.gov/content/pkg/FR-2019-02-14/html/2018-28281.htm),
[effective-date delay](https://www.govinfo.gov/content/pkg/FR-2019-03-29/html/2019-06011.htm),
[2019 simplifications](https://www.govinfo.gov/content/pkg/FR-2019-07-22/html/2019-15131.htm),
[2020 corporate correction](https://www.govinfo.gov/content/pkg/FR-2020-09-17/html/2020-17744.htm).
The manifest supplies all other URLs and local locators, not just these representative links.

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

### Minimal dependency inventory

These classifications are review candidates, conditional on approved facts—not a new executable
dependency registry. Every dependency has source IDs and an explicit scope in the manifest.

- **REQUIRED:** 217.12 election/grace-period screen; 217.202 covered-position definition;
  217.38(a)–(b) unsettled-transaction scope. The 217.32(k) past-due/nonaccrual screen is also
  required but is already inside the six captured sections.
- **SUPPORTING:** 217.22(b)(2) AOCI/measurement-exception context; 217.2 institution definitions
  and 217.1 timing, already captured. No BHC/SLHC threshold engine, capital deductions, or
  CBLR eligibility calculator is added.
- **NOT_REQUIRED_FOR_GOLDEN_CASE, conditional:** detailed 217.35 QCCP rates and 217.3 cleared
  transaction conditions if the outer CCP/cash-collateral predicate is demonstrably false;
  217.33–.37 CCF/derivative/CRM calculations; securitization/equity calculations; conditional
  real-estate statutory safe harbors where the outer category is demonstrably absent.
  The definitions, exception triggers and negative reasons are still required. Missing or
  positive facts must reject/defer the path, not silently select corporate.
- **UNRESOLVED:** incorporated depository-institution/foreign-bank/credit-union identity
  sources; the PPP statutory definition; necessary reporting/accounting dependencies and
  the complete covered-position definition/footnote chain. Details follow.

## Remaining human/legal-review items

1. **Close incorporated identity sources.** 217.2 points to FDIA section 3 / 12 USC 1813
   and Regulation K / 12 CFR 211.2. The relevant 2025 external chains are not independently
   captured/reconciled; the minimum credit-union identity authority also needs confirmation.
   A reviewer must either require and reconcile those exact dated sources or document why
   approved explicit synthetic negative facts make further incorporated detail unnecessary.
   A non-financial-company label or borrower name is not evidence closure.
2. **Close PPP incorporation.** The corporate definition's amendment is established, but
   the referenced 15 USC 636(a)(36) statutory version/chain is not independently established.
   Obtain the dated statute and applicable amendments if needed, or secure an evidenced,
   reviewed basis for excluding PPP without evaluating its subsidiary conditions.
3. **Close reporting/accounting and covered-position dependencies.** Dated 217.202 is
   captured, but its transitive/footnote lineage and required Call Report/FR Y-9C reporting
   definitions are not certified complete. Determine whether the synthetic case needs those
   exact dated instructions. Likewise approve the non-AFS/HTM/non-PCD measurement screen,
   GAAP carrying-value reconciliation and any relevant CECL adoption/transition facts.
4. **Approve the minimal fact/dependency boundary.** All fourteen corporate exclusions,
   the measurement exceptions, CBLR election/grace state, market-risk scope and QCCP/past-due
   triggers need accountable human review. Existing NO assessments are candidates, not legal
   findings. No facts were added or changed to make the source review pass.
5. **Approve date/lifecycle and interpretation.** Document why each cited paragraph version
   applies on 2025-01-01, with any institution-specific timing. Unknown end dates prohibit
   inferred future validity. Current text corroboration does not approve executable selection.
6. **Provide accountable human approval.** The owner must supply/approve the personally
   named reviewer, role/authority, responsibilities, date, decision and linked evidence.
   Sources, interpretations, assumptions, classification, risk weight, RWA, sole teaching
   output and exclusions require that review. All seven activation-record fields remain null.

Items 1–3 are specific remaining source-evidence/dependency questions, not merely absent signatures.
Official sources were reachable; no access failure is being claimed as the reason for this
remaining block. Further capture should follow the minimum dependency decision and preserve
this evidence, rather than refetch unchanged material or treat an unbounded legal corpus as reviewed.

## Hash and verification policy

Raw evidence is hashed over the complete stored response bytes with SHA-256. No HTML/XML,
newline, Unicode or whitespace normalization is applied to raw hashes. HTML in .source.txt is
inert evidence, not executable content. evidence/.gitattributes disables text conversion and
source whitespace checks; authored documents/tests still require formatting and whitespace checks.

Manifest v0.3 adds paragraph/binding interval semantics, dependency classifications and precise
gaps while retaining original source metadata, proposal evidence and interpretations. Final
approved manifest canonicalization/hash remains a separate contract decision.

The planning-evidence suite checks all registered raw files, proposal isolation, unknown-end
semantics, source/dependency links, inactive status and unchanged reviewer fields. The normal
repository suite validates the unchanged Sprint 00/01 software baseline, not a regulatory engine.
See [REVIEW.md](REVIEW.md) for commands, outcomes and limitations.

The effective-dated regulatory source resolver skill was used unchanged. Its selector tuple,
paragraph granularity, unknown-end and partial-manifest rules already cover the issues encountered;
no interpreter/calculator behavior was added to the skill.

## Activation readiness

**Source side: BLOCKED_ON_SOURCE_EVIDENCE**, not READY_FOR_HUMAN_REVIEW as a complete source pack.
The core documentary findings can be reviewed now, but the full minimum dependency set is not
closed. Resolution remains UNRESOLVED; approval and every review status remain PENDING_REVIEW;
every executable flag remains false.

R-1888 remains **PROPOSED**, executable=false, isolated from all 2025 source/rule/lineage/dependency
bindings. Neither an alias nor a future finalization may retroactively replace the 2025 evidence.

ACTIVATION_RECORD.json is byte-for-byte unchanged. No reviewer identity/approval/evidence was
invented. No activation PR was created. ADR 0004 remains PROPOSED. No production regulatory engine,
calculation, API, persistence, UI, or source-selection implementation was added.

SPRINT 02 REMAINS INACTIVE
