# Sprint 03 — Golden Lesson Planning

Status: PLANNING ONLY — NOT ACTIVE

## Goal and authority

Design one read-only learner-facing screen:
**Corporate Exposure — From Loan to Regulatory Capital**.

The owner authorized this planning pack only. Sprint 02 is ACCEPTED AND MERGED by the owner's
confirmed delivery decision; its engine is already on main through PR #5 at 979dda6.
The actual fetched branch baseline and PR #6 observation are recorded in [REVIEW.md](REVIEW.md).
A discrepancy in the cleanup PR's GitHub status does not authorize merging it or changing history.
No Sprint 03 implementation or activation follows from producing or pushing these documents.

## Narrow planned outcome

A banker/analyst follows one synthetic FinBank / Alpha Manufacturing USD 10,000,000 term loan
through facts, U.S. context, corporate classification, regulatory exposure measure, weight, RWA,
educational equivalent and source-linked reasoning. The narrative is Story -> Rule -> Calculation
-> Why -> Source. It is not a raw regulatory-result JSON viewer.

Seven sections are defined in [UX_FLOW.md](UX_FLOW.md). Proposed route:
`/lessons/corporate-exposure`. Reading, expanding explanations and following citations are the only
learner interactions. No editable inputs, scenario controls, jurisdiction selector or progress state.

## Immutable dependency and boundary

Consume the existing pure Python finance engine, accepted ADR 0004 and approved Sprint 02 artifacts.
Exact ruleset: `US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1`.
Jurisdiction US; regulator FRB; standardized approach; regulatory as-of 2025-01-01.

Retain the accepted Golden result:

- CORPORATE.
- EXPOSURE_AMOUNT / US_STANDARDIZED_CARRYING_VALUE, USD 10,000,000.00.
- Risk weight 1.00, presented as 100%.
- RWA USD 10,000,000.00.
- Only baseline_total_capital_equivalent, USD 800,000.00 at 0.08, presented as 8%.
- Twelve ordered source-linked calculation steps; existing warnings/exclusions remain authoritative.
- R-1888 stays PROPOSED/non-executable and cannot influence the lesson.

No formulas, risk-weight tables, classifications or regulatory decisions in React, Next.js or the
presentation mapper. The mapper may format already returned values and translate reviewed labels;
it must not recalculate RWA or the educational amount. No LLM in that path.

## Proposed application boundary

Existing engine -> Python lesson service -> allowlisted presentation DTO -> Next.js server page
-> small disclosure components. See [API_CONTRACT.md](API_CONTRACT.md).

Plan `GET /api/v1/lessons/corporate-exposure/golden-case` in the existing FastAPI application.
One configured Golden Case, no request-supplied regulatory facts or selectors. Next.js fetches it
server-side using the existing server-only API_BASE_URL convention; no second calculator or
duplicate Next.js business endpoint. Existing health contracts and bootstrap behavior stay intact.

Future implementation must address local finance-package installation and access to the unchanged
evidence bundle. Neither is provided by the current API image. These are integration prerequisites,
not authorization for deployment or dependency edits in this planning task.

## Exactly this planning pack

- [SPRINT.md](SPRINT.md): boundary, sequencing and activation gate.
- [UX_FLOW.md](UX_FLOW.md): seven sections, text wireframe, disclosures, accessibility and open UX choices.
- [API_CONTRACT.md](API_CONTRACT.md): application/service ownership, DTO, errors, privacy and integration prerequisites.
- [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md): proposed future implementation proofs and present planning checks.
- [REVIEW.md](REVIEW.md): inspected baseline, actual verification, limitations and pending decisions.

No additional ADR, runtime mock, component, endpoint, schema source file or test implementation is
created now. Accepted ADR 0004 already supplies the relevant dependency direction.

## Explicitly excluded

Do not plan implementation of editable calculators, alternative exposure classes, BCBS/SAMA/CBUAE
calculators, additional rule versions/dates, AI tutor, voice, assessments, mastery/progress, login,
billing, database persistence, content/video publishing or production deployment. No regulatory
source collection, modified Golden Case, revised source approval or new regulatory review authority.
The broader V1 roadmap and old prototype are not scope authorization.

## Proposed sequencing after separate approval

1. Approve the bounded UX, learner copy, public DTO and service/error contract.
2. On a separately authorized implementation branch from then-current main, integrate the accepted
   engine/package/evidence with the minimal lesson service and boundary tests.
3. Add the read-only Next.js screen and accessible disclosures, displaying server values only.
4. Run contract, UI, real-engine integration, browser and unchanged Sprint 02 regression checks.
5. Open an implementation review PR; require human review, not automatic merge.

This is a proposed sequence, not permission to execute it.

## Activation gate and stop condition

Before activation, the owner must explicitly approve this pack, the open UX choices, learner-facing
explanatory copy against existing rule evidence, API exposure/error policy and bounded integration
prerequisites. Do not populate human approval fields from a passing test or an AI-authored draft.
No new regulatory interpretation is requested: contested wording is resolved before implementation.

For this task, verify and push only the five Markdown planning files to
`codex/sprint-03-golden-lesson-planning`. Do not create an activation or implementation PR or merge
this branch. Root/status and all Sprint 02 files remain unchanged.

SPRINT 03 REMAINS INACTIVE
