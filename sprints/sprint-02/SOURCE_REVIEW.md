# Sprint 02 — Point-in-Time Source Review

Status: PLANNING ONLY — NOT ACTIVE

Capture date: 2026-09-08. Regulatory/fact date: **2025-01-01**, fixed by owner direction.
Evidence is captured for review; no rule, interpretation or candidate output is approved.

## What is pinned

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records exact local paths, retrieval URLs, publication/
version metadata, section/paragraph candidates, retrieval dates, byte lengths and SHA-256 hashes.

- Six full section snapshots from the official dated eCFR API: 217.1, 217.2, 217.10, 217.30,
  217.31 and 217.32. Date is explicit in every API request, not inferred from retrieval.
- [GovInfo 2025 annual edition](https://www.govinfo.gov/content/pkg/CFR-2025-title12-vol2/xml/CFR-2025-title12-vol2-part217.xml):
  full Part 217 XML, title 12 volume 2, FDSYS DATE and ORIGINALDATE both 2025-01-01.
  This corroborating document contains additional provisions; capturing them does not authorize
  implementing them or automatically including them in the first executable ruleset.
- eCFR Part 217 editorial version history, captured separately. It includes records after the
  Golden Case date and unrelated sections; it is metadata, not executable authority.
- [FR document 2013-21653](https://www.govinfo.gov/content/pkg/FR-2013-10-11/html/2013-21653.htm),
  78 FR 62018-62291 (2013-10-11), containing the founding rule/Part 217 codification.
- [FR document 2023-23911](https://www.govinfo.gov/content/pkg/FR-2023-11-27/html/2023-23911.htm),
  88 FR 82950-82980 (2023-11-27), covering insurance-activities amendments to general provisions.
  These two records start the source chain; they are not a complete amendment history.
- [R-1888 proposal record](https://www.federalreserve.gov/apps/proposals/FR-2026-0008-01/details),
  captured separately under evidence/r-1888. It links to FR document 2026-05960 dated 2026-03-27.
  legal_status=PROPOSED, executable=false. The full proposal notice has not been captured here.

The six section records are candidate execution sources, not an execution allowlist.
All source records and rule bindings have executable=false and pending review.

## Hash and normalization policy

Proposed source-raw-bytes-sha256.v1-draft: hash the complete downloaded response body as stored.
No whitespace, newline, Unicode, HTML or XML normalization; do not reserialize the XML first.
HTTP transfer framing/headers and URL text are not part of the payload. Files containing HTML
are saved as .source.txt and must not be executed. XML stylesheets are not needed or fetched.

evidence/.gitattributes sets -text so Git preserves every byte, including line endings, and
-whitespace to retain original source whitespace without treating it as an authored formatting defect. Verify
working-tree and staged/committed blobs against the manifest. Reformatting an evidence file breaks
its hash. A source change requires a new snapshot/version, never an in-place approved-content edit.
The manifest and candidate JSON are authored planning records, not source snapshots. Final
canonical manifest/input hashing is a separate contract approval; no approved manifest hash exists.

## Legal dates: what has NOT been inferred

The manifest stores effective_from=null, effective_to=null and effective_interval_status=PENDING.
Null means unknown, not open-ended validity. The January 2025 snapshot proves what was requested
and captured from the dated service; it does not by itself complete all legal applicability review.

The eCFR history contains editorial date/amendment_date/issue_date values. In particular, the
2017-01-01 baseline entries for §§ 217.30/.31 are NOT asserted to be original legal effective dates.
Other section updates/corrections also need paragraph-level review against actual final-rule dates.
A 2026 FRRS compilation or the time of this download is never proof of 2025 applicability.

CURRENT on the six draft records means candidate lifecycle **as of 2025-01-01**, pending review,
not an assertion that every section is the latest law today. Historical selection must reconcile
later supersession while preserving the requested 2025 applicability, without allowing proposals.

## Required amendment-chain review

### Follow-up using existing captures only — 2026-09-08

No source was recaptured or rewritten. All 11 evidence files and original retrieval metadata from
4738841 are retained. SourceManifest v0.2-draft adds explicit US/FRB/regime selectors,
resolution_status=UNRESOLVED and evidence-linked documentary observations; it does not promote
any source to approved or executable.

Resolved as documentary observations (not legal approval):

- **Founding date clause:** FR-2013-21653, DATES, captured lines 156-162, states January 1, 2014
  effectiveness with specified exceptions for other Part 208/225 amendments. It separately states
  mandatory compliance on January 1, 2014 for advanced-approaches organizations other than savings
  and loan holding companies, and January 1, 2015 for other covered organizations. Publication,
  effectiveness and mandatory compliance must not be collapsed into one date.
- **FRB adoption provenance:** the same document, 78 FR 62285, instructions 43-44, captured lines
  33137-33166, adds Part 217 from the common preamble and specifies Board/Board-regulated-institution
  substitutions. This connects common text to FRB authority; it does not allow an OCC/FDIC regime
  substitution. The eCFR 2017 baseline cannot be treated as the founding rule's original effective date.
- **2023 final-rule date:** FR-2023-23911, DATES at captured line 92, explicitly states January 1, 2024. Section II.B distinguishes this from first reporting as of December 31, 2024 and submissions
  in March 2025. These are source-level statements, not blanket inception dates for unchanged paragraphs.
- **2023 amendatory targets:** instructions 2-4 (88 FR 82968-82969; captured lines 2418-2604)
  revise § 217.1(c)(1), add § 217.1(g), revise the covered-savings-and-loan-holding-company definition,
  add five named insurance/regulated-affiliate definitions to § 217.2, and add § 217.10(f).
  Those instructions do not amend the corporate exposure, carrying value or exposure amount
  definitions, or § 217.10(a)(1)(iii). This bounded observation is not proof of an otherwise complete
  amendment chain or a conclusion about the Golden Case institution.
- **Dated text corroboration:** the direct paragraph sequences in the captured eCFR and GovInfo
  XML contain respectively 48, 555, 75, 2, 9 and 70 paragraphs for .1, .2, .10, .30, .31 and .32.
  An order-sensitive comparison of parsed paragraph InnerText, removing whitespace only, found
  zero remaining character differences for all six sections. Headings, tables, footnotes and
  editorial notes were outside this diagnostic comparison. This is neither legal equivalence nor
  a replacement for amendment review. No normalization was applied to captured bytes or SHA-256.

Exact findings and source IDs/locators are recorded in SOURCE_MANIFEST.json amendment_review.
The first two final-rule records already captured supply these observations; no new authority was
assumed and no new legal effective endpoint was assigned to a consolidated source.

Still unresolved for every section: final reviewed effective_from/effective_to, full relevant
amendment/correction/transition history, cross-reference completeness and human/legal applicability.
Both interval fields remain null with status PENDING. In particular, the missing § 217.2 LSA/
definition-amendment chain cannot be supplied by the limited 2023 insurance amendment alone.
The additional section-note references for .1/.10/.32 also require reconciliation.

### Remaining review work

- Read the relevant final-rule applicability/compliance/effective provisions, not just publication.
- Reconcile all relevant section and definition amendments through 2025-01-01 against dated eCFR,
  GovInfo annual text and Federal Register/LSA evidence. Record exact paragraph locators and dates.
- The captured § 217.2 editorial note expressly refers to the List of CFR Sections Affected:
  its single printed 2013 source note is not the complete amendment chain.
- Section notes for .1, .10 and .32 retain additional printed FR references in the XML and manifest.
  Obtain/verify the applicable additional final-rule evidence before accepting their legal intervals.
- Determine whether cross-referenced sources are needed (for example .12 CBLR context, company/
  instrument definitions and treatment exclusions); the required six are a minimum, not proof
  that six alone exhaust every legal dependency.
- Review the complete corporate definition, measurement and treatment exceptions against actual
  facts. Narrow product restrictions must not be represented as new statutory exclusions.
- Record reviewed interpretation, applicability, exclusions, human evidence and golden results.

This reconciliation is INCOMPLETE. No point-in-time source is legally approved merely because
its content hash matches. No 2026 proposal is an alternative source for the 2025 case.

## Proposal isolation

The R-1888 record remains immutable proposal evidence. It is absent from candidate_execution_source_ids
and rule bindings. A proposal cannot execute by direct request, alias, internal approval flag,
date manipulation or copying its candidate rate into a CURRENT record.
A subsequently finalized rule requires a new final-rule source chain, date, version and review,
then selection for an applicable as-of. It cannot retroactively change the accepted 2025 snapshot.

Planning-only tests exercise unsafe candidate-source list mutations. Future production selector
tests in [PLANNED_TESTS.md](PLANNED_TESTS.md) remain unimplemented until activation.

## Human review and readiness

The reusable [effective-dated regulatory source resolver skill](../../skills/effective-dated-regulatory-source-resolver/SKILL.md)
documents separate U.S. and BCBS provider workflows. It preserves the full selector tuple and keeps
CURRENT/PROPOSED/FUTURE/SUPERSEDED/REMOVED distinct from internal review status. It resolves source
evidence only; it does not classify exposures, calculate, approve sources, populate reviewer identity
or implement the future Change Detector.

[ACTIVATION_RECORD.json](ACTIVATION_RECORD.json) leaves all seven reviewer fields null for the owner
to supply/approve. Linked human evidence must approve sources, locators, interpretations, case
assumptions, classification, measure, weight, RWA, the sole 8% teaching output and exclusions.

Source capture: COMPLETE for the six required raw sections.
Source-chain/effective-interval review: INCOMPLETE.
Human approval: MISSING.
Activation PR: NOT READY; not created. ADR 0004 remains PROPOSED.

SPRINT 02 REMAINS INACTIVE
