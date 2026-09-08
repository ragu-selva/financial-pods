# Sprint 02 Acceptance Criteria — Final Activation Candidate

Status: PLANNING ONLY — NOT ACTIVE

Architecture direction is approved; regulatory interpretation and implementation are not.
All unchecked gates below require evidence. Preparing or testing a draft does not activate Sprint 02.

## Activation and personally accountable review

- [ ] Owner supplies/approves all fields in ACTIVATION_RECORD.json: reviewer_name, reviewer_role,
      reviewer_qualification_or_authority, responsibilities_accepted, review_date, review_decision,
      review_evidence. No AI identity or AI sign-off.
- [ ] Framework, U.S./FRB institution perimeter, regulatory sources, calculation scope, Golden
      assumptions/outputs, exclusions and review process are explicitly approved together.
- [ ] Regulatory/fact date remains 2025-01-01; accepted Sprint 01 fixture and schema are unchanged.
- [ ] Six required point-in-time sections (§§ 217.1, .2, .10, .30, .31, .32), exact locators,
      source bytes/hashes, metadata and relevant Federal Register/LSA amendment chain are reviewed.
- [ ] Legal effective_from/effective_to and lifecycle-as-of are approved. Editorial amendment
      dates, null intervals and a 2026 compilation/retrieval cannot stand in for legal validity.
- [ ] Corporate-definition exclusions, carrying value, measurement, 100% candidate weight, RWA
      and the sole 8% teaching transformation are approved against that dated U.S. authority.
- [ ] Source hash/normalization, result/fact/trace versions and historical selection policy are approved.
- [ ] Only after all prerequisites are complete, prepare codex/sprint-02-activation from current main.
      Include approved documents/evidence, accepted ADR 0004, Golden assumptions/outputs and activation
      decision/status only. No engine code; no wholesale planning-branch merge; no automatic PR merge.
- [ ] Implementation begins only after that activation PR is reviewed and merged, on the separate
      codex/sprint-02-us-corporate-engine branch. Architecture approval alone is not activation.

## Generic architecture and U.S. classification

- [ ] Facts, validation, provider/registry, classification, treatment, measure, risk weight, RWA,
      sole teaching output and trace are distinct typed contracts with deterministic orchestration.
- [ ] Only USStandardizedRuleset's approved ordinary corporate slice is implemented after activation.
- [ ] No borrower/case-name dispatch or scattered jurisdiction conditionals; alternate name/amount
      cases use identical orchestration.
- [ ] U.S. corporate status follows the selected 2025 § 217.2 corporate definition and applicable
      Part 217 rules, including all fourteen numbered exclusions and each alternative in paragraph (1).
- [ ] Generic retail, specialised lending, BCBS SME and BCBS rating vocabulary cannot independently
      set/veto U.S. corporate status. Any executable mapping requires an approved U.S. rule reference.
- [ ] Definition exclusions are separate from treatment exceptions and narrower product-scope guards.
      Unsupported scope must not fabricate a non-corporate legal classification.
- [ ] § 217.30(b) scope, § 217.32(f)(2)-(3) exceptions, § 217.32(k), measurement exceptions and
      CRM/guarantee/netting are assessed. No alternative exposure-class calculations.
- [ ] Required facts and negative assessments are explicit, provenance-linked and reviewed. Absent,
      unknown, conflicting or out-of-scope facts produce typed errors, never silent defaults.
- [ ] Institution/regulator/regime and CBLR not-elected assumption are reviewed, not inferred from names.
- [ ] BCBS remains conceptual, with no executable U.S. fallback; other providers, exposure classes,
      core extraction, UI/API/database/tutor/content and Basel/ERBA integration remain future work.

## Measurement, result schema and teaching output

- [ ] RegulatoryExposureMeasure has amount, currency, measure_type, measurement_basis, rule_refs,
      warnings. U.S. type is EXPOSURE_AMOUNT; basis is US_STANDARDIZED_CARRYING_VALUE.
- [ ] Authoritative RWA uses that measure and risk weight; no ead alias, duplicated authoritative
      exposure_amount output, implicit EAD conversion or advanced-approaches model.
- [ ] EAD is only a future measure discriminator where an approved provider actually requires it.
      Invalid provider/type/basis combinations fail.
- [ ] GAAP carrying value is reconciled to the approved U.S. definition without double subtraction
      of provisions, allowances or write-offs.
- [ ] Result regulatory-calculation.v0.2-draft is finalized/versioned: classification, treatment,
      regulatory_exposure_measure, risk_weight, rwa, capital_teaching_outputs, ruleset/rule versions,
      manifest/catalog/input hashes, trace, citations, warnings and exclusions.
- [ ] Exact decimal/ratio units remain context-independent; no floating point or implicit rounding.
- [ ] Exactly one output: baseline_total_capital_equivalent, ratio 0.08, candidate USD 800,000.
      No CET1 or Tier 1 educational equivalents; those need later Golden Lesson/UX review.
- [ ] It is educational, based on the minimum total-capital ratio, not allocated loan capital,
      an institution-specific capital requirement, or a capital adequacy conclusion.
- [ ] Independently reviewed Golden outputs match U.S. sources, not merely an old BCBS numeric example.

## Effective-dated selection and evidence

- [ ] Internal review status is separate from legal CURRENT/PROPOSED/FUTURE/SUPERSEDED.
- [ ] Execution requires a reviewed as-of interval, allowed lifecycle, APPROVED and executable=true,
      exact jurisdiction/regime/version, verified source hashes and no ambiguous match.
- [ ] R-1888 evidence remains PROPOSED and executable=false, excluded from 2025 execution candidates.
      Direct ID requests, CURRENT aliases and accidental internal approval cannot bypass that exclusion.
- [ ] A later final rule is a separately sourced/reviewed/versioned record, never a mutated proposal.
- [ ] Future-effective, revoked, unapproved, missing-hash and wrong-as-of candidates fail closed.
- [ ] CURRENT aliases resolve to pinned evidence once; no ambient date or silent rule upgrades.
- [ ] Approved content is immutable; append-only lifecycle history preserves the 2025 decision.

## Trace and reproducibility

- [ ] Finalize regulatory-trace.v0.2-draft: ordered step ID, operation, rule/version or engine-contract
      ref, reason, source locator, inputs_used, typed output and warnings.
- [ ] Measurement step emits the complete typed measure; RWA step references that object and risk_weight,
      never ead. Preserve type, basis, 2025 as-of, exact version, sources and rejected-proposal evidence.
- [ ] References resolve to approved U.S. records; BCBS conceptual references are separately labelled.
- [ ] Versioned canonical fact/manifest serialization and source-byte hashing are reproducible.
- [ ] Failed validation/selection emits a typed failure trace with no successful financial outputs.
- [ ] No runtime network, wall-clock, random, database or LLM dependencies in the deterministic core.

## Verification and planned implementation tests

- [ ] Implement and pass the negative/property/regression vectors in PLANNED_TESTS.md only after activation.
- [ ] Cover proposed-rule direct/alias/approval bypass, dates, conflicts, revoked versions and source tampering.
- [ ] Cover all U.S. definition predicates, generic-vocabulary non-interference, typed measure/no-EAD,
      trace binding, exactly one teaching output, immutable results and exact arithmetic.
- [ ] Existing Sprint 00 and hardened Sprint 01 tests remain passing.
- [ ] Formatting, lint, mypy/TypeScript, tests, builds, artifact hashes and relevant E2E/infra checks
      pass with observed evidence and limitations recorded in REVIEW.md.

Planning-evidence tests run now only validate draft artifacts and fail-closed publication constraints.
They do not implement or verify a production ruleset selector or calculator.

SPRINT 02 REMAINS INACTIVE
