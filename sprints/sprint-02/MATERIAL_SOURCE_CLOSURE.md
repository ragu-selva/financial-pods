# Sprint 02 — Minimum Golden Case Source Closure

Status: PLANNING ONLY — NOT ACTIVE

Assessment: 2026-09-10. Source-side readiness: **READY_FOR_HUMAN_REVIEW**.
Jurisdiction/regulator/family: **US / FRB / US_FRB_PART217_STANDARDIZED**.
Regulatory and fact snapshot: **2025-01-01**.

This is an AI-assisted documentary assessment and proposed synthetic fact boundary for the internal
prototype. REQUIRED_AND_RESOLVED means the necessary text, dated evidence and explicit candidate
facts are available for human review. It does **not** mean approved interpretation, verified real-world
facts, approved GAAP accounting, executable sources, or Sprint 02 activation.

The owner has agreed to act as accountable reviewer. No personal identity, qualifications, approval
date, signature or final decision has been invented. ACTIVATION_RECORD.json remains unchanged.

## Preserved inputs and stopping rule

[GOLDEN_CASE_SOURCE_BOUNDARY.json](GOLDEN_CASE_SOURCE_BOUNDARY.json) makes material facts explicit.
Its new facts are **PROPOSED_SYNTHETIC_FACTS_FOR_OWNER_REVIEW**, not previously approved borrower
records. They supplement, and do not overwrite, the original candidate or accepted Sprint 01 fixture.

The candidate remains CORPORATE, EXPOSURE_AMOUNT USD 10,000,000, ratio risk weight 1.00,
RWA USD 10,000,000, and baseline_total_capital_equivalent USD 800,000 at 0.08.
These are unchanged candidate expectations, not engine output. No EAD alias or additional
capital measure is introduced.

Stop collecting sources once this boundary is documented. Positive, missing or contradictory
facts must reopen the affected dependency; they must never silently select the corporate path.
A different date, jurisdiction, product or material accounting treatment requires new review.
No borrower-name-dependent logic or production validator is implemented here.

## 1. Corporate counterparty exclusion — documentary gap resolved

Minimum sources and locators:

- US-DEFINITIONS: dated 217.2 Corporate exposure (1)-(2), Company, Depository institution,
  Foreign bank, Sovereign, MDB, PSE and GSE.
- USC-2024-12-1813: [FDIA section 3](https://www.govinfo.gov/content/pkg/USCODE-2024-title12/html/USCODE-2024-title12-chap16-sec1813.htm),
  especially (c)(1), with (a)(1)-(2) and (b)(1)-(3).
- US-INCORPORATED-211.2 and GOVINFO-2025-211.2:
  [Regulation K 211.2(j)(1)-(5)](https://www.govinfo.gov/content/pkg/CFR-2025-title12-vol2/xml/CFR-2025-title12-vol2-sec211-2.xml),
  independently captured from dated eCFR and the annual CFR.
- USC-2024-12-1752: [Federal Credit Union Act definitions](https://uscode.house.gov/view.xhtml?req=granuleid:USC-2024-title12-section1752&num=0&edition=2024),
  (1), (6), and the insured/noninsured distinction in (7). This supplies minimum U.S.
  identity context; do not claim Part 217 expressly incorporates this section.

The candidate is a privately owned domestic for-profit manufacturing corporation. The explicit
counterparty facts exclude national/state banks, banking associations, trust/savings/industrial banks,
federal/state savings associations, former savings associations, a joint-agency savings-association
determination, and foreign banks/branches/agencies. It does not conduct banking or receive deposits,
has no demand-deposit power, and is not recognized as a bank by a banking supervisor.
Lack of deposit insurance alone is **not** the exclusion rationale.

The credit-union screen is supported by the absence of a federal/state credit-union charter and of
a member thrift/credit cooperative. No detailed chartering, membership or insurance-eligibility
conditions need evaluation for this synthetic private manufacturing corporation.

The same explicit legal-form/purpose facts exclude a sovereign, central bank, governmental
subdivision/PSE, government-established or chartered public-purpose enterprise/GSE, and an
international or multilateral institution. The twelve named alternatives in the original
US-CORP-01 screen and GSE in US-CORP-02 remain unapproved NO candidates.
Do not infer that every financial company is excluded by the U.S. corporate definition.

### Dated reconciliation

The 2024 Code edition runs through **2025-01-06**, not January 1. The 1813 source credit/amendment
notes end in 2010; the 1752 notes end in 2006, with the latest edits targeting (3)/(5).
No post-January-1 change is present in the selected definitions. These are point-in-time
documentary findings based on official codification/notes, not invented original effective dates
or a review of every incorporated law. The 1813 deposit-insurance and foreign-branch subsidiary
statutes need not be traversed further where all relevant organizational categories are explicitly absent.

The Regulation K request is explicitly for 2025-01-01; the annual section carries DATE 2025-01-01.
All 58 direct paragraphs match after whitespace-only normalization, including the five (j) criteria.
This corroborates the selected dated text; it does not establish a whole-section commencement date,
an open-ended interval, or legal applicability after the requested date.

## 2. PPP exclusion — documentary gap resolved

USC-2024-15-636 provides
[15 USC 636(a)(36)(A)(ii)-(iii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title15/html/USCODE-2024-title15-chap14A-sec636.htm).
The definition is program-based: the loan must have been made under that paragraph during its
specified covered period. The source also contains the second-draw definition at (37)(A)(ii).

The case now explicitly stipulates ppp_loan=false, no origination under (a)(36) or (a)(37),
no SBA-program loan, and no PPP refinancing/acquisition. An ordinary loan label alone is not
the evidentiary boundary. Neither a 2025 snapshot nor expiry of an origination window proves
that an outstanding loan is non-PPP.

USC-2023-15-636 (edition through 2024-01-03) and USC-2024-15-636 (through 2025-01-06) have
**byte-identical (a)(36) fragments**, 47,441 bytes, SHA-256
198cc3d8c1e0122ec1348b44ab28331a17f895d041a2820f07355187e6e2e03e.
The section's latest amendment notes are 2022; those PPP edits add limitations provisions, not
a new covered-loan definition. The 2021 note identifies the change to the covered-period end.
No 2025 post-snapshot alteration of the relied-on definition is imported.

The existing FR-2020-07712 and FR-2020-21894 evidence already establishes the Part 217 exclusion
and unchanged final adoption. No new CARES corpus, SBA eligibility, payroll, forgiveness or
second-draw eligibility analysis is needed when program provenance is explicitly negative.
This is a proposed reviewed boundary awaiting the owner's actual sign-off, not that sign-off itself.

## 3. Carrying value and accounting — source/reconciliation boundary resolved

Minimum sources:

- US-DEFINITIONS: GAAP, Carrying value, Exposure amount (1), at 2025-01-01.
- Existing FR-2018-28281 / FR-2019-06011: revised carrying-value definition and delayed general
  commencement to 2019-07-01.
- FFIEC-GLOSSARY-2024-06: A-11, printed 6-24 (PDF page 11), Amortized Cost Basis and footnote 1;
  A-102, printed 3-24 (PDF page 108), opening PCD definition.
- FFIEC-RC-2024-03: RC-9/10, printed 3-24 (PDF pages 9/10), items 4.a-4.d and 5.
- FDIC-2024-06-INSTRUCTIONS-INDEX / FDIC-2024-12-INDEX / FFIEC-2024-12-UPDATES:
  dated component and replacement-page evidence.

Proposed reconciliation, all USD, all at the fixed snapshot:

| Component                                                         | Explicit candidate amount/treatment                         |
| ----------------------------------------------------------------- | ----------------------------------------------------------- |
| Original funded principal                                         | 10,000,000.00                                               |
| Principal repayments                                              | 0.00; outstanding principal 10,000,000.00                   |
| Accrued interest receivable                                       | 0.00; no elapsed unpaid interest included at this snapshot  |
| Unamortized fees and costs                                        | 0.00 each                                                   |
| Unamortized premium and discount                                  | 0.00 each                                                   |
| Full charge-offs and partial write-offs                           | 0.00 each; two labels do not create two deductions          |
| FX, fair-value hedge and other carrying adjustments               | 0.00 each                                                   |
| Gross amortized cost                                              | 10,000,000.00                                               |
| Credit-loss allowance, specific provisions, transfer-risk reserve | 0.00 each, expressly synthetic and pending human acceptance |
| Net balance-sheet amount under that zero-allowance assumption     | 10,000,000.00                                               |
| Part 217 ordinary non-PCD carrying value candidate                | 10,000,000.00; no second allowance/provision deduction      |

A-11 specifies the amortized-cost adjustment categories and treats charge-off/write-off terminology
interchangeably. RC-9 distinguishes gross HFI loans, allowance and allowance-net HFI balance.
Part 217's Carrying value definition does not reduce the ordinary non-PCD/non-AFS asset by its
associated credit-loss allowance. Those are distinct concepts, despite equal candidate numbers.

**Zero allowance is not inferred from performing status.** No CECL estimate has been calculated,
no claim is made that GAAP permits zero allowance merely because a loan is current, and no
real loan's GAAP compliance is certified. The owner must expressly accept the zero-balance
educational simplification or require a changed accounting candidate before activation.
If an allowance is positive, the net balance would differ; it must not automatically reduce this
ordinary non-PCD regulatory measure. No general CECL, loss-estimation or bank-capital transition
engine is a prerequisite to explaining this bounded gross-carrying-value example.

FinBank originates and retains the ordinary loan for investment, with intent/ability to hold;
it does not acquire a credit-deteriorated asset or legacy PCI pool. There is no fair-value option,
held-for-sale classification, AFS/HTM debt security or preferred security. HFI loans are not
automatically HTM securities. These explicit instrument facts close the outer exception gates;
the positive measurement exceptions, AOCI election mechanics and full ASC corpus are not evaluated.

This closes the **source and proposed factual basis for review**, not final accounting approval.
The original candidate's gaap_carrying_value label must be read with this gross/net distinction.
A human rejection of the stipulations reopens DEP-REPORTING-ACCOUNTING; it is not overridden by tests.

## 4. Covered position / market-risk scope — documentary gap resolved

US-DEPENDENCY-217.202 supplies Covered position (1), (1)(i)-(ii), (2), footnotes 32/33,
Trading position and Foreign exchange position; US-SCOPE-STANDARDIZED supplies 217.30(b).

The substantive candidate facts exclude short-term resale, price-profit/arbitrage or market-making
intent, trading management/reporting, hedging another covered position, FX and commodity positions.
The bank's functional currency and loan currency are both USD, with no embedded derivative.
There is no securities-lending/repo position (footnote 32) and no covered-position hedge
(footnote 33); neither footnote requires its downstream treatment to be evaluated here.

FFIEC-RCD-2020-09, RC-D-1 (PDF page 1), and FFIEC-GLOSSARY-2024-06, A-119/120 (PDF pages 127/128),
supply reporting/trading substance. They explicitly distinguish ordinary non-trading loans from
loans managed for trading. Non-filing of RC-D or a small trading balance is **not** the reason
for the candidate exclusion. RC-D's FDIC assessment-threshold footnote concerns who reports the
schedule, not whether this loan is held for trading, so the Part 327 assessment chain is unnecessary.
FR Y-9C is not the selected entity's report; it is a bank, not a holding-company case.

The dated 217.202 text was already corroborated against annual CFR (69 direct paragraphs).
Existing FR-2019-27249's footnote table renumbers the Board's covered-position footnotes 31/32
to 32/33; numbering is not a new loan treatment. No claim of an institution-wide market-risk
exemption or review of the entire market-risk rule follows.

### Reporting edition boundary and access limitation

The [FDIC December 2024 archive](https://www.fdic.gov/bank-financial-reports/december-2024) links the
June instruction set and December update. Captured components retain their printed page dates.
The December replacement list does not replace A-11, A-102, A-119/120, RC-9/10 or RC-D-1.
Only these passages are relied on. Older A-3/A-6/A-7 pages are **not** used as December authority.

The full December FFIEC PDF and index were readable through web search, but direct raw download
returned HTTP 403/CAPTCHA. No challenge was bypassed and no error page was kept as evidence.
The official FDIC component files and update list supply the needed raw-byte evidence instead.
The complete 782-page instruction book is neither captured nor asserted to have been reviewed.
Relevant source pages, printed dates and footnotes were extracted and visually inspected.

## Final minimum dependency boundary

Every manifest dependency has one of the owner's four allowed labels:

- **REQUIRED_AND_RESOLVED (8):** DEP-INSTITUTION, DEP-CBLR, DEP-EXTERNAL-IDENTITY, DEP-PPP,
  DEP-REPORTING-ACCOUNTING, DEP-COVERED-POSITION, DEP-UNSETTLED, DEP-PAST-DUE.
  Resolution is documentary readiness conditional on the explicit candidate facts.
- **REQUIRED_BUT_UNRESOLVED (0):** none under that narrow candidate boundary.
- **NOT_REQUIRED_FOR_GOLDEN_CASE (4):** DEP-AOCI, DEP-QCCP, DEP-CRM-DERIVATIVES,
  DEP-OTHER-CLASSES. Their outer negative screens remain required; deeper conditional law,
  positive qualification and calculation mechanics are unnecessary for these facts.
- **DEFERRED_FUTURE_SCOPE (2 groups):** DEP-FUTURE-POSITIVE-TREATMENTS and
  DEP-OTHER-DATES-AND-JURISDICTIONS. This includes full CECL/accounting, bank/PPP eligibility,
  market risk, all other exposure classes, other dates/jurisdictions and full interval endpoints.

The existing CBLR never-elected/no-grace, unsettled securities/FX/commodity transaction,
past-due/nonaccrual, and institution facts close the remaining immediate scope screens.
No permission to implement those future classes or controls is implied.

## Human decisions still required

The owner must review and sign the exact source versions/locators, interpretations, proposed
negative facts, carrying-value reconciliation and zero-allowance simplification, corporate
classification, 100% weight, RWA, sole educational capital output, and exclusions.
Final reviewer identity/authority, responsibilities, date, decision and linked evidence remain empty.

Unknown effective_to values remain UNKNOWN_NOT_OPEN_ENDED. Documentary observation at January 1
does not establish validity on other dates. Future executable version/hash/trace contracts and
activation approval remain separate gates. Source readiness does not fulfill them.

R-1888 remains **PROPOSED / executable=false**. Every source/dependency remains PENDING_REVIEW
and non-executable. No activation PR was created. No production code changed.

SPRINT 02 REMAINS INACTIVE
