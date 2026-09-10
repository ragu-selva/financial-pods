# Sprint 03 — Proposed Acceptance Criteria

Status: PLANNING ONLY — NOT ACTIVE

## Present task — documentation only

- Exactly five new Markdown planning files under sprints/sprint-03, linked from [SPRINT.md](SPRINT.md).
- All five prominently state PLANNING ONLY — NOT ACTIVE. No inferred activation or populated approval.
- Branch originates from actual fetched origin/main; record the observed PR #6 discrepancy accurately.
- No production, test, dependency, infrastructure, accepted fixture/source/reviewer or root-status changes.
- Existing repository verification and Sprint 02 evidence checks pass; document warnings/limitations.
- Markdown formatting, local links, contract example syntax and Git whitespace checks pass.
- Push only the planning branch; no activation/implementation PR, merge or Sprint 03 implementation.

## Future implementation — proposals, not completed acceptance

The following criteria become an implementation boundary only after separate explicit approval.
They do not imply that a UI, business API or any Sprint 03 tests exist today.

### 1. One lesson, seven readable sections

- Proposed /lessons/corporate-exposure page renders the seven sections in UX_FLOW.md in order.
- Learner can understand the loan, corporate decision, measure, weight, RWA and educational amount
  without inspecting raw JSON, source hashes, internal field paths or reviewer records.
- FinBank, Alpha Manufacturing, term loan, USD 10,000,000 and as-of 2025-01-01 bind to the accepted case.
- Context clearly says United States / Federal Reserve, dated rules and synthetic education.
- Corporate reasoning, Why 100%?, twelve-step trace and dated source citations are accessible.
- No editable amounts, case/jurisdiction selectors or excluded future-product controls.

### 2. Exact engine-to-API parity

- Real engine integration test invokes the unchanged accepted engine through the lesson service.
- DTO validates CORPORATE; EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE USD 10,000,000.00;
  ratio 1.00; RWA USD 10,000,000.00; only baseline_total_capital_equivalent USD 800,000.00 at 0.08.
- Selected ruleset is exactly US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1. R-1888 remains
  PROPOSED/non-executable. No date/coverage expansion or EAD/CET1/Tier 1 aliases.
- Assert DTO numeric strings equal the actual engine result attributes; do not duplicate formulas
  in a second service calculator to generate the comparison.
- A service/mapper boundary test proves invocation and field projection, not invented static results.
- Verify decimal-safe display formatting under modified Decimal contexts without changing the engine.
- Missing/unverified fixture or evidence, invalid engine response and missing required mapping produce
  sanitized unavailable errors, never a success containing assumed facts or fallback numbers.

### 3. Frontend is presentation only

- Components display server-supplied amount and percentage strings and preserve currency/meaning.
- A test-only valid DTO with USD 5,000,000 RWA / USD 400,000 teaching amount renders those supplied
  values; this is a display-parity test, not an alternate-case public endpoint.
- Component tests can vary server display labels to prove they are consumed, not recreated locally.
- Focused boundary/static checks reject regulatory imports, formulas, weight tables and numeric
  coercion of authoritative financial fields in client code; ordinary layout arithmetic is unrelated.
- Browser assertions verify the full Golden screen against the real Python API/engine, not only a mock.
- No LLM-generated or uncited dynamically invented legal explanations.

### 4. Trace, source fidelity and privacy

- All twelve actual engine trace steps appear in order with reviewed plain-English labels.
- Regulatory steps have their bound rule locators and official dated citations; non-regulatory
  validation steps do not fabricate legal sources.
- Risk-weight explanation names 12 CFR 217.32(f)(1) and preserves required exception-screen context.
- Corporate disclosure covers the accepted definition screen while separating treatment/product guards.
- Citation/trace mapping is complete and source-linked; missing mandatory bindings fail closed.
- DTO, HTML, hydration/RSC data and DOM contain no paths, hashes, reviewer details or manifest internals.
- No arbitrary source HTML, unsafe URL scheme or unapproved source substitution is rendered.

### 5. Educational warnings and resilient UX

- All seven engine warning meanings survive projection.
- The amount section visibly states educational only and all five capital limitations listed in
  UX_FLOW.md, on desktop/mobile, without requiring a disclosure or tooltip.
- Loading, timeout, malformed DTO, missing warnings and non-200 responses never show successful
  financial values; sanitized error and keyboard-operable Retry work.
- Unknown query selectors are rejected; unsupported mutation methods cannot calculate or persist.
- Tests confirm no-store behavior and bounded fetch timeout; no stale/partial result fallback.
- Semantic heading order, keyboard focus, disclosure expansion, readable source links, 320-pixel
  layout and 200% zoom pass. If a drawer is chosen, test focus return and Escape as well.

### 6. Preserve the accepted foundation

- All existing Sprint 02 regulatory/property and earlier domain tests remain unchanged and pass,
  including alternate-name/alternate-amount proofs, exact Decimal behavior and failure guards.
- Approved evidence/fixture/approval bytes and hashes remain unchanged; 35 planning/activation evidence
  checks and 10 immutable reference-artifact checks pass.
- Existing API/web health and bootstrap tests pass, plus new API, component, integration and browser
  tests after activation. Do not replace existing tests with weaker lesson-only coverage.
- node scripts/task.mjs verify passes: formatting, lint, mypy, TypeScript, Python/web tests, builds
  and browser checks. Document exact totals from the future run rather than presupposing them.
- A usable local API+web integration run is required for future acceptance; a Docker runtime pass
  must never be claimed unless actually run. Docker's existing limitation remains documented.
- Changes stay within the approved lesson service/presentation/integration boundary. No regulatory
  engine rewrite, persistence, tutor, video, additional rulesets/classes or production deployment.

Human implementation review and acceptance are still required after these proposed proofs pass.
The current planning verification is recorded separately in [REVIEW.md](REVIEW.md).

SPRINT 03 REMAINS INACTIVE
