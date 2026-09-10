# Sprint 03 — Learner Journey and Screen Plan

Status: PLANNING ONLY — NOT ACTIVE

## Design intent

Audience: a banker or analyst learning the concept through one synthetic loan. Begin with who
lent what to whom, reveal the regulatory decision, then connect each server-returned number to
its reason and source. This is a scrollable lesson with progressive disclosure, not a report dump.

Primary title: **Corporate Exposure — From Loan to Regulatory Capital**.
Always-visible context: **United States / Federal Reserve · As of 1 January 2025 · Synthetic educational example**.
Do not imply that this dated snapshot is the latest rule or that the amount is a live bank requirement.

Proposed visual direction: clear, restrained cards, readable dark text on light surfaces, a single
accent for the current story/decision and strong heading hierarchy. The old immutable HTML prototype
is a visual reference only. Its SAMA context, 75% example, EAD, editable calculator, video, tutor,
voice, comparison and progress features are explicitly not imported.

## Textual wireframe — no UI implemented

```text
Financial Pods
Corporate Exposure — From Loan to Regulatory Capital
United States / Federal Reserve | As of 1 January 2025
Synthetic educational example

1  THE LOAN
   FinBank  ->  USD 10,000,000 corporate term loan  ->  Alpha Manufacturing

2  WHY CORPORATE?
   CORPORATE
   Short explanation + selected approved exclusion checks
   [View regulatory reasoning]

3  EXPOSURE MEASURE
   Regulatory Exposure Amount                 USD 10,000,000
   Plain-language carrying-value explanation  [View source]

4  RISK WEIGHT
   Corporate Risk Weight                     100%
   12 CFR 217.32(f)(1)                        [Why 100%?]

5  RWA
   USD 10,000,000 exposure x 100% = USD 10,000,000 risk-weighted assets

6  EDUCATIONAL TOTAL-CAPITAL EQUIVALENT
   USD 10,000,000 RWA x 8% = USD 800,000
   Educational-only notice + all five limitations (always visible)

7  HOW DID WE GET THIS?
   Twelve ordered steps with expandable reasons
   [Source / rule locator] where applicable
```

This is composition guidance. All displayed amounts, percentages and equation results come from the
server DTO, including the formatted strings. Symbols and layout explain the relationship; the
browser performs no regulatory arithmetic. A verbal equivalent accompanies each visual equation.

## Seven sections and proposed copy

All explanatory prose below is DRAFT learner copy for human approval against the accepted evidence,
not new regulatory interpretation or an approved source quotation.

1. **The Loan.** Display FinBank, Alpha Manufacturing, corporate term loan, USD 10,000,000 and
   2025-01-01. Narration: "FinBank has made a fully drawn term loan to Alpha Manufacturing.
   Follow this synthetic loan through the reviewed U.S. capital framework." The arrow is
   decorative; the complete relationship is available as text. No borrower/date/value controls.
2. **Why Corporate?** Show the engine's CORPORATE label. Draft: "This case passes the reviewed U.S.
   corporate-definition screen." Primary examples may include not sovereign, not bank/depository,
   not PSE/GSE, not residential mortgage, not securitization, not equity and not PPP.
   Label these as selected checks, not the entire definition. The reasoning disclosure covers all
   fourteen reviewed definition paragraphs and their named alternatives with friendly labels.
   Keep statutory exclusions, treatment exceptions and synthetic/product assumptions in separate
   groups; do not claim that every narrow product guard is a statutory non-corporate category.
3. **Exposure Measure.** Heading "Regulatory Exposure Amount", USD 10,000,000. Draft:
   "The reviewed U.S. rules use a carrying-value measure. In this synthetic example, the explicitly
   approved zero adjustments leave the amount shown." Explain the simplified accounting assumption
   without implying that carrying value always equals original principal or that zero allowance
   follows from a performing loan. Technical detail may identify US_STANDARDIZED_CARRYING_VALUE;
   never relabel it EAD. Bind the source action to the accepted US-MEASURE evidence.
4. **Risk Weight.** Heading "Corporate Risk Weight", 100%, source label "12 CFR 217.32(f)(1)".
   "Why 100%?" expands draft copy: "For this reviewed ordinary corporate case, the selected U.S.
   rule returns the weight shown. The required exception checks have also passed."
   Show supporting exception-screen context from the accepted rule references; do not imply that
   all companies, jurisdictions or loan variants receive this weight. No rating/SME shortcut.
5. **RWA.** Display the DTO exposure amount, weight and RWA with multiplication/equality symbols.
   The server result is authoritative. Draft: "The engine applies the selected risk weight to the
   regulatory exposure amount to produce risk-weighted assets." Source comes from US-RWA evidence.
6. **Educational Total-Capital Equivalent.** Display the DTO RWA, 8% and USD 800,000.
   The amount maps only to baseline_total_capital_equivalent. Keep "Educational only" beside it
   and show every limitation without requiring a click: not allocated loan capital; not economic
   capital; not a complete regulatory capital requirement; not an institution-specific capital
   requirement; not a capital adequacy conclusion. Show internal-prototype context. No CET1/Tier 1.
7. **How Did We Get This?** Render the twelve actual engine steps in order, translated to learner
   titles and explanations. Do not generate a new trace or display raw JSON, internal field paths,
   hashes or reviewer details. Preserve source availability and warnings while simplifying language.

## Trace presentation mapping

The application maps existing operation identifiers to reviewed display copy. Mapping is presentation
only; missing/unrecognized required operation or output shape prevents a complete lesson response.

| Step | Learner title                                   | Evidence shown                                                            |
| ---- | ----------------------------------------------- | ------------------------------------------------------------------------- |
| 1    | Check the regulatory context                    | Lesson validation; no invented legal citation                             |
| 2    | Select the U.S. Part 217 ruleset                | Selected dated context; no invented legal citation                        |
| 3    | Verify approved source evidence                 | Evidence-verification explanation; no hashes/reviewer internals           |
| 4    | Check FinBank's institutional scope             | Selected US-SCOPE references                                              |
| 5    | Check corporate exclusions and case assumptions | Actual US-CLASS / scope / measure / treatment references, grouped clearly |
| 6    | Classify as Corporate                           | Selected US-CLASS references                                              |
| 7    | Resolve the ordinary corporate treatment        | Selected treatment and measurement references                             |
| 8    | Determine the exposure measure                  | US-MEASURE and returned measure                                           |
| 9    | Apply the corporate risk weight                 | US-CORP-RW, including 217.32(f)(1)                                        |
| 10   | Calculate risk-weighted assets                  | US-RWA and returned RWA                                                   |
| 11   | Calculate the educational equivalent            | US-TEACHING and returned amount/ratio, with limitations                   |
| 12   | Attach sources and warnings                     | Available source list and limitations; no fabricated rule                 |

Each regulatory step has a plain-English explanation, legal locator and usable source link(s).
Non-regulatory steps explicitly say they are lesson/engine checks rather than inventing a legal rule.
A source disclosure distinguishes the dated source, approved interpretation and teaching explanation.
A linked official page is not a claim about today's law.

## Proposed component structure

Future locations only; no components/files are created by this pack:

```text
apps/web/src/app/lessons/corporate-exposure/page.tsx  (server composition)
  GoldenLessonHeader
  LoanStory
  CorporateClassification
    RegulatoryReasoningDisclosure
  ExposureMeasure
  RiskWeight
    WhyRiskWeightDisclosure
  RwaEquation
  EducationalCapitalEquivalent
    EducationalWarnings
  CalculationTrace
    TraceStepDisclosure
    CitationList / CitationLink
```

Use server-rendered sections and native details/summary disclosures where suitable. Prefer an inline
expanding reasoning panel for the first slice; a drawer is an unresolved UX choice, not required.
Do not add a component library, canvas, charting engine or motion system for this screen.
Shared components remain colocated until genuine reuse exists; do not build a premature UI package.

## Reading, accessibility and error states

- One H1 and seven H2 sections; a skip link and optional anchor navigation, not a progress tracker.
- On narrow screens, stack the bank/loan/borrower story and equation operands in reading order.
  Preserve full amounts and units; no horizontal-scroll-only content at 320 CSS pixels.
- Test keyboard navigation, visible focus, disclosure semantics, screen-reader labels and 200% zoom.
  Expanded content stays reachable; color alone never indicates meaning. If a drawer is approved,
  explicitly test focus entry/return, Escape and appropriate dialog behavior.
- Warnings remain visible at mobile sizes. Put them with the amount, not only in a footer.
- Source links use descriptive text, indicate official destinations and any new-tab behavior, and
  never render arbitrary source HTML. Default same-tab navigation is proposed pending owner choice.
- Loading shows neutral placeholders, never fabricated numbers or an apparent calculated result.
- Missing/malformed DTO, timeout, failed source verification or non-200 response shows a clear
  "This lesson is temporarily unavailable" state and Retry. Never show partial, stale or fallback
  financial values. A missing optional external page does not substitute a new legal source.
- The static document title/help copy may remain visible on failure, but not successful calculations.
  Correlation IDs are for support details, not primary learner content.

## UX decisions pending before activation

Recommended defaults are proposals, not owner approvals:

- Inline reasoning panel versus drawer: inline panel first for mobile/keyboard simplicity.
- One scrolling page versus staged reveal: one page; no persistence or gated progression.
- English USD display: full grouped amounts; integer-dollar display for this case, retain exact
  cents in server values. Percentages shown as 100% and 8% from server formatting.
- Confirm the draft carrying-value, corporate-screen and "Why 100%?" prose; no source reinterpretation.
- Confirm light-theme brand treatment and source-link same-tab behavior; no brand asset generation.
- Confirm placement/density of the complete twelve-step trace and full exclusion screen.

SPRINT 03 REMAINS INACTIVE
