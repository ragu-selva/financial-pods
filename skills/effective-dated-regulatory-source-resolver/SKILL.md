---
name: effective-dated-regulatory-source-resolver
description: Resolves official regulatory source-version evidence for an explicit jurisdiction, regulator, regime and as-of date. Use for point-in-time source manifests, amendment-chain reconciliation, or dated BCBS chapter evidence; not exposure classification, calculations or regulatory approval.
---

# Effective-Dated Regulatory Source Resolver

> Which official regulatory text was applicable for a requested jurisdiction, regulator, regulatory regime, section/topic and regulatory as-of date?

Answer with documentary source candidates, exact version evidence and unresolved questions.
Do not turn source resolution into a legal applicability opinion. This skill does not calculate
RWA, classify exposures, interpret borrower facts, make regulatory judgments, approve sources or
substitute an AI reviewer. It neither activates a sprint nor authorizes product implementation.

## Inputs and selection boundary

Require explicit jurisdiction, regulator, regime/ruleset family, as-of date, and sections/topics.
Validate the ISO calendar date. Ask for missing selectors; do not infer them from a borrower,
currency, date or a convenient source. A topic request needs a confirmed section/chapter mapping;
do not silently guess a complete regulatory dependency set.

```json
{
  "jurisdiction": "US",
  "regulator": "FRB",
  "ruleset_family": "US_FRB_PART217_STANDARDIZED",
  "as_of_date": "2025-01-01",
  "required_sections": [
    "217.1",
    "217.2",
    "217.10",
    "217.30",
    "217.31",
    "217.32"
  ]
}
```

Selection order must be:

```text
jurisdiction
+
regulator
+
regime/ruleset family
+
as-of date
+
legal lifecycle status
        ↓
exact source version
```

Never infer jurisdiction from the date.
Never substitute BCBS for missing U.S. authority.
The date selects a version inside the selected universe; it never chooses the universe.

Supported documentary workflows below: US / FRB / Part 217 and the separately selected BCBS
Basel Framework universe. For BCBS use an explicit non-domestic universe identifier (for example,
jurisdiction=BCBS, regulator=BCBS) with a confirmed framework family and chapters; this identifier
does not assert domestic legal authority. Other jurisdictions/regulators/regimes fail closed until
a source-provider workflow is separately established. Do not route OCC/FDIC requests to FRB merely
because comparable text exists.

## Inspect before fetching

Read applicable repository AGENTS.md and execution controls. Use the caller's repository/output
location and authorized scope; this skill does not install itself, publish, merge, approve or monitor.

Check existing SourceManifest records and local snapshots first. Verify raw-byte hashes and the
full selector tuple before reuse; a matching date or URL alone is insufficient. Preserve original
retrieval metadata, bytes and history. Record a new verification date separately, not as a new
retrieval. Do not refetch identical evidence merely to rewrite it.

Only fetch missing evidence needed by the request. Use official sources, record redirects/content
type, and verify the response contains the requested document (an HTTP 200 HTML error is not XML/PDF).
If access fails, try a relevant official alternate and record the limitation. Do not fabricate
versions or evade access restrictions. A known evidence conflict or exhausted official alternatives
ends in an unresolved manifest, not an invented fallback.

## U.S. provider process

```text
requested US as-of date
        ↓
dated eCFR source
        ↓
GovInfo annual CFR corroboration
        ↓
Federal Register / amendment-chain evidence
        ↓
effective interval reconciliation
        ↓
raw source capture
        ↓
SHA-256
        ↓
SourceManifest
        ↓
human regulatory review
```

1. Bind US + FRB + Part 217 regime before resolving the date. Use the dated eCFR section/API,
   retaining the requested date, exact paragraph/definition locator and editorial version metadata.
   Example already used: official eCFR `/api/versioner/v1/full/2025-01-01/title-12.xml?part=217&section=217.2`.
   Treat this as an example, not a promise of an unchanged API.
2. Corroborate with the applicable GovInfo annual CFR edition. Read its actual title, volume and
   edition date. If an edition precedes the request, bridge the gap with amendments; if it follows,
   reconcile intervening changes rather than assuming it represents the earlier date.
3. Follow section source notes, the List of CFR Sections Affected (LSA), and Federal Register final
   rules/corrections/delays/removals. Match agency and regulation in multi-agency rules; common
   preamble text requires the agency's adopting instructions. A section note can omit definition
   amendment detail. Latest editorial `amendment_date` is not proof of legal commencement.
4. Extract stated effective dates, mandatory compliance dates, transition/sunset conditions and
   amendatory paragraph targets separately. Publication, retrieval, editorial correction and
   compliance dates are different facts. Record supported event dates without assigning them to
   an entire consolidated section whose intervening amendment chain is incomplete.
5. Reconcile candidate effective_from/effective_to at the required paragraph/version granularity.
   Unknown end date is not proof of infinite validity. Preserve conflicting candidates for review;
   do not choose the newest. Changes with unresolved applicability, exceptions or transitions require
   human/legal review. No independent borrower/institution treatment judgment belongs here.
6. Preserve raw responses needed to support this reconciliation. Capture may occur earlier so the
   evidence can be examined; incomplete reconciliation may still produce a partial, non-executable
   manifest. Hash full stored bytes with SHA-256: no text/XML/Unicode/newline normalization, no URL-
   only hash. Separate any normalized diagnostic comparison from the authoritative raw hash.
7. Emit source evidence and explicit gaps for a personally named human reviewer. Never copy
   approval identities from unrelated records or label AI research as approval.

Concrete Financial Pods examples, relative to this skill directory:

- [Existing SourceManifest](../../sprints/sprint-02/SOURCE_MANIFEST.json)
- [Source review and amendment follow-up](../../sprints/sprint-02/SOURCE_REVIEW.md)
- [Raw 2025-01-01 captures](../../sprints/sprint-02/evidence/us-2025-01-01)
- [Human activation record](../../sprints/sprint-02/ACTIVATION_RECORD.json)

These captures were committed in 4738841; reuse their hashes and original retrieval metadata.
For this case, 2025-01-01 stays fixed. The 2017 eCFR baseline and a 2026 compilation do not establish
original effective dates. Source findings may remain unresolved after all captured text is inspected.

## BCBS provider process

```text
requested BCBS framework + as-of date
        ↓
BIS Basel Framework timeline/version
        ↓
chapter version effective as-of requested date
        ↓
published version / status
        ↓
raw source snapshot
        ↓
SHA-256
        ↓
SourceManifest
        ↓
human review
```

Use the official [Basel Framework](https://www.bis.org/committees/bcbs/basel-framework) and
[past/future changes timeline](https://www.bis.org/committees/bcbs/basel-framework/timeline).
Select the requested chapter's dated version, not today's default page or latest full-framework PDF.
Record framework/chapter/paragraph identifiers, exact version URL/locator, published version/status,
effective-as-of and any evidenced successor/removal boundary, source documents and retrieval/hash.

BIS explains that effective-as-of dates reflect agreed implementation timing and can default to
the consolidated framework's launch for already-existing standards. Do not mistake such a default
for a standard's original publication or domestic commencement date. Check chapter-level dates and
status independently; do not infer one chapter's interval from another chapter or a whole-framework
headline. A consultation, future change or removed version is not automatically current.

BCBS is a separate regulatory universe from U.S. Part 217. Its dates are framework dates, not proof
of adoption into U.S., SAMA or CBUAE law. Mark authority_kind=INTERNATIONAL_STANDARD and state that
domestic applicability has not been resolved. Federal Register references are NOT_APPLICABLE for
a BCBS-only record, with a reason, not silently missing evidence. Request human review of any
unresolved chapter lineage/status. This provider resolves documents only; no BCBS calculator.

## Lifecycle, review and proposal safety

Keep legal lifecycle distinct from internal review:

```text
CURRENT
PROPOSED
FUTURE
SUPERSEDED
REMOVED
```

```text
DRAFT
PENDING_REVIEW
APPROVED
REJECTED
```

Record lifecycle relative to the requested as-of date, plus observed present/source-publication
status where different. CURRENT means candidate in force in the selected universe at that date,
not "most recently retrieved." FUTURE is not eligible before its evidenced effective date.
PROPOSED is never executable. SUPERSEDED/REMOVED cannot be live defaults; a requested historical
date before supersession/removal needs an explicit reviewed interval and retained evidence.
Do not erase historical versions or invent a removal date from a missing webpage.

A source may be used by an executable ruleset only when it is legally applicable to the requested
as-of date and internally approved. These are necessary, not sufficient: exact selector match,
complete verified evidence, unambiguous version, no applicable revocation and downstream authorization
also matter. The resolver does not grant executable=true; it emits non-executable review candidates.
Preserve existing valid human approval metadata unchanged when reusing evidence; conflicts require
review, not silent approval or rejection by this skill.

R-1888 is the concrete safety example:
[separate proposal evidence](../../sprints/sprint-02/evidence/r-1888/proposal-record.source.txt).

```text
legal_status = PROPOSED
executable = false
```

A proposal must never replace an effective rule because it is newer. An alias named CURRENT,
internal approval flag or later retrieval cannot bypass proposal status. A later final rule must
be independently sourced, versioned, effective-dated and human-reviewed as a new record; never
mutate the proposal snapshot into a final rule or retroactively change the 2025 case.

## Output and fail-closed behavior

Use a versioned SourceManifest compatible with the repository's existing review manifest; extend
it explicitly rather than overwrite approved records. For a new repository, agree its versioned
mapping first. Keep source resolution separate from calculation bindings/borrower assumptions;
do not generate or change the existing manifest's regulatory interpretations or calculation rules.

Include:

- jurisdiction, regulator, ruleset_family/regime and regulatory_as_of;
- source sections/topics/chapters, exact source locators and immutable source/version identity;
- effective_from/effective_to, whether an unknown endpoint is unresolved or explicitly open-ended,
  date-basis evidence, publication/version and editorial metadata kept distinct;
- Federal Register/amendment references where applicable; cross-reference dependencies and limits;
- retrieval timestamp/date, original URL/redirect, local snapshot path, raw byte length, SHA-256
  and explicit hash policy; original capture and later verification dates kept separate;
- lifecycle status/as-of, internal review status and preserved or null human review evidence;
- conflicts/unresolved_evidence with source locators, reason and the review/action needed;
- resolution_status and executable=false for the resolver's new candidate output.

Return UNRESOLVED with reasons and no executable source selection when any of these holds:
EFFECTIVE_INTERVAL_UNRESOLVED, CONFLICTING_ELIGIBLE_VERSIONS, SOURCE_EVIDENCE_INCOMPLETE,
ONLY_PROPOSED_OR_FUTURE_AVAILABLE, or UNSUPPORTED_JURISDICTION_OR_REGIME.
Also fail closed on missing selectors, hash mismatch, unreviewed removal/supersession or ambiguous
topic mapping. A partial evidence manifest is useful; an implied successful applicability finding is not.
Documentary completion may be CANDIDATE_EVIDENCE_COMPLETE while approval is still PENDING_REVIEW;
never describe that as regulatory approval or activation readiness.

## Verification and handoff

Check selector consistency, raw-file/Git-blob hashes, locators, distinct date semantics, all required
sections, isolated proposals, explicit gaps and reviewer metadata preservation. Report what was
verified mechanically versus what still needs human review. In this repository run
`node --test sprints/sprint-02/planning-evidence.test.mjs` and applicable documentation checks.
Those checks do not prove legal applicability. Do not populate previously null reviewer fields,
manufacture reviewer evidence, create an activation PR or implement downstream engines as part of
a resolver run. Any later activation workflow needs its own explicit authorization and completed gates.

## Reuse

The same versioned evidence workflow is intended for:

- Financial Pods: effective-dated learning/calculations consuming reviewed manifests.
- AI Regulatory OS: regulatory processing consuming reviewed source records.
- Reg Radar: change detection using retained dated evidence.
- Future Regulatory Change Detector: compare source manifests across dates.

These are intended consumers, not integrations implemented by this skill. Do not build the future
Change Detector, automatic monitoring, regulatory production engine or another repository here.
Keep provider universes separate and the resolver independent of Alpha Manufacturing or any case.

For the current Financial Pods planning work: PLANNING ONLY — NOT ACTIVE.
SPRINT 02 REMAINS INACTIVE
