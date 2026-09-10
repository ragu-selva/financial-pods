# Sprint 02 — Activation Review

Status: ACTIVE

Review date: 2026-09-10. Implementation: **NOT YET STARTED**.
Activation PR: [#4](https://github.com/ragu-selva/financial-pods/pull/4), **OPEN FOR REVIEW**. No automatic merge.
Activation commit: bfd57576c1615abb53171abe6daeff5b0a854d83.
Hosted CI: pending for the final publication head; local verification below passed.

## Human approval

**Ragunath Selvaraj — Project Owner / Internal Regulatory Reviewer** approved the reviewed
boundary and accepted responsibility for the internal Financial Pods V1 prototype.
Decision: **APPROVED_FOR_INTERNAL_PROTOTYPE**. See [ACTIVATION_RECORD.json](ACTIVATION_RECORD.json).
The owner explicitly confirmed the reviewer name. AI transcribes this approval; it does not
independently sign off, certify regulation, or assume the reviewer's accountability.

Authority: Project owner accountable for regulatory interpretation and Golden Case approval for
the internal Financial Pods V1 prototype. This is not independent legal counsel, regulatory
certification, or production-bank sign-off.

## Approved scope and evidence

- Fixed US / FRB / US_FRB_PART217_STANDARDIZED / 2025-01-01.
- Synthetic in-scope state member bank, standardized treatment, CBLR not elected or in grace.
- Synthetic non-financial corporate borrower; ordinary fully drawn on-balance-sheet USD loan.
- All fourteen corporate exclusions and outer treatment/measurement negatives reviewed for this case.
- Six source-linked rule scopes and eight REQUIRED_AND_RESOLVED dependencies; none unresolved.
  Four deeper dependencies NOT_REQUIRED_FOR_GOLDEN_CASE, two groups DEFERRED_FUTURE_SCOPE.
- Exact-date approval only. Unknown legal endpoints remain UNKNOWN_NOT_OPEN_ENDED.
- R-1888 remains PROPOSED / executable=false; no alias or internal flag can admit it.
- Approved expectations: CORPORATE; EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE USD 10m;
  weight 1.00; RWA USD 10m; only baseline_total_capital_equivalent at 0.08 / USD 800k.
- Explicit synthetic simplifications: zero credit-loss allowance/write-offs/premium/discount/
  accrued-interest/fee adjustments; PCD=false, CRM=none, past_due=false, nonaccrual=false.
  No performing-status inference of zero CECL, no real-loan GAAP certification.
- USD 800k is educational, not allocated loan capital, economic capital, complete required capital,
  institution-specific requirement, or a capital adequacy conclusion.

The v1 SOURCE_MANIFEST.json is a separate approval envelope over the unchanged reviewed
SOURCE_MANIFEST.reviewed-v0.4.json. All 71 original raw captures, metadata, hashes, amendment
references and lineage remain intact. No new source investigation was performed.
Whole-document capture is not whole-document execution approval. Only listed locators qualify.

GOLDEN_CASE_APPROVED.json records approved expectations, not a runtime result. Candidate/fact
boundary files and ACTIVATION_RECORD.reviewed-v0.4.json retain their pre-approval state as
historical evidence. New approval does not edit Sprint 01's accepted fixture.

## Architecture and resolver

ADR 0004: **ACCEPTED**. Generic engine -> registry -> jurisdiction provider -> U.S. first.
BCBS is conceptual; additional providers/classes, Regxify extraction and Basel/ERBA integration
remain future scope. Alpha Manufacturing is a fixture, never engine dispatch logic.
The existing effective-dated source-resolver skill is included unchanged and approved only for
source evidence resolution. Its planning-run note is historical; it grants no activation authority.

## Git provenance and selective transfer

Planning commit **79b33dbb1f069a89fc6d87336a23268adea08589** was published unchanged to
codex/sprint-02-planning. That branch/history remains preserved, including 60fad85.
Activation branch **codex/sprint-02-activation** starts from fetched main at
**5fcfc5a42fc8cb3fc0a8bf53a8659fd60fa6d931**, containing PR #2 merge b0cf3a9.
Only sprints/sprint-02, ADR 0004 and the resolver skill were imported; current status/roadmap/
architecture controls and evidence checks are updated here. No wholesale branch merge or history rewrite.
Historical Sprint 00/01/hardening reviews and immutable reference artifacts are untouched.

Prior planning review:
[79b33db review](https://github.com/ragu-selva/financial-pods/blob/79b33dbb1f069a89fc6d87336a23268adea08589/sprints/sprint-02/REVIEW.md).

## Verification

**VERIFIED locally, 2026-09-10:**

- Source hashes and planning/activation checks: 35/35 pass; all 71 raw captures and pinned snapshots intact.
- node scripts/task.mjs verify: exit 0. Formatting, ESLint/Ruff, TypeScript and strict mypy pass.
- Python: 130 finance-engine tests (including Hypothesis properties), 5 API tests pass.
- Web: 3 unit tests and 2 Playwright Chromium smoke tests pass.
- Builds: Next.js production build and API/finance-engine sdist/wheel pass.
- All 10 immutable reference-artifact hashes pass.
- git diff --check passes. Authored activation formatting is checked separately from immutable evidence.

Docker runtime recheck failed: failed to connect to the docker API at
npipe:////./pipe/dockerDesktopLinuxEngine; open //./pipe/dockerDesktopLinuxEngine:
The system cannot find the file specified. This is the existing non-blocking local-runtime limitation.
No Docker stack-runtime pass is claimed; production/infrastructure code is unchanged.

Tests validate artifact integrity and approval consistency; they are not independent regulatory
review or evidence that a regulatory engine has been implemented.

Historical baseline: 130 finance-engine Python tests including property tests, 5 API tests,
3 web tests, 2 Playwright tests, lint/types/builds and 10 reference-artifact hashes passed.
These historical counts are not a claim of a fresh run.

Docker local-runtime known limitation: the Docker Desktop Linux engine pipe was unavailable
during prior verification. No fresh runtime pass is claimed. Recheck and record the exact result.

## Remaining gate and stop condition

Human/source/Golden activation prerequisites are complete for this internal prototype.
The activation PR must be reviewed and merged by a human before implementation starts on
codex/sprint-02-us-corporate-engine. No production classifier, provider, regulatory calculation,
business API, persistence, UI or tutor has been added. Runtime criteria remain unchecked.
Stop after this governance/evidence PR is ready for review; do not merge or start the engine.

## Historical planning review — superseded status, preserved evidence

The following review is retained from 79b33dbb1f069a89fc6d87336a23268adea08589.
Its pending/inactive wording and verification dates describe that historical planning snapshot,
not the current approval. The activation review above is current. No historical finding is deleted.

# Sprint 02 Planning Review — Final Activation Preparation

Status: PLANNING ONLY — NOT ACTIVE

Revision date: 2026-09-10. This record distinguishes completed planning work from unapproved
regulatory interpretation and unimplemented software.

## Architecture direction versus activation

- Product architecture direction: approved by the project owner's explicit architecture-revision request.
- Generalized engine, pluggable rulesets, BCBS concept layer, U.S. first executable jurisdiction:
  documented design intent, not implemented behavior.
- Proposed ADR: [0004 — Generalized regulatory engine](../../docs/adr/0004-generalized-regulatory-engine.md).
  Status PROPOSED until Sprint 02 activation.
- Product-owner implementation activation: NOT GRANTED.
- Owner has agreed to act as accountable human reviewer for the internal prototype.
- Personally named reviewer identity/authority, final review evidence and approval: PENDING.
- Final reviewer fields are deliberately unfilled; willingness to review is not completed approval.
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

### Source-chain and dependency follow-up (historical, 2026-09-08)

The source-resolver follow-up below describes 02904db historically. This later task reused all
11 captures and added 48 official raw files: 30 FR documents, 12 cumulative Title 12 LSA editions,
two discovery indexes and four dated dependency sections. SourceManifest v0.3-draft now records
ten paragraph lineage candidates, explicit unknown-end semantics and the minimal dependency inventory.
The existing six core section identities and regulatory/fact date remain unchanged.

Resolved documentary matters include the 2019 carrying-value delay; 2019 corporate definition
revision; 2020 PPP exclusion and final confirmation; 2020 corporate/QCCP cross-reference correction;
2020 renumbering of the 8% source; original RWA/scope adoption; 2024 institution-perimeter locator;
and the explicit 2021 end of temporary CBLR asset relief. See SOURCE_REVIEW.md for dates and limits.

**BLOCKED_ON_SOURCE_EVIDENCE:** incorporated identity/PPP statutory definitions, reporting/accounting
dependencies and covered-position/conditional-definition closure remain incomplete. The core
findings are available for review, not approved. Neither missing facts nor unknown legal endpoints
are defaulted. No activation PR is created.

Verification for this follow-up:

- Skill Creator quick_validate.py: PASS using the existing isolated PyYAML 6.0.3 validation directory;
  no project/global dependency or skill change. The existing skill covers the issues encountered.
- `node --test sprints/sprint-02/planning-evidence.test.mjs`: PASS, **20** planning-only checks.
  Eight added checks cover date/unknown-end semantics, delay/correction/sunset evidence, source/
  dependency links, proposal injection, premature approval and preserved activation controls.
- `node scripts/task.mjs verify`: PASS, exit 0. Formatting, ESLint/Ruff, TypeScript/mypy,
  130 finance tests (including existing Hypothesis tests), 5 API, 3 web, 2 browser tests,
  Next.js production build, API/finance source/wheel builds and 10 immutable artifact hashes.
- All **59** raw-byte source SHA-256/length checks: PASS. Original 11 source files and metadata,
  proposal record, Golden Case and activation record are preserved; all seven human fields null.
- New eCFR/annual direct paragraph comparisons: .12 32/32, .202 69/69, .22 102/102, .38 16/16;
  zero non-whitespace mismatches. This is not legal applicability or full cross-reference proof.
- `git diff --check` and `git diff --cached --check`: PASS. All 59 staged raw-source blobs
  match manifest byte lengths and SHA-256. Original metadata/binding interpretations and
  actual activation/Golden/skill bytes match 02904db; production/historical files match origin/main.
- Production code, accepted Sprint 00/01/hardening records, infrastructure and reference artifacts
  remain unchanged. Docker is not rerun for this non-runtime task; no new Docker pass is claimed.
- Existing non-failing warnings: Starlette/httpx deprecation, pytest cache WinError 183,
  Next.js slow filesystem and FORCE_COLOR/NO_COLOR precedence.
- Hosted CI is not claimed: this repository triggers CI on main pushes, PRs or manual dispatch.
  No activation PR/manual run is requested. Publication of this follow-up was stopped by the
  permission review pending explicit approval to upload the planning/evidence files to GitHub.
  The verified changes are retained in a local planning-branch commit; no remote push is claimed.

These checks validate planning evidence and the existing baseline. They do not verify any
production regulatory classifier/calculator, approve source intervals or activate Sprint 02.

### Minimum material source closure (current, 2026-09-10)

The owner approved proceeding to human activation review for the internal V1 prototype, subject
to a narrow material-evidence boundary. This is **not implementation activation**. See
[MATERIAL_SOURCE_CLOSURE.md](MATERIAL_SOURCE_CLOSURE.md) and
[GOLDEN_CASE_SOURCE_BOUNDARY.json](GOLDEN_CASE_SOURCE_BOUNDARY.json).

- **Source side: READY_FOR_HUMAN_REVIEW**, not APPROVED. The earlier documentary block is
  superseded for these explicit facts and this date only.
- Four documentary gaps resolved: institutional counterparty exclusion, PPP exclusion,
  carrying-value/accounting basis, and covered-position/market-risk outer scope.
- Added 12 official raw captures; all 59 earlier captures retained. Total **71** source files.
- SourceManifest v0.4-draft: 8 REQUIRED_AND_RESOLVED; 0 REQUIRED_BUT_UNRESOLVED;
  4 NOT_REQUIRED_FOR_GOLDEN_CASE; 2 DEFERRED_FUTURE_SCOPE groups.
- The new synthetic fact supplement is proposed for the owner's review, not an approved fixture.
  Zero allowance is an explicit educational simplification, not an inferred CECL/GAAP conclusion;
  the gross/net/regulatory carrying-value distinction is documented.
- Source collection stops here unless a material fact/source finding is rejected or changes.
- All source/dependency reviews remain PENDING_REVIEW; every executable flag remains false.
  R-1888 remains PROPOSED / executable=false. Fixed selectors and candidate outputs are unchanged.
- Owner willingness to act as reviewer is recorded, but ACTIVATION_RECORD.json and all seven
  human fields remain unchanged/null. No personal identity, qualification or sign-off is invented.
- Commit 6405e628f4ec365981a32d07cd5c37a4303b73ee was subsequently published with explicit owner
  approval; the preceding historical publication-block note is not the current branch status.
- No activation PR, main merge, production regulatory code or implementation activation.

Verification completed locally on 2026-09-10:

- `node --test sprints/sprint-02/planning-evidence.test.mjs`: PASS, **26** planning-only
  checks. Six new checks cover the minimum boundary, required-dependency removal/downgrade,
  explicit fact omissions/contradictions, individual material-source link removal, PPP edition
  reconciliation, and bounded identity/reporting captures. Readiness cannot imply approval.
- All **71** raw evidence SHA-256/byte-length checks: PASS, including the four new PDFs.
  Every original source record and all 59 earlier raw files match 6405e62 byte-for-byte;
  all original rule bindings, candidate outputs and activation-record bytes are unchanged.
- PPP (a)(36) edition-fragment comparison: identical, 47,441 bytes, documented SHA-256.
  Regulation K eCFR/annual comparison: 58/58 direct paragraphs, zero whitespace-normalized
  differences. Relevant PDF passages, printed dates and footnotes were visually inspected.
- `node scripts/task.mjs verify`: PASS, exit 0. Formatting, ESLint/Ruff, TypeScript/mypy,
  130 finance tests including Hypothesis tests, 5 API tests, 3 web tests, 2 browser tests,
  Next.js production build, API/finance wheel/source builds, and 10 immutable artifact hashes.
- Authored planning-file Prettier checks, JavaScript syntax, local Markdown links/code fences
  and `git diff --check`: PASS.
- Production, accepted fixtures, infrastructure, immutable references and historical Sprint
  00/01/hardening records remain unchanged. No regulatory engine is implemented or tested.
- Docker stack verification was not rerun for this planning-only change. The previously
  recorded local-runtime limitation remains; no fresh Docker pass is claimed.
- Non-failing existing warnings: Starlette/httpx deprecation, pytest cache WinError 183,
  Next.js slow-filesystem detection and FORCE_COLOR/NO_COLOR precedence.
- No new hosted CI run, activation PR or remote publication is claimed for this local closure.
  All checks above are local documentary/baseline checks, not human legal/accounting approval.

## Known limitations and deferred work

### Reusable source-resolver follow-up (02904db; historical)

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
Narrow documentary source closure is ready for human review; final legal/fact/Golden-result
acceptance and executable interval policy remain unapproved. Activation PR creation is not authorized;
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
- [x] Resolve the minimum documentary source dependencies for the fixed synthetic Golden Case.
- [ ] Complete named human source/applicability/fact/result sign-off.
- [ ] Accept proposed ADR 0004 at activation.
- [ ] Approve regulatory sources, interpretations, facts, and golden results.
- [ ] Activate Sprint 02.
- [ ] Accept Sprint 02 implementation.

Named regulatory reviewer/date: PENDING.

SPRINT 02 REMAINS INACTIVE
