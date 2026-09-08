# Sprint 02 Planning Review — Architecture Revision

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
- EAD alias, accounting basis, and final schema/trace/hash policies: PENDING.
- No AI system is designated as the accountable regulatory reviewer.

## Planning changes made

- Replaced a BCBS-first, case-focused proposal with generic orchestration and a U.S. Part 217 provider.
- Made Alpha Manufacturing presentation/fixture data only; required name-invariance and another
  ordinary corporate fixture without changing core orchestration.
- Separated conceptual BCBS authority from executable domestic regulatory authority.
- Defined minimum fact requirements, explicit negative/scope facts, extension points, and typed errors.
- Defined structured classification/result contracts, ratio units, EAD alias proposal, and ordered trace.
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

Primary pages accessed 2026-09-08 are linked in FRAMEWORK_SCOPE.md:
Federal Reserve FRRS Part 217 index; §§ 217.1, 217.2, 217.10, 217.30, 217.31, 217.32;
the Board's March 2026 proposal material; and the official BCBS Framework overview.

The research located candidate U.S. applicability, corporate, measurement, risk-weight, RWA,
and capital-teaching references. It did not approve a legal snapshot or expected result.
Direct eCFR section retrieval failed through the browsing tool; readable official FRRS text was
used as a planning reference. Exact historical/current effective intervals, Federal Register
amendment chains, source-byte hashes, and human interpretation remain activation gates.

The FRRS compilation date is not a paragraph-by-paragraph effective date. The original fixture's
2025-01-01 as-of date must not be conflated with a 2026 retrieval or compilation date.
The proposed 2026 corporate-weight change is explicitly non-executable pending a separately verified,
effective, approved version. No claim is made that this review exhaustively found every amendment.

## Golden Case review checklist

- [ ] In-scope synthetic U.S./FRB institutional perimeter, reporting regime, and CBLR decision.
- [ ] Historical 2025-01-01 rules or an explicitly re-versioned/re-dated scenario.
- [ ] Full corporate-definition exclusion screen and ordinary-loan applicability.
- [ ] Carrying-value reconciliation, adjustments, performance state, and every material assumption.
- [ ] U.S. corporate classification and risk weight.
- [ ] Exposure amount, EAD naming/mapping, and RWA.
- [ ] Educational total-capital equivalent, ratio basis, warnings, and exclusions.
- [ ] Personally named human approval, source/version evidence, and independent expected results.

Any illustrative USD 10 million RWA / USD 800,000 teaching value in the scope document remains
conditional. Matching the old BCBS numeric example cannot substitute for U.S. regulatory review.

## Verification evidence

### Historical evidence, not verification of a Sprint 02 implementation

The 2026-08-27 draft review recorded 41 finance, 5 API, 3 web, and 2 browser tests plus
format/lint/types/builds and 10 artifact hashes passing. Sprint 01 hardening later recorded
130 finance tests and successful hosted CI; its accepted review remains untouched.
These results test the existing baseline, not an implemented U.S. regulatory engine.

### This documentation revision

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

## Known limitations and deferred work

No U.S. executable rules, approved source manifest, new fixture, schemas in production, or engine
implementation exist. Tests described in ACCEPTANCE_CRITERIA.md are future acceptance obligations.
Local Docker's previously recorded runtime limitation is non-blocking for documentation work;
this revision changes no runtime/infrastructure.

BCBS/SAMA/CBUAE providers; broad Basel calculator; bank/retail/mortgage/SME/sovereign/defaulted
and other classes; IRB/ERBA; CCF/CRM; actual capital ratios/adequacy; UI/API/database/AI/content;
and external core extraction are deferred. The owner's existing Basel/ERBA engine has not been
inspected, copied, or evaluated for reuse in this task; that requires a later bounded analysis.

## Decision

- [x] Record the owner-approved architecture direction as planning.
- [ ] Accept proposed ADR 0004 at activation.
- [ ] Approve regulatory sources, interpretations, facts, and golden results.
- [ ] Activate Sprint 02.
- [ ] Accept Sprint 02 implementation.

Named regulatory reviewer/date: PENDING.

SPRINT 02 REMAINS INACTIVE
