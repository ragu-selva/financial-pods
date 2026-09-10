# Sprint 02 Acceptance Criteria — Approved Internal Prototype

Status: ACTIVE

Activation date: 2026-09-10. Human decision: **APPROVED_FOR_INTERNAL_PROTOTYPE**.
Reviewer: **Ragunath Selvaraj — Project Owner / Internal Regulatory Reviewer**.
This is the owner's accountable internal-prototype approval, not independent legal counsel,
regulatory certification, production-bank sign-off or real-bank GAAP certification.

Sprint 02: **ACTIVE** on main through merged PR #4 at
`a89eeb60727c5f615514f75ecc27f57f19ec23cf`. The owner authorized the separate
`codex/sprint-02-us-corporate-engine` implementation branch. Implementation is present;
engineering verification and implementation PR review are recorded in REVIEW.md.
No automatic merge or broader regulatory scope is authorized.

## Activation governance gates — complete

- [x] Explicitly confirmed human reviewer, role/authority, responsibilities, date, decision and
      linked evidence recorded in ACTIVATION_RECORD.json; no AI signature.
- [x] US / FRB / US_FRB_PART217_STANDARDIZED, fixed 2025-01-01, narrow corporate scope approved.
- [x] Exact source versions, paragraph locators, interpretations, hashes and amendment evidence
      approved only for the six rule scopes and eight resolved dependencies; no blanket capture approval.
- [x] Point-in-time applicability approved; unknown endpoints remain UNKNOWN_NOT_OPEN_ENDED.
- [x] Synthetic accounting simplifications, all negative facts, classification, typed measure,
      100% weight, RWA, sole 8% teaching amount and limitations expressly approved.
- [x] ADR 0004 accepted; existing source-resolver responsibility unchanged and approved.
- [x] Source-package version/hash policy and fail-closed selection/design boundary documented.
      Runtime schema/trace verification is recorded separately below.
- [x] Separate activation branch starts from current main; only governance/evidence/tests imported.
- [x] Activation PR #4 reviewed and merged at a89eeb6 before this implementation branch.

The following checkmarks record implemented behavior and engineering verification, not final
human acceptance of the implementation PR. See REVIEW.md for commands, results and limitations.

## Generic architecture and U.S. classification

- [x] Facts, validation, provider/registry, classification, treatment, measure, risk weight, RWA,
      sole teaching output and trace are distinct typed contracts with deterministic orchestration.
- [x] Only USStandardizedRuleset's approved ordinary corporate slice is implemented after activation.
- [x] No borrower/case-name dispatch or scattered jurisdiction conditionals; alternate name/amount
      cases use identical orchestration.
- [x] U.S. corporate status follows the selected 2025 § 217.2 corporate definition and applicable
      Part 217 rules, including all fourteen numbered exclusions and each alternative in paragraph (1).
- [x] Generic retail, specialised lending, BCBS SME and BCBS rating vocabulary cannot independently
      set/veto U.S. corporate status. Any executable mapping requires an approved U.S. rule reference.
- [x] Definition exclusions are separate from treatment exceptions and narrower product-scope guards.
      Unsupported scope must not fabricate a non-corporate legal classification.
- [x] § 217.30(b) scope, § 217.32(f)(2)-(3) exceptions, § 217.32(k), measurement exceptions and
      CRM/guarantee/netting are assessed. No alternative exposure-class calculations.
- [x] Required facts and negative assessments are explicit, provenance-linked and reviewed. Absent,
      unknown, conflicting or out-of-scope facts produce typed errors, never silent defaults.
- [x] Institution/regulator/regime and CBLR not-elected assumption are reviewed, not inferred from names.
- [x] BCBS remains conceptual, with no executable U.S. fallback; other providers, exposure classes,
      core extraction, UI/API/database/tutor/content and Basel/ERBA integration remain future work.

## Measurement, result schema and teaching output

- [x] RegulatoryExposureMeasure has amount, currency, measure_type, measurement_basis, rule_refs,
      warnings. U.S. type is EXPOSURE_AMOUNT; basis is US_STANDARDIZED_CARRYING_VALUE.
- [x] Authoritative RWA uses that measure and risk weight; no ead alias, duplicated authoritative
      exposure_amount output, implicit EAD conversion or advanced-approaches model.
- [x] EAD is only a future measure discriminator where an approved provider actually requires it.
      Invalid provider/type/basis combinations fail.
- [x] GAAP carrying value is reconciled to the approved U.S. definition without double subtraction
      of provisions, allowances or write-offs.
- [x] Result regulatory-calculation.v0.2-draft is finalized as regulatory-calculation.v1: classification, treatment,
      regulatory_exposure_measure, risk_weight, rwa, capital_teaching_outputs, ruleset/rule versions,
      manifest/catalog/input hashes, trace, citations, warnings and exclusions.
- [x] Exact decimal/ratio units remain context-independent; no floating point or implicit rounding.
- [x] Exactly one output: baseline_total_capital_equivalent, ratio 0.08, approved expected USD 800,000.
      No CET1 or Tier 1 educational equivalents; those need later Golden Lesson/UX review.
- [x] It is educational, based on the minimum total-capital ratio, not allocated loan capital,
      an institution-specific capital requirement, or a capital adequacy conclusion.
- [x] Accountable-human-reviewed Golden outputs match U.S. sources, not merely an old BCBS numeric example.

## Effective-dated selection and evidence

- [x] Internal review status is separate from legal CURRENT/PROPOSED/FUTURE/SUPERSEDED.
- [x] Execution requires a reviewed as-of interval, allowed lifecycle, APPROVED and executable=true,
      exact jurisdiction/regime/version, verified source hashes and no ambiguous match.
- [x] R-1888 evidence remains PROPOSED and executable=false, excluded from 2025 execution candidates.
      Direct ID requests, CURRENT aliases and accidental internal approval cannot bypass that exclusion.
- [x] A later final rule is a separately sourced/reviewed/versioned record, never a mutated proposal.
- [x] Future-effective, revoked, unapproved, missing-hash and wrong-as-of candidates fail closed.
- [x] Only the exact version is accepted; CURRENT aliases are rejected. No ambient date or silent upgrades.
- [x] Approved content is immutable; append-only lifecycle history preserves the 2025 decision.

## Trace and reproducibility

- [x] Finalize regulatory-trace.v0.2-draft as regulatory-trace.v1: ordered step ID, operation, rule/version or engine-contract
      ref, reason, source locator, inputs_used, typed output and warnings.
- [x] Measurement step emits the complete typed measure; RWA step references that object and risk_weight,
      never ead. Preserve type, basis, 2025 as-of, exact version, sources and rejected-proposal evidence.
- [x] References resolve to approved U.S. records; BCBS conceptual references are separately labelled.
- [x] Versioned canonical fact/manifest serialization and source-byte hashing are reproducible.
- [x] Failed validation/selection emits a typed failure trace with no successful financial outputs.
- [x] No runtime network, wall-clock, random, database or LLM dependencies in the deterministic core.

## Verification and planned implementation tests

- [x] Implement and pass the negative/property/regression vectors in PLANNED_TESTS.md only after activation.
- [x] Cover proposed-rule direct/alias/approval bypass, dates, conflicts, revoked versions and source tampering.
- [x] Cover all U.S. definition predicates, generic-vocabulary non-interference, typed measure/no-EAD,
      trace binding, exactly one teaching output, immutable results and exact arithmetic.
- [x] Existing Sprint 00 and hardened Sprint 01 tests remain passing.
- [x] Formatting, lint, mypy/TypeScript, tests, builds, artifact hashes and relevant E2E/infra checks
      pass with observed evidence and limitations recorded in REVIEW.md.

Planning/evidence and activation checks validate artifacts, source hashes, scope and approval
consistency only. They do not implement or verify a production selector, classification or calculator.
Sprint 02: ACTIVE. Narrow implementation present; final human implementation acceptance is pending.

- [ ] Human review/acceptance and merge of the implementation PR (never automatic).
- [ ] Local Docker stack-runtime verification once Docker Desktop Linux engine is available.
