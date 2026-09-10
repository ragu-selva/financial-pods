// Planning-only checks. No production ruleset selection, classification or calculation.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync, readdirSync } from "node:fs";
import { dirname, resolve, relative, isAbsolute } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const root = dirname(fileURLToPath(import.meta.url));
const read = (name) => readFileSync(resolve(root, name), "utf8");
const json = (name) => JSON.parse(read(name));
const manifest = json("SOURCE_MANIFEST.json");
const golden = json("GOLDEN_CASE_CANDIDATE.json");
const activation = json("ACTIVATION_RECORD.json");
const boundary = json("GOLDEN_CASE_SOURCE_BOUNDARY.json");
const banner = "PLANNING ONLY — NOT ACTIVE";
const proposalId = "R-1888-PROPOSAL";
const reviewerFields = [
  "reviewer_name",
  "reviewer_role",
  "reviewer_qualification_or_authority",
  "responsibilities_accepted",
  "review_date",
  "review_decision",
  "review_evidence",
];
const allEvidence = [
  ...manifest.sources,
  ...manifest.supporting_evidence,
  ...manifest.proposal_evidence,
];

// This checks a draft evidence list, NOT an executable ruleset registry.
function checkCandidateSources(draft) {
  const records = [
    ...draft.sources,
    ...draft.supporting_evidence,
    ...draft.proposal_evidence,
  ];
  assert.equal(new Set(records.map((x) => x.source_id)).size, records.length);
  assert.equal(new Set(draft.candidate_execution_source_ids).size, 6);
  for (const id of draft.candidate_execution_source_ids) {
    const record = records.find((x) => x.source_id === id);
    assert.ok(record, "Missing evidence record: " + id);
    assert.equal(record.source_kind, "DATED_ECFR_SECTION");
    assert.equal(record.legal_status, "CURRENT");
    assert.equal(record.legal_status_as_of, "2025-01-01");
    assert.equal(record.point_in_time_date, "2025-01-01");
    assert.equal(record.executable, false, "No draft source is executable");
    assert.equal(record.review_status, "PENDING_REVIEW");
  }
  for (const binding of draft.rule_bindings) {
    assert.equal(binding.executable, false);
    for (const id of binding.source_ids) {
      assert.ok(
        draft.candidate_execution_source_ids.includes(id),
        "Rule bound to non-candidate evidence",
      );
    }
  }
}

// Validate the proposed specimen shape; no numeric calculation occurs here.
function checkCandidateResult(result) {
  assert.equal(result.schema_version, "regulatory-calculation.v0.2-draft");
  assert.equal(Object.hasOwn(result, "ead"), false);
  assert.equal(Object.hasOwn(result, "exposure_amount"), false);
  const measure = result.regulatory_exposure_measure;
  assert.deepEqual(
    Object.keys(measure).sort(),
    [
      "amount",
      "currency",
      "measure_type",
      "measurement_basis",
      "rule_refs",
      "warnings",
    ].sort(),
  );
  assert.equal(measure.measure_type, "EXPOSURE_AMOUNT");
  assert.equal(measure.measurement_basis, "US_STANDARDIZED_CARRYING_VALUE");
  assert.equal(measure.amount, "10000000.00");
  assert.equal(measure.currency, "USD");
  assert.deepEqual(measure.rule_refs, ["US-MEASURE"]);
  assert.equal(result.capital_teaching_outputs.length, 1);
  const output = result.capital_teaching_outputs[0];
  assert.equal(output.name, "baseline_total_capital_equivalent");
  assert.equal(output.ratio, "0.08");
  assert.equal(output.amount, "800000.00");
  for (const warning of [
    "EDUCATIONAL_ONLY",
    "NOT_ALLOCATED_LOAN_CAPITAL",
    "NOT_INSTITUTION_SPECIFIC_REQUIREMENT",
    "NOT_CAPITAL_ADEQUACY_CONCLUSION",
  ]) {
    assert.ok(output.warnings.includes(warning));
  }
}

test("all authored controls remain inactive, ADR proposed and reviewer unfilled", () => {
  for (const name of [
    "SPRINT.md",
    "FRAMEWORK_SCOPE.md",
    "ACCEPTANCE_CRITERIA.md",
    "REVIEW.md",
    "SOURCE_REVIEW.md",
    "MATERIAL_SOURCE_CLOSURE.md",
    "PLANNED_TESTS.md",
    "../../docs/adr/0004-generalized-regulatory-engine.md",
  ]) {
    const text = read(name);
    assert.ok(text.split("\n").slice(0, 5).join("\n").includes(banner), name);
    assert.equal((text.match(/^```/gm) ?? []).length % 2, 0, name);
    for (const match of text.matchAll(/```json\r?\n([\s\S]*?)\r?\n```/g))
      JSON.parse(match[1]);
  }
  assert.ok(
    read("../../docs/adr/0004-generalized-regulatory-engine.md").includes(
      "Status: PROPOSED",
    ),
  );
  for (const record of [manifest, golden, activation, boundary])
    assert.equal(record.status, banner);
  for (const field of reviewerFields)
    assert.equal(activation[field], null, field);
  assert.equal(activation.activation_status, "BLOCKED");
  assert.equal(activation.activation_pr.created, false);
  assert.equal(activation.activation_pr.merged, false);
  assert.equal(activation.implementation.authorized, false);
});

test("six dated sections and every captured evidence hash are intact", () => {
  assert.deepEqual(
    manifest.sources.map((x) => x.section).sort(),
    ["217.1", "217.2", "217.10", "217.30", "217.31", "217.32"].sort(),
  );
  for (const item of allEvidence) {
    const path = resolve(root, item.local_path);
    const rel = relative(resolve(root, "evidence"), path);
    assert.ok(
      !rel.startsWith("..") && !isAbsolute(rel),
      "Evidence path outside capture directory",
    );
    const bytes = readFileSync(path);
    assert.equal(bytes.length, item.byte_length, item.source_id);
    assert.equal(
      createHash("sha256").update(bytes).digest("hex"),
      item.content_sha256,
      item.source_id,
    );
    if (item.source_kind === "DATED_ECFR_SECTION") {
      assert.ok(bytes.toString("utf8").includes('N="' + item.section + '"'));
      assert.ok(item.retrieval_url.includes("/full/2025-01-01/"));
      assert.equal(item.effective_interval_status, "PENDING");
      assert.equal(item.effective_from, null);
      assert.equal(item.effective_to, null);
      assert.equal(item.reviewer_name, null);
    }
  }
  const files = readdirSync(resolve(root, "evidence"), { recursive: true })
    .map((x) => x.replaceAll("\\", "/"))
    .filter((x) => /\.(xml|json|txt|pdf)$/.test(x));
  assert.equal(files.length, allEvidence.length, "Unregistered raw evidence");
  assert.ok(read("evidence/.gitattributes").includes("* -text"));
});

test("candidate list uses only the dated U.S. sections; proposal stays separate", () => {
  checkCandidateSources(manifest);
  assert.equal(manifest.executable, false);
  const proposal = manifest.proposal_evidence.find(
    (x) => x.source_id === proposalId,
  );
  assert.equal(proposal.legal_status, "PROPOSED");
  assert.equal(proposal.executable, false);
  assert.ok(!manifest.candidate_execution_source_ids.includes(proposalId));
});

test("planning check rejects proposal injected directly into source candidates", () => {
  const unsafe = structuredClone(manifest);
  unsafe.candidate_execution_source_ids[0] = proposalId;
  assert.throws(() => checkCandidateSources(unsafe));
});

test("planning check rejects CURRENT alias substitution and accidental internal approval", () => {
  const unsafe = structuredClone(manifest);
  const proposal = unsafe.proposal_evidence[0];
  proposal.source_id = unsafe.sources[0].source_id;
  unsafe.sources.shift();
  proposal.legal_status = "CURRENT";
  proposal.review_status = "APPROVED";
  proposal.executable = true;
  assert.throws(() => checkCandidateSources(unsafe));
});

test("planning check rejects a rule binding to separate proposal evidence", () => {
  const unsafe = structuredClone(manifest);
  unsafe.rule_bindings[0].source_ids = [proposalId];
  assert.throws(() => checkCandidateSources(unsafe));
});

test("Golden Case date and accepted Sprint 01 bytes remain unchanged", () => {
  assert.equal(golden.context.regulatory_as_of, "2025-01-01");
  assert.equal(golden.accepted_fixture.regulatory_fact_snapshot, "2025-01-01");
  const fixture = readFileSync(
    resolve(root, golden.accepted_fixture.path),
    "utf8",
  ).replaceAll("\r\n", "\n");
  assert.equal(
    createHash("sha256").update(fixture, "utf8").digest("hex"),
    golden.accepted_fixture.sha256,
  );
  assert.equal(golden.candidate_facts.institution.cblr_elected, false);
  const exposure = golden.candidate_facts.exposure;
  assert.equal(exposure.past_due, false);
  assert.equal(exposure.days_past_due, 0);
  assert.equal(exposure.nonaccrual, false);
  assert.equal(exposure.gaap_carrying_value, "10000000.00");
  assert.equal(golden.review_status, "PENDING_REVIEW");
  assert.equal(golden.executable, false);
});

test("candidate screen maps fourteen U.S. definition paragraphs, not generic concepts", () => {
  const screen = golden.candidate_facts.definition_screen;
  assert.equal(screen.length, 14);
  assert.deepEqual(
    screen.map((x) => x.assessment_id),
    Array.from(
      { length: 14 },
      (_, i) => "US-CORP-" + String(i + 1).padStart(2, "0"),
    ),
  );
  assert.equal(screen[0].alternative_assessments.length, 12);
  for (const item of screen) {
    assert.equal(item.rule_ref, "US-CLASS");
    assert.equal(item.reviewer_evidence, null);
    for (const alternative of item.alternative_assessments) {
      assert.equal(alternative.candidate_outcome, "NO");
      assert.equal(alternative.review_status, "PENDING_REVIEW");
      assert.ok(!/retail|specialised|sme|rating/.test(alternative.concept));
    }
  }
});

test("candidate result uses the typed U.S. measure and only the total-capital teaching output", () => {
  checkCandidateResult(golden.candidate_result);
  assert.equal(golden.candidate_result.risk_weight.value, "1.00");
  assert.equal(golden.candidate_result.rwa.amount, "10000000.00");
  for (const field of [
    "ruleset_version",
    "rule_versions",
    "manifest_hash",
    "catalog_snapshot_id",
    "input_snapshot_hash",
    "calculation_trace",
  ]) {
    assert.equal(
      golden.candidate_result[field],
      null,
      "Do not fabricate runtime evidence",
    );
  }
});

test("planning specimen check rejects EAD aliases, EAD type and incompatible basis", () => {
  for (const mutate of [
    (x) => {
      x.ead = { amount: "10000000.00", currency: "USD" };
    },
    (x) => {
      x.exposure_amount = x.regulatory_exposure_measure;
    },
    (x) => {
      x.regulatory_exposure_measure.measure_type = "EAD";
    },
    (x) => {
      x.regulatory_exposure_measure.measurement_basis = "UNAPPROVED_BASIS";
    },
  ]) {
    const unsafe = structuredClone(golden.candidate_result);
    mutate(unsafe);
    assert.throws(() => checkCandidateResult(unsafe));
  }
});

test("planning specimen check rejects CET1 and Tier 1 teaching expansion", () => {
  for (const name of ["cet1_equivalent", "tier1_equivalent"]) {
    const unsafe = structuredClone(golden.candidate_result);
    unsafe.capital_teaching_outputs.push({
      ...unsafe.capital_teaching_outputs[0],
      name,
    });
    assert.throws(() => checkCandidateResult(unsafe));
  }
});

test("trace planning binds RWA to the typed measure; runtime tests remain deferred", () => {
  const scope = read("FRAMEWORK_SCOPE.md");
  assert.ok(scope.includes("regulatory-trace.v0.2-draft"));
  assert.ok(
    scope.includes(
      "Step 8 inputs_used names regulatory_exposure_measure and risk_weight",
    ),
  );
  assert.ok(
    read("PLANNED_TESTS.md").includes("AFTER activation (NOT IMPLEMENTED)"),
  );
  assert.ok(
    read("SPRINT.md").includes(
      "Only after review and merge may implementation start",
    ),
  );
});

function checkParagraphEvidence(draft) {
  assert.equal(draft.schema_version, "source-review-manifest.v0.4-draft");
  assert.equal(draft.regulatory_as_of, "2025-01-01");
  checkMinimumBoundary(draft, boundary);
  const records = [...draft.sources, ...draft.supporting_evidence];
  const sourceIds = new Set(records.map((x) => x.source_id));
  const lineageIds = new Set(draft.paragraph_lineage.map((x) => x.lineage_id));
  assert.equal(lineageIds.size, draft.paragraph_lineage.length);
  const dependencyIds = new Set(
    draft.dependency_inventory.map((x) => x.dependency_id),
  );
  assert.equal(dependencyIds.size, draft.dependency_inventory.length);
  const validDate = (value) =>
    typeof value === "string" &&
    /^\d{4}-\d{2}-\d{2}$/.test(value) &&
    !Number.isNaN(Date.parse(value)) &&
    new Date(value).toISOString().slice(0, 10) === value;
  const checkPending = (x) => {
    assert.equal(x.review_status, "PENDING_REVIEW");
    assert.equal(x.executable, false);
  };
  for (const x of draft.paragraph_lineage) {
    checkPending(x);
    assert.ok(sourceIds.has(x.source_id));
    assert.equal(x.legal_status, "CURRENT");
    assert.equal(x.legal_status_as_of, "2025-01-01");
    assert.ok(validDate(x.effective_from));
    assert.ok(x.effective_from <= "2025-01-01");
    assert.equal(x.effective_to, null);
    assert.equal(x.effective_to_status, "UNKNOWN_NOT_OPEN_ENDED");
    assert.equal(x.documentary_coverage_through, "2025-01-01");
    assert.equal(x.reviewer_name, null);
    assert.equal(x.review_date, null);
    assert.equal(x.review_evidence, null);
    assert.ok(x.paragraph_locator.length > 0);
    assert.ok(x.amendment_events.length > 0);
    for (const event of x.amendment_events) {
      checkPending(event);
      assert.ok(sourceIds.has(event.source_id));
      assert.ok(validDate(event.publication_date));
      assert.ok(validDate(event.stated_effective_date));
      assert.ok(event.evidence_locator.length > 0);
    }
  }
  for (const x of draft.dependency_inventory) {
    checkPending(x);
    assert.ok(
      [
        "REQUIRED_AND_RESOLVED",
        "REQUIRED_BUT_UNRESOLVED",
        "NOT_REQUIRED_FOR_GOLDEN_CASE",
        "DEFERRED_FUTURE_SCOPE",
      ].includes(x.classification),
    );
    assert.equal(x.classification_is_candidate, true);
    assert.ok(x.scope.length > 0);
    for (const id of x.source_ids) assert.ok(sourceIds.has(id));
    if (x.lineage_id !== null) assert.ok(lineageIds.has(x.lineage_id));
  }
  for (const x of draft.rule_bindings) {
    checkPending(x);
    assert.ok(validDate(x.effective_from));
    assert.equal(x.effective_to, null);
    assert.equal(x.effective_to_status, "UNKNOWN_NOT_OPEN_ENDED");
    assert.equal(x.documentary_coverage_through, "2025-01-01");
    for (const id of x.paragraph_lineage_ids) assert.ok(lineageIds.has(id));
    for (const id of x.dependency_ids) assert.ok(dependencyIds.has(id));
  }
  for (const x of [
    ...draft.sources,
    ...draft.supporting_evidence,
    ...draft.proposal_evidence,
  ])
    checkPending(x);
}

test("paragraph review dates are bounded documentary evidence, not approved selection", () => {
  checkParagraphEvidence(manifest);
  const byId = Object.fromEntries(
    manifest.paragraph_lineage.map((x) => [x.lineage_id, x]),
  );
  for (const [id, date] of Object.entries({
    "P-INSTITUTION": "2024-01-01",
    "P-CORPORATE": "2020-04-13",
    "P-CARRYING": "2019-07-01",
    "P-EXPOSURE-AMOUNT": "2014-01-01",
    "P-STANDARDIZED-SCOPE": "2014-01-01",
    "P-CORPORATE-WEIGHT": "2020-09-17",
    "P-RWA": "2014-01-01",
    "P-TEACHING-SOURCE": "2020-01-01",
    "P-PAST-DUE": "2019-10-01",
    "P-CBLR-ELECTION": "2020-01-01",
  }))
    assert.equal(byId[id].effective_from, date);
});

test("review rejects invented open-ended or as-of-as-expiry intervals", () => {
  for (const change of [
    (x) => {
      x.paragraph_lineage[0].effective_to_status = "OPEN_ENDED";
    },
    (x) => {
      x.paragraph_lineage[0].effective_to = "2025-01-02";
    },
    (x) => {
      x.paragraph_lineage[0].effective_from = "2024-02-30";
    },
    (x) => {
      x.rule_bindings[0].effective_to_status = "OPEN_ENDED";
    },
    (x) => {
      x.rule_bindings[0].effective_to = "2025-01-01";
    },
  ]) {
    const unsafe = structuredClone(manifest);
    change(unsafe);
    assert.throws(() => checkParagraphEvidence(unsafe));
  }
});

test("review rejects proposal injection into paragraph or dependency evidence", () => {
  for (const change of [
    (x) => {
      x.paragraph_lineage[0].source_id = proposalId;
    },
    (x) => {
      x.paragraph_lineage[0].amendment_events[0].source_id = proposalId;
    },
    (x) => {
      x.dependency_inventory[0].source_ids = [proposalId];
    },
    (x) => {
      x.rule_bindings[0].paragraph_lineage_ids = ["MISSING"];
    },
    (x) => {
      x.rule_bindings[0].dependency_ids = ["MISSING"];
    },
  ]) {
    const unsafe = structuredClone(manifest);
    change(unsafe);
    assert.throws(() => checkParagraphEvidence(unsafe));
  }
});

test("review rejects approval or execution before dependency and human gates close", () => {
  for (const change of [
    (x) => {
      x.paragraph_lineage[0].executable = true;
    },
    (x) => {
      x.paragraph_lineage[0].amendment_events[0].review_status = "APPROVED";
    },
    (x) => {
      x.dependency_inventory[0].review_status = "APPROVED";
    },
    (x) => {
      x.rule_bindings[0].review_status = "APPROVED";
    },
    (x) => {
      x.source_readiness = "APPROVED";
    },
  ]) {
    const unsafe = structuredClone(manifest);
    change(unsafe);
    assert.throws(() => checkParagraphEvidence(unsafe));
  }
});

test("known delays, corrections and expired relief retain distinct dates", () => {
  const source = (id) => allEvidence.find((x) => x.source_id === id);
  assert.match(
    read(source("FR-2019-06011").local_path),
    /delayed until July 1, 2019/,
  );
  assert.match(
    read(source("FR-2020-17744").local_path),
    /paragraphs \(f\)\(2\) and \(f\)\(3\)/,
  );
  assert.match(
    read(source("FR-2020-06755").local_path),
    /effective\s+date will remain April 1, 2020/,
  );
  assert.match(read(source("FR-2020-21894").local_path), /without change/);
  const expiry = manifest.interval_contract.bounded_expiry_example;
  assert.equal(expiry.effective_from, "2020-12-02");
  assert.equal(expiry.stated_last_day, "2021-12-31");
  assert.equal(expiry.effective_to, "2022-01-01");
  assert.equal(expiry.effective_to_status, "ESTABLISHED_EXCLUSIVE_SUNSET");
  assert.equal(expiry.executable, false);
});

test("new required dependency sections are dated captures, not proposal or URL-only evidence", () => {
  for (const [id, section] of [
    ["DEP-CBLR", "217.12"],
    ["DEP-COVERED-POSITION", "217.202"],
    ["DEP-UNSETTLED", "217.38"],
  ]) {
    const dependency = manifest.dependency_inventory.find(
      (x) => x.dependency_id === id,
    );
    assert.equal(dependency.classification, "REQUIRED_AND_RESOLVED");
    const sourceId = "US-DEPENDENCY-" + section;
    assert.ok(dependency.source_ids.includes(sourceId));
    const source = allEvidence.find((x) => x.source_id === sourceId);
    assert.equal(source.source_kind, "DATED_ECFR_SECTION");
    assert.equal(source.point_in_time_date, "2025-01-01");
    assert.equal(source.review_status, "PENDING_REVIEW");
    assert.equal(source.executable, false);
  }
  for (const id of [
    "DEP-EXTERNAL-IDENTITY",
    "DEP-PPP",
    "DEP-REPORTING-ACCOUNTING",
  ])
    assert.equal(
      manifest.dependency_inventory.find((x) => x.dependency_id === id)
        .classification,
      "REQUIRED_AND_RESOLVED",
    );
});

test("annual Title 12 LSA evidence excludes proposals and old Regulation Q identity", () => {
  const index = json(
    allEvidence.find((x) => x.source_id === "FR-PART217-FINAL-RULE-INDEX")
      .local_path,
  );
  assert.equal(index.count, 56);
  assert.ok(index.next_page_url == null);
  assert.ok(index.results.some((x) => x.document_number === "2020-17744"));
  for (const id of manifest.amendment_chain_screen.excluded_regime_documents)
    assert.ok(index.results.some((x) => x.document_number === id));
  for (let year = 2013; year <= 2024; year++) {
    const source = allEvidence.find(
      (x) => x.source_id === `LSA-${year}-12-TITLE12`,
    );
    assert.match(read(source.local_path), /TITLE 12_BANKS AND BANKING/);
  }
});

test("activation record is preserved and source review distinguishes readiness from approval", () => {
  // Authored JSON may receive checkout CRLF; raw regulatory evidence is never normalized.
  // The task also separately audits actual working-tree bytes against the original Git blob.
  const bytes = Buffer.from(
    read("ACTIVATION_RECORD.json").replaceAll("\r\n", "\n"),
    "utf8",
  );
  assert.equal(
    createHash("sha256").update(bytes).digest("hex"),
    "4af225c03848aa361fcd0efae64c61e565c9e21497eb224b3d2b5fc135fc014c",
  );
  const review = read("SOURCE_REVIEW.md");
  for (const heading of [
    "Resolved documentary evidence",
    "Remaining human/legal-review items",
    "Activation readiness",
  ])
    assert.ok(review.includes("## " + heading));
  assert.ok(review.includes("Source-side status: **READY_FOR_HUMAN_REVIEW**"));
  assert.ok(review.includes("SPRINT 02 REMAINS INACTIVE"));
});

// Exact planning specimen assertions, not a reusable regulatory fact validator.
const expectedBoundaryFacts = {
  institution: {
    state_member_bank: true,
    frb_supervised: true,
    standardized_reporting: true,
    cblr_elected: false,
    cblr_ever_elected: false,
    cblr_grace_period: false,
    call_report_not_holding_company_report: true,
  },
  counterparty: {
    legal_form: "DOMESTIC_PRIVATE_FOR_PROFIT_CORPORATION",
    organized_in: "US",
    business_activity: "MANUFACTURE_AND_SALE_OF_PHYSICAL_GOODS",
    banking_business: false,
    receives_deposits: false,
    power_to_accept_demand_deposits: false,
    national_or_state_bank_or_banking_association: false,
    trust_savings_or_industrial_bank: false,
    federal_or_state_savings_association: false,
    former_savings_association: false,
    joint_agency_savings_association_determination: false,
    foreign_bank_or_bank_branch_or_agency: false,
    recognized_as_bank_by_supervisor: false,
    federal_or_state_credit_union_charter: false,
    member_thrift_credit_cooperative: false,
    government_or_political_subdivision: false,
    government_established_or_chartered_public_purpose_enterprise: false,
    multilateral_or_supranational_institution: false,
    central_bank: false,
  },
  ppp: {
    ppp_loan: false,
    originated_under_15_usc_636_a_36: false,
    originated_under_15_usc_636_a_37: false,
    sba_program_loan: false,
    ppp_refinancing_or_acquired_ppp_loan: false,
  },
  accounting: {
    accounting_basis: "US_GAAP",
    originated_by_finbank: true,
    acquired_loan: false,
    held_for_investment: true,
    intent_and_ability_to_hold: true,
    held_for_sale: false,
    measurement: "AMORTIZED_COST",
    fair_value_option: false,
    pcd: false,
    legacy_pci_pool: false,
    afs_debt_security: false,
    htm_debt_security: false,
    preferred_security: false,
    original_principal: "10000000.00",
    outstanding_principal: "10000000.00",
    principal_repayments: "0.00",
    accrued_interest_receivable: "0.00",
    unamortized_premium: "0.00",
    unamortized_discount: "0.00",
    unamortized_deferred_fees: "0.00",
    unamortized_deferred_costs: "0.00",
    full_charge_offs: "0.00",
    partial_write_offs: "0.00",
    credit_loss_allowance: "0.00",
    specific_provisions: "0.00",
    allocated_transfer_risk_reserve: "0.00",
    foreign_exchange_adjustments: "0.00",
    fair_value_hedge_adjustments: "0.00",
    other_carrying_value_adjustments: "0.00",
    currency: "USD",
    gross_amortized_cost: "10000000.00",
    net_balance_sheet_amount_candidate: "10000000.00",
    gaap_based_regulatory_carrying_value_candidate: "10000000.00",
  },
  market_risk: {
    bank_functional_currency: "USD",
    loan_currency: "USD",
    short_term_resale_intent: false,
    short_term_price_profit_intent: false,
    arbitrage_intent: false,
    market_making_or_customer_trading_accommodation: false,
    managed_as_trading: false,
    reported_as_trading_asset: false,
    hedges_another_covered_position: false,
    foreign_exchange_position: false,
    commodity_position: false,
    securities_lending_or_repo_position: false,
    embedded_derivative: false,
  },
  other_scope: {
    fully_drawn: true,
    on_balance_sheet: true,
    off_balance_sheet: false,
    undrawn_amount: "0.00",
    security_or_fx_or_commodity_settlement_trade: false,
    unsettled_transaction: false,
    ccp_or_clearing_member_transaction: false,
    cash_collateral_to_ccp: false,
    cleared_transaction: false,
    default_fund_contribution: false,
    derivative: false,
    repo_style_transaction: false,
    eligible_margin_loan: false,
    collateral: false,
    guarantee: false,
    netting: false,
    crm_recognition: false,
    real_estate_collateral: false,
    real_estate_acquisition_development_or_construction_purpose: false,
    securitization_or_tranching: false,
    equity_or_equity_linked_return: false,
    policy_loan: false,
    separate_account: false,
    days_past_due: 0,
    nonaccrual: false,
    defaulted: false,
  },
};

function checkFactBoundary(facts) {
  assert.equal(facts.status, banner);
  assert.equal(facts.schema_version, "golden-source-boundary.v0.1-draft");
  assert.equal(facts.review_status, "PENDING_REVIEW");
  assert.equal(facts.executable, false);
  assert.deepEqual(facts.context, {
    as_of_date: "2025-01-01",
    jurisdiction: "US",
    regulator: "FRB",
    ruleset_family: "US_FRB_PART217_STANDARDIZED",
  });
  assert.equal(
    facts.provenance.kind,
    "PROPOSED_SYNTHETIC_FACTS_FOR_OWNER_REVIEW",
  );
  assert.equal(facts.provenance.human_approved, false);
  for (const field of ["reviewer_name", "review_date", "review_evidence"])
    assert.equal(facts.provenance[field], null);
  assert.deepEqual(
    Object.keys(facts.fact_groups).sort(),
    Object.keys(expectedBoundaryFacts).sort(),
  );
  for (const [name, expected] of Object.entries(expectedBoundaryFacts)) {
    assert.deepEqual(
      facts.fact_groups[name].facts,
      expected,
      name + ": no missing/defaulted material facts",
    );
    assert.ok(facts.fact_groups[name].note.length > 0);
  }
  assert.match(facts.fact_groups.accounting.note, /NOT a CECL estimate/);
  assert.match(
    facts.missing_or_changed_fact_policy,
    /No material field may be silently defaulted/,
  );
}

function checkMinimumBoundary(draft, facts) {
  checkFactBoundary(facts);
  assert.equal(draft.status, banner);
  assert.equal(draft.executable, false);
  assert.equal(draft.approval_status, "PENDING_REVIEW");
  const required = [
    "DEP-CBLR",
    "DEP-COVERED-POSITION",
    "DEP-UNSETTLED",
    "DEP-EXTERNAL-IDENTITY",
    "DEP-PPP",
    "DEP-REPORTING-ACCOUNTING",
    "DEP-PAST-DUE",
    "DEP-INSTITUTION",
  ];
  const notRequired = [
    "DEP-AOCI",
    "DEP-QCCP",
    "DEP-CRM-DERIVATIVES",
    "DEP-OTHER-CLASSES",
  ];
  const deferred = [
    "DEP-FUTURE-POSITIVE-TREATMENTS",
    "DEP-OTHER-DATES-AND-JURISDICTIONS",
  ];
  const inventory = draft.dependency_inventory;
  assert.deepEqual(
    inventory.map((x) => x.dependency_id).sort(),
    [...required, ...notRequired, ...deferred].sort(),
  );
  const closure = draft.material_closure;
  assert.equal(closure.version, "minimum-dependency-boundary.v0.1-draft");
  assert.equal(closure.documentary_as_of, "2025-01-01");
  assert.equal(closure.fact_boundary_file, "GOLDEN_CASE_SOURCE_BOUNDARY.json");
  assert.equal(closure.evidence_review_file, "MATERIAL_SOURCE_CLOSURE.md");
  assert.equal(closure.review_status, "PENDING_REVIEW");
  assert.equal(closure.executable, false);
  assert.deepEqual(
    [...closure.required_dependency_ids].sort(),
    [...required].sort(),
  );
  const sourceIds = new Set(
    [...draft.sources, ...draft.supporting_evidence].map((x) => x.source_id),
  );
  const requiredSourceLinks = {
    "DEP-CBLR": ["US-DEPENDENCY-217.12"],
    "DEP-COVERED-POSITION": [
      "US-DEPENDENCY-217.202",
      "FFIEC-RCD-2020-09",
      "FFIEC-GLOSSARY-2024-06",
      "FFIEC-2024-12-UPDATES",
    ],
    "DEP-UNSETTLED": ["US-DEPENDENCY-217.38"],
    "DEP-EXTERNAL-IDENTITY": [
      "US-DEFINITIONS",
      "USC-2024-12-1813",
      "US-INCORPORATED-211.2",
      "GOVINFO-2025-211.2",
      "USC-2024-12-1752",
    ],
    "DEP-PPP": ["US-DEFINITIONS", "USC-2023-15-636", "USC-2024-15-636"],
    "DEP-REPORTING-ACCOUNTING": [
      "US-DEFINITIONS",
      "FFIEC-GLOSSARY-2024-06",
      "FFIEC-RC-2024-03",
      "FDIC-2024-06-INSTRUCTIONS-INDEX",
      "FDIC-2024-12-INDEX",
      "FFIEC-2024-12-UPDATES",
    ],
    "DEP-PAST-DUE": ["US-WEIGHT-TREATMENT"],
    "DEP-INSTITUTION": ["US-SCOPE-INSTITUTION", "US-DEFINITIONS"],
  };
  for (const id of closure.new_source_ids) assert.ok(sourceIds.has(id));
  assert.equal(new Set(closure.new_source_ids).size, 12);
  const unresolved = [];
  for (const item of inventory) {
    assert.equal(item.review_status, "PENDING_REVIEW");
    assert.equal(item.executable, false);
    assert.equal(item.documentary_as_of, "2025-01-01");
    assert.equal(item.closure_evidence, "MATERIAL_SOURCE_CLOSURE.md");
    assert.ok(item.scope.length > 0);
    for (const id of item.source_ids) assert.ok(sourceIds.has(id), id);
    for (const group of item.fact_group_refs) {
      assert.ok(facts.fact_groups[group]);
      assert.ok(
        facts.fact_groups[group].dependency_ids.includes(item.dependency_id),
      );
    }
    if (required.includes(item.dependency_id)) {
      for (const id of requiredSourceLinks[item.dependency_id])
        assert.ok(
          item.source_ids.includes(id),
          "Missing material source link: " + id,
        );
      assert.ok(
        ["REQUIRED_AND_RESOLVED", "REQUIRED_BUT_UNRESOLVED"].includes(
          item.classification,
        ),
      );
      assert.ok(item.fact_group_refs.length > 0);
      assert.ok(item.source_ids.length > 0);
      if (item.classification === "REQUIRED_BUT_UNRESOLVED")
        unresolved.push(item.dependency_id);
    } else if (notRequired.includes(item.dependency_id)) {
      assert.equal(item.classification, "NOT_REQUIRED_FOR_GOLDEN_CASE");
      assert.ok(
        item.fact_group_refs.length > 0,
        "A conditional exclusion must retain its fact gate",
      );
    } else assert.equal(item.classification, "DEFERRED_FUTURE_SCOPE");
  }
  assert.deepEqual(
    [...closure.required_but_unresolved_ids].sort(),
    unresolved.sort(),
  );
  assert.equal(
    draft.source_readiness,
    unresolved.length ? "BLOCKED_ON_SOURCE_EVIDENCE" : "READY_FOR_HUMAN_REVIEW",
  );
  assert.equal(
    draft.resolution_status,
    unresolved.length ? "UNRESOLVED" : "RESOLVED_FOR_NARROW_GOLDEN_CASE",
  );
  if (!unresolved.length) assert.deepEqual(draft.unresolved_evidence, []);
}

test("minimum evidence boundary is ready for human review, never approved", () => {
  checkMinimumBoundary(manifest, boundary);
  assert.equal(manifest.source_readiness, "READY_FOR_HUMAN_REVIEW");
  assert.deepEqual(manifest.material_closure.required_but_unresolved_ids, []);
});

test("readiness fails closed for a missing, downgraded or unresolved required dependency", () => {
  for (const mutate of [
    (x) => {
      x.dependency_inventory = x.dependency_inventory.filter(
        (y) => y.dependency_id !== "DEP-PPP",
      );
    },
    (x) => {
      x.dependency_inventory.find(
        (y) => y.dependency_id === "DEP-PPP",
      ).classification = "NOT_REQUIRED_FOR_GOLDEN_CASE";
    },
    (x) => {
      x.dependency_inventory.find(
        (y) => y.dependency_id === "DEP-PPP",
      ).classification = "REQUIRED_BUT_UNRESOLVED";
    },
    (x) => {
      x.dependency_inventory.find(
        (y) => y.dependency_id === "DEP-PPP",
      ).source_ids = [];
    },
    (x) => {
      x.dependency_inventory.find(
        (y) => y.dependency_id === "DEP-AOCI",
      ).fact_group_refs = [];
    },
    (x) => {
      x.dependency_inventory.find(
        (y) => y.dependency_id === "DEP-PPP",
      ).source_ids = [proposalId];
    },
    (x) => {
      x.material_closure.executable = true;
    },
    (x) => {
      x.approval_status = "APPROVED";
    },
  ]) {
    const changed = structuredClone(manifest);
    mutate(changed);
    assert.throws(() => checkMinimumBoundary(changed, boundary));
  }
  const reopened = structuredClone(manifest);
  reopened.dependency_inventory.find(
    (y) => y.dependency_id === "DEP-PPP",
  ).classification = "REQUIRED_BUT_UNRESOLVED";
  reopened.material_closure.required_but_unresolved_ids = ["DEP-PPP"];
  reopened.source_readiness = "BLOCKED_ON_SOURCE_EVIDENCE";
  reopened.resolution_status = "UNRESOLVED";
  reopened.unresolved_evidence = ["A reviewer reopens PPP provenance"];
  checkMinimumBoundary(reopened, boundary);
});

test("material fact omissions, changed facts, dates and invented approval are rejected", () => {
  for (const mutate of [
    (x) => {
      delete x.fact_groups.ppp.facts.ppp_loan;
    },
    (x) => {
      x.fact_groups.counterparty.facts.receives_deposits = true;
    },
    (x) => {
      x.fact_groups.accounting.facts.credit_loss_allowance = "1.00";
    },
    (x) => {
      delete x.fact_groups.accounting.facts.unamortized_deferred_fees;
    },
    (x) => {
      x.fact_groups.accounting.facts.pcd = true;
    },
    (x) => {
      x.fact_groups.market_risk.facts.hedges_another_covered_position = true;
    },
    (x) => {
      x.fact_groups.market_risk.facts.foreign_exchange_position = true;
    },
    (x) => {
      x.fact_groups.institution.facts.cblr_grace_period = true;
    },
    (x) => {
      x.context.as_of_date = "2025-01-06";
    },
    (x) => {
      x.provenance.human_approved = true;
    },
    (x) => {
      x.provenance.reviewer_name = "Invented reviewer";
    },
  ]) {
    const changed = structuredClone(boundary);
    mutate(changed);
    assert.throws(() => checkMinimumBoundary(manifest, changed));
  }
});

test("ready evidence cannot lose an individual incorporated-source or accounting-version link", () => {
  for (const [dependency, source] of [
    ["DEP-EXTERNAL-IDENTITY", "US-INCORPORATED-211.2"],
    ["DEP-PPP", "USC-2023-15-636"],
    ["DEP-REPORTING-ACCOUNTING", "FFIEC-2024-12-UPDATES"],
    ["DEP-COVERED-POSITION", "FFIEC-RCD-2020-09"],
  ]) {
    const changed = structuredClone(manifest);
    const item = changed.dependency_inventory.find(
      (x) => x.dependency_id === dependency,
    );
    item.source_ids = item.source_ids.filter((x) => x !== source);
    assert.throws(() => checkMinimumBoundary(changed, boundary));
  }
});

test("PPP statutory edition reconciliation retains raw bytes and correct cutoff", () => {
  const a = read("evidence/material-closure-2025/usc-2023-15-636.source.txt");
  const b = read("evidence/material-closure-2025/usc-2024-15-636.source.txt");
  assert.match(a, /currentthrough:20240103/);
  assert.match(b, /currentthrough:20250106/);
  const fragment = (text) => {
    const start = text.indexOf('<p class="statutory-body-1em">(36)');
    const end = text.indexOf('<p class="statutory-body-1em">(37)');
    assert.ok(start >= 0 && end > start);
    return text.slice(start, end);
  };
  assert.equal(fragment(a), fragment(b));
  assert.equal(Buffer.byteLength(fragment(b)), 47441);
  assert.equal(
    createHash("sha256").update(fragment(b)).digest("hex"),
    "198cc3d8c1e0122ec1348b44ab28331a17f895d041a2820f07355187e6e2e03e",
  );
  assert.match(
    fragment(b),
    /means a loan made under this paragraph during the covered period/,
  );
  assert.match(fragment(b), /ending on June 30, 2021/);
});

test("incorporated identity and reporting evidence is captured, bounded and linked", () => {
  const evidence = (id) => allEvidence.find((x) => x.source_id === id);
  const bank = evidence("USC-2024-12-1813");
  assert.match(read(bank.local_path), /any bank or savings association/);
  const creditUnion = evidence("USC-2024-12-1752");
  assert.match(
    read(creditUnion.local_path),
    /Text contains those laws in effect on January 6, 2025/,
  );
  assert.match(
    read(creditUnion.local_path),
    /cooperative association organized/,
  );
  const regK = evidence("US-INCORPORATED-211.2");
  assert.equal(regK.point_in_time_date, "2025-01-01");
  assert.match(
    read(regK.local_path),
    /Has the power to accept demand deposits/,
  );
  assert.match(
    read(evidence("GOVINFO-2025-211.2").local_path),
    /<DATE>2025-01-01<\/DATE>/,
  );
  for (const id of [
    "FFIEC-GLOSSARY-2024-06",
    "FFIEC-RC-2024-03",
    "FFIEC-RCD-2020-09",
    "FFIEC-2024-12-UPDATES",
  ]) {
    const item = evidence(id);
    assert.equal(
      readFileSync(resolve(root, item.local_path)).subarray(0, 5).toString(),
      "%PDF-",
    );
    assert.ok(item.source_locator.length > 0);
    assert.equal(item.executable, false);
  }
  const review = read("MATERIAL_SOURCE_CLOSURE.md");
  for (const warning of [
    "Zero allowance is not inferred",
    "UNKNOWN_NOT_OPEN_ENDED",
    "REQUIRED_BUT_UNRESOLVED (0)",
    "No production code changed",
    "SPRINT 02 REMAINS INACTIVE",
  ])
    assert.ok(review.includes(warning));
});
