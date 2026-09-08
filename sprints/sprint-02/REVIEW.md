# Sprint 02 Planning Review — Final Activation Preparation

Status: PLANNING ONLY — NOT ACTIVE

Revision date: 2026-09-08. This record distinguishes completed planning work from unapproved
regulatory interpretation and unimplemented software.

## Architecture direction versus activation

- Product architecture direction: approved by the project owner's explicit architecture-revision request.
- Generalized engine, pluggable rulesets, BCBS concept layer, U.S. first executable jurisdiction:
  documented design intent, not implemented behavior.
- Proposed ADR: [0004 — Generalized regulatory engine](../../docs/adr/0004-generalized-regulatory-engine.md).
  Status PROPOSED until Sprint 02 activation.
- Product-owner implementation activation: NOT GRANTED.
- Personally named human regulatory reviewer: PENDING.
- Reviewer role/authority/acceptance and review process: PENDING.
- U.S. source versions, dates, hashes, locators, and interpretation approval: PENDING.
- Golden Case assumptions/classification/risk weight/RWA/teaching outputs/exclusions: PENDING.
- Typed regulatory exposure measure replaces the rejected EAD alias by owner direction.
- Accounting basis, regulatory interpretation, final schema/hash and historical-selection policies: PENDING.
- No AI system is designated as the accountable regulatory reviewer.

## Planning changes made

- Replaced a BCBS-first, case-focused proposal with generic orchestration and a U.S. Part 217 provider.
- Made Alpha Manufacturing presentation/fixture data only; required name-invariance and another
  ordinary corporate fixture without changing core orchestration.
- Separated conceptual BCBS authority from executable domestic regulatory authority.
- Defined minimum fact requirements, explicit negative/scope facts, extension points, and typed errors.
- Revised result/trace contracts to v0.2-draft and RegulatoryExposureMeasure to a typed contract.
  U.S. output is EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE; no EAD alias.
- Kept 2025-01-01 fixed, restricted teaching to baseline_total_capital_equivalent at 0.08,
  and mapped the corporate screen to the fourteen dated U.S. definition exclusions.
- Separated generic future vocabulary from executable U.S. predicates and product-scope guards.
- Added a null accountable-human activation record and conditional activation-PR/implementation sequence.
- Added a draft Golden Case, source manifest, captured evidence, planning-only checks and future test vectors.
- Replaced the old automatic net-provisions premise with review of U.S. carrying-value measurement.
- Removed mandatory BCBS non-SME/EUR sales and rating-path assumptions from the first U.S. slice.
- Added lifecycle versus review-status separation, date-matching, source manifests, and immutable evidence.
- Documented future BCBS calculator, Regxify Regulatory Core reuse, and existing Basel/ERBA integration
  analysis as later work. No provider implementation or repository extraction occurred.

These are planning-file revisions, not checked-off Sprint 02 implementation acceptance criteria.

## History and preservation

- Original accepted Sprint 01: 03b03ec; hardening merge PR #2: b0cf3a9.
- Post-merge acceptance cleanup PR #3: 5fcfc5a, brought into this planning branch without rewriting history.
- Original Sprint 02 planning commit 60fad85b78a1559fe61b78e461894587d165a304 remains preserved in
  ancestry and at the untouched local codex/sprint-02-rules-calculation branch.
- Planning publication f90ee1e remains in history. Old BCBS candidate text is superseded as an
  execution proposal, not erased from historical commits.
- Review branch: https://github.com/ragu-selva/financial-pods/tree/codex/sprint-02-planning
- No Sprint 02 branch merge into main, activation, production-code change, or fixture change is authorized.

## Source research and limits

See [SOURCE_REVIEW.md](SOURCE_REVIEW.md) and [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json).

- Captured all six required sections through the official dated eCFR API for 2025-01-01.
- Captured the GovInfo 2025 annual Part 217 XML, which explicitly records 2025-01-01.
- Captured eCFR version history and Federal Register documents 2013-21653 / 2023-23911 as source-chain
  starting evidence. Section notes include further references; the full relevant amendment/LSA
  reconciliation, especially § 217.2, is not complete.
- Captured the R-1888 proposal record separately: PROPOSED, executable=false. No 2026 proposal
  becomes 2025 authority or silently replaces a CURRENT rule.
- Exact raw files and SHA-256 values are recorded. Effective_from/effective_to, interpretation
  and reviewer fields are explicitly pending, not guessed from editorial dates.
- A browser-page access failure was overcome using the dated eCFR API. Initial GovInfo volume-3
  probes returned HTML rather than requested XML/PDF; those were not retained. Volume 2 is the
  correct captured annual edition. No 2026 FRRS compilation is used as 2025 proof.
- Sources are CAPTURED, NOT APPROVED. No execution-ready source manifest is claimed.

## Golden Case review checklist

- [ ] In-scope synthetic U.S./FRB institutional perimeter, reporting regime, and CBLR decision.
- [ ] Approve captured point-in-time 2025-01-01 sources and complete amendment/effective-interval review.
      The date is fixed; no re-dating alternative.
- [ ] Full corporate-definition exclusion screen and ordinary-loan applicability.
- [ ] Carrying-value reconciliation, adjustments, performance state, and every material assumption.
- [ ] U.S. corporate classification and risk weight.
- [ ] Typed regulatory exposure measure (EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE) and RWA.
- [ ] Sole baseline_total_capital_equivalent at 0.08, candidate USD 800,000, warnings and exclusions.
      No CET1/Tier 1 equivalents; no allocated-capital, institution-specific or adequacy claim.
- [ ] Personally named human approval, source/version evidence, and independent expected results.

Any illustrative USD 10 million RWA / USD 800,000 teaching value in the scope document remains
conditional. Matching the old BCBS numeric example cannot substitute for U.S. regulatory review.

## Verification evidence

### Historical evidence, not verification of a Sprint 02 implementation

The 2026-08-27 draft review recorded 41 finance, 5 API, 3 web, and 2 browser tests plus
format/lint/types/builds and 10 artifact hashes passing. Sprint 01 hardening later recorded
130 finance tests and successful hosted CI; its accepted review remains untouched.
These results test the existing baseline, not an implemented U.S. regulatory engine.

### Prior architecture-revision verification (03d0e09), preserved evidence

Verified locally on 2026-09-08:

- `node scripts/task.mjs verify`: PASS (exit 0).
- Formatting, ESLint/Ruff lint, TypeScript, and mypy: PASS.
- Existing tests: 130 finance, 5 API, 3 web, and 2 browser tests: PASS.
- Web production build and API/finance source and wheel builds: PASS.
- All 10 immutable reference-artifact hashes: PASS.
- Planning-document banners, proposed ADR status, relative links, balanced code fences,
  and the JSON classification example: PASS.
- `git diff --check`: PASS.
- Production code, fixtures, infrastructure, reference artifacts, and historical Sprint 00,
  Sprint 01, and Sprint 01 hardening files match origin/main.

These checks verify the existing baseline and revised documentation, not an implemented
classification/calculation/provider or the proposed regulatory outputs. No new Sprint 02
implementation tests were added. Docker stack verification was not rerun for this documentation-only
change; the previously recorded local-runtime limitation remains, and no new Docker pass is claimed.
Non-failing baseline warnings included Starlette/httpx deprecation, pytest cache WinError 183,
Next.js slow-filesystem detection, and FORCE_COLOR/NO_COLOR precedence.

### Final activation-preparation verification

Verified locally on 2026-09-08 for this preparation:

- `node --test sprints/sprint-02/planning-evidence.test.mjs`: PASS, 12 planning-only tests.
  Includes raw SHA-256 checks, all six dated sections, proposal-injection/alias/binding mutations,
  no-EAD/wrong-basis/extra-teaching-output mutations, fixed date, U.S. screen structure,
  null reviewer identity and inactive controls.
- `node scripts/task.mjs verify`: PASS, exit 0. Formatting, lint, TypeScript/mypy, 130 finance
  tests, 5 API tests, 3 web tests, 2 browser tests, web/Python builds and all 10 artifact hashes pass.
- Authored planning Markdown/JSON/test formatting and JavaScript syntax checks: PASS.
- Documentation links, JSON examples and code-fence checks: PASS.
- Source XML parses and all six sections are present in the GovInfo 2025 annual-edition XML.
- All 11 captured evidence hashes also match their staged Git blobs. Raw-source whitespace is
  preserved through evidence-only Git attributes; authored files pass formatting and diff checks.
- Accepted fixture matches its original Git blob; only checkout CRLF is normalized for that check.
  Source evidence hashes use raw bytes with no normalization.
- Production, data, infrastructure, reference artifacts and accepted historical sprint files remain
  identical to origin/main. No regulatory runtime schemas, selector, classifier or calculator added.

These checks validate review artifacts and the existing baseline, not legal interpretation or
production regulatory behavior. The runtime vectors in PLANNED_TESTS.md remain unimplemented.
Docker was not rerun for this non-runtime change; the previously recorded local-runtime limitation
remains and no new stack pass is claimed. Existing non-failing Starlette/httpx, pytest cache
WinError 183, Next.js slow-filesystem and FORCE_COLOR/NO_COLOR warnings remain.

## Known limitations and deferred work

### Reusable source-resolver follow-up

The requested skill is at skills/effective-dated-regulatory-source-resolver/SKILL.md. Its scope is
documentary source-version resolution for explicit jurisdiction/regulator/regime/as-of selectors,
not legal judgment, exposure classification, calculations, source approval or sprint activation.
U.S. and BCBS source universes are separate, with proposal/removal safety and fail-closed gaps.

SOURCE_REVIEW.md and SourceManifest v0.2-draft record further documentary extraction from the
unchanged 4738841 captures: founding effective/compliance clauses, Board-specific adoption,
2023 effective date/amendatory targets and six-section paragraph-text corroboration.
All six consolidated effective intervals and human/legal approval remain unresolved.
ACTIVATION_RECORD.json and its seven null reviewer fields remain byte-for-byte unchanged.
No new source capture, activation PR, production engine or Change Detector was created.

Follow-up verification on 2026-09-08:

- Skill Creator quick_validate.py: PASS. Project/global/bundled Python initially lacked PyYAML;
  the validator ran with PyYAML 6.0.3 in an isolated temporary directory, with no project/global
  dependency change. This validates skill structure, not regulatory reasoning or legal approval.
- Skill is under 500 lines; local references, code fences, input JSON and authored formatting: PASS.
- `node --test sprints/sprint-02/planning-evidence.test.mjs`: PASS, all 12 checks.
- `node scripts/task.mjs verify`: PASS, exit 0; format/lint/types, 130 finance, 5 API, 3 web and
  2 browser tests, web/Python builds and all 10 immutable reference-artifact hashes.
- Additive-manifest audit: original source records, hashes, retrieval metadata, rule bindings,
  proposal evidence, executable flags and review values match 4738841 exactly.
- Raw evidence, seven-field activation record, Golden Case and production/historical files are
  unchanged. `git diff --check`: PASS.
- The ordered six-section XML paragraph comparison is diagnostic only, as documented in SOURCE_REVIEW.md.

The source resolver is an authored reusable skill, not an installed global integration or a
production source-selection engine. No activation/implementation authority follows from these passes.
Docker was not rerun for this documentation-only change; existing non-failing environment warnings
and the previously recorded local-runtime limitation remain unchanged.

No U.S. executable rules, approved source manifest, accepted regulatory fixture, production schemas,
or engine implementation exist. The draft JSON and local evidence-check tests are review artifacts,
not production models or calculation/selection logic. PLANNED_TESTS.md describes future runtime tests.
ACTIVATION_RECORD.json leaves all seven human reviewer fields null; the owner must supply/approve them.
Legal source/effective-interval and Golden result review is incomplete. Activation PR creation is BLOCKED;
no activation branch/PR or implementation branch was created.
Local Docker's previously recorded runtime limitation is non-blocking for documentation work;
this revision changes no runtime/infrastructure.

BCBS/SAMA/CBUAE providers; broad Basel calculator; bank/retail/mortgage/SME/sovereign/defaulted
and other classes; IRB/ERBA; CCF/CRM; actual capital ratios/adequacy; UI/API/database/AI/content;
and external core extraction are deferred. The owner's existing Basel/ERBA engine has not been
inspected, copied, or evaluated for reuse in this task; that requires a later bounded analysis.

## Decision

- [x] Record the owner-approved final architecture directions as planning.
- [x] Capture dated source bytes and prepare draft manifest/Golden/reviewer records.
- [ ] Finish source/amendment/effective-interval review and named human sign-off.
- [ ] Accept proposed ADR 0004 at activation.
- [ ] Approve regulatory sources, interpretations, facts, and golden results.
- [ ] Activate Sprint 02.
- [ ] Accept Sprint 02 implementation.

Named regulatory reviewer/date: PENDING.

SPRINT 02 REMAINS INACTIVE
