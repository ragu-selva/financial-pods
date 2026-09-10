// Offline approval-artifact checks only. No regulatory engine is imported or implemented.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const root = dirname(fileURLToPath(import.meta.url));
const read = (path) => readFileSync(resolve(root, path), "utf8");
const json = (path) => JSON.parse(read(path));
const hash = (path) =>
  createHash("sha256")
    .update(read(path).replaceAll("\r\n", "\n"))
    .digest("hex");
const pack = json("SOURCE_MANIFEST.json");
const baseline = json("SOURCE_MANIFEST.reviewed-v0.4.json");
const activation = json("ACTIVATION_RECORD.json");
const golden = json("GOLDEN_CASE_APPROVED.json");
const candidate = json("GOLDEN_CASE_CANDIDATE.json");
const boundary = json("GOLDEN_CASE_SOURCE_BOUNDARY.json");
const approved = "APPROVED_FOR_INTERNAL_PROTOTYPE";
const version = "US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1";
const reviewer = "Ragunath Selvaraj";
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
const pins = {
  "SOURCE_MANIFEST.reviewed-v0.4.json":
    "acae53f92c283487d9d7bbd2692d6e25900cc0d63ebb1cfe9a0e2666f92862f2",
  "GOLDEN_CASE_CANDIDATE.json":
    "0eae615fc75c0f4a3ac4e578d8f83d6c5ea38e2570c1526bf9bdf702c8581617",
  "GOLDEN_CASE_SOURCE_BOUNDARY.json":
    "913e8d5ef75deb1e631856513a826aa170a5609e2293ec98e3f7793d54bd2e46",
  "ACTIVATION_RECORD.reviewed-v0.4.json":
    "4af225c03848aa361fcd0efae64c61e565c9e21497eb224b3d2b5fc135fc014c",
};
const evidence = [...baseline.sources, ...baseline.supporting_evidence];
const refs = (ids) =>
  ids.map((id) => {
    const source = evidence.find((x) => x.source_id === id);
    assert.ok(source, id);
    return { source_id: id, content_sha256: source.content_sha256 };
  });

function checkHuman(a) {
  assert.equal(
    a.review_evidence.approved_manifest_sha256,
    hash("SOURCE_MANIFEST.json"),
  );
  assert.equal(
    a.review_evidence.approved_golden_case_sha256,
    hash("GOLDEN_CASE_APPROVED.json"),
  );
  assert.equal(a.status, "ACTIVE");
  assert.equal(a.activation_status, "HUMAN_APPROVED_PENDING_PR_MERGE");
  assert.equal(a.reviewer_name, reviewer);
  assert.equal(a.reviewer_role, "Project Owner / Internal Regulatory Reviewer");
  assert.equal(
    a.reviewer_qualification_or_authority,
    "Project owner accountable for regulatory interpretation and Golden Case approval for the internal Financial Pods V1 prototype. This is not independent legal counsel, regulatory certification, or production-bank sign-off.",
  );
  assert.equal(a.responsibilities_accepted, true);
  assert.equal(a.review_date, "2026-09-10");
  assert.equal(a.review_decision, approved);
  assert.equal(a.regulatory_as_of, "2025-01-01");
  assert.equal(a.source_approval_complete, true);
  assert.equal(a.golden_case_approval_complete, true);
  assert.deepEqual(
    a.review_evidence.reviewed_subjects,
    a.required_review_subjects,
  );
  assert.equal(
    a.review_evidence.planning_commit,
    "79b33dbb1f069a89fc6d87336a23268adea08589",
  );
  assert.equal(
    a.review_evidence.reviewed_manifest_sha256,
    pins["SOURCE_MANIFEST.reviewed-v0.4.json"],
  );
  assert.equal(a.review_evidence.source_manifest, "SOURCE_MANIFEST.json");
  assert.equal(a.review_evidence.golden_case, "GOLDEN_CASE_APPROVED.json");
  assert.deepEqual(a.review_evidence.source_closure, [
    "SOURCE_REVIEW.md",
    "MATERIAL_SOURCE_CLOSURE.md",
  ]);
  assert.ok(
    a.review_evidence.approval_basis.includes("Explicit project-owner"),
  );
  assert.equal(a.adr_status, "ACCEPTED");
  assert.equal(a.source_resolver_skill.approved, true);
  assert.equal(a.activation_pr.branch, "codex/sprint-02-activation");
  assert.equal(a.activation_pr.base, "main");
  assert.equal(a.activation_pr.merged, false);
  if (a.activation_pr.created)
    assert.match(
      a.activation_pr.url,
      /^https:\/\/github\.com\/ragu-selva\/financial-pods\/pull\/\d+$/,
    );
  else assert.equal(a.activation_pr.url, null);
  assert.equal(a.implementation.authorized, false);
  assert.equal(a.implementation.status, "NOT YET STARTED");
  assert.match(a.implementation.prerequisite, /reviewed and merged/);
}

function checkScopedApproval(x) {
  assert.equal(x.review_status, approved);
  assert.equal(x.reviewer_name, reviewer);
  assert.equal(x.review_date, "2026-09-10");
  assert.equal(x.review_evidence, "ACTIVATION_RECORD.json");
  assert.equal(x.approved_for_execution_evidence, true);
  assert.deepEqual(x.approved_as_of_dates, ["2025-01-01"]);
}

function checkPackage(p) {
  assert.equal(p.schema_version, "source-approval-package.v1");
  assert.equal(p.status, "ACTIVE");
  assert.equal(p.approval_status, approved);
  assert.equal(p.source_readiness, approved);
  assert.equal(
    p.executable,
    false,
    "Documentary approval is not executable software",
  );
  assert.equal(p.ruleset_family, "US_FRB_PART217_STANDARDIZED");
  assert.equal(p.ruleset_version, version);
  assert.equal(p.regulatory_as_of, "2025-01-01");
  assert.equal(p.jurisdiction, "US");
  assert.equal(p.regulator, "FRB");
  assert.equal(p.regulatory_regime, "STANDARDIZED");
  assert.equal(p.reviewed_manifest.path, "SOURCE_MANIFEST.reviewed-v0.4.json");
  assert.equal(p.reviewed_manifest.sha256, pins[p.reviewed_manifest.path]);
  assert.equal(p.approval_record, "ACTIVATION_RECORD.json");
  assert.equal(p.approved_golden_case, "GOLDEN_CASE_APPROVED.json");
  assert.deepEqual(p.selection_policy.approved_as_of_dates, ["2025-01-01"]);
  assert.equal(p.selection_policy.legal_status_as_of, "CURRENT");
  assert.equal(p.selection_policy.effective_to, null);
  assert.equal(
    p.selection_policy.effective_to_status,
    "UNKNOWN_NOT_OPEN_ENDED",
  );
  assert.equal(p.selection_policy.unknown_endpoint_is_open_ended, false);
  assert.equal(p.selection_policy.other_dates, "REQUIRE_NEW_REVIEW");
  assert.equal(p.selection_policy.ambiguous_or_missing_evidence, "FAIL_CLOSED");
  assert.deepEqual(p.required_but_unresolved_ids, []);
  assert.deepEqual(
    p.approved_rules.map((x) => x.rule_id),
    [
      "US-SCOPE",
      "US-CLASS",
      "US-MEASURE",
      "US-CORP-RW",
      "US-RWA",
      "US-TEACHING",
    ],
  );
  for (const x of p.approved_rules) {
    checkScopedApproval(x);
    const original = baseline.rule_bindings.find(
      (y) => y.rule_id === x.rule_id,
    );
    assert.equal(x.rule_version, x.rule_id + "@2025-01-01.internal-v1");
    assert.equal(x.legal_status, "CURRENT");
    assert.equal(x.legal_status_as_of, "2025-01-01");
    assert.equal(x.effective_from, original.effective_from);
    assert.equal(x.effective_to, null);
    assert.equal(x.effective_to_status, "UNKNOWN_NOT_OPEN_ENDED");
    assert.deepEqual(x.paragraph_lineage_ids, original.paragraph_lineage_ids);
    assert.deepEqual(
      x.locators,
      original.paragraph_lineage_ids.map(
        (id) =>
          baseline.paragraph_lineage.find((y) => y.lineage_id === id)
            .paragraph_locator,
      ),
    );
    assert.deepEqual(x.source_refs, refs(original.source_ids));
    assert.deepEqual(x.dependency_ids, original.dependency_ids);
    assert.equal(
      x.interpretation,
      original.interpretation.replace(/^Candidate /, ""),
    );
    assert.match(x.scope, /not positive excluded treatments/);
  }
  assert.deepEqual(
    p.approved_required_dependencies.map((x) => x.dependency_id),
    required,
  );
  for (const x of p.approved_required_dependencies) {
    checkScopedApproval(x);
    const original = baseline.dependency_inventory.find(
      (y) => y.dependency_id === x.dependency_id,
    );
    assert.equal(x.classification, "REQUIRED_AND_RESOLVED");
    assert.deepEqual(x.locators, original.locators);
    assert.deepEqual(x.source_refs, refs(original.source_ids));
    assert.deepEqual(x.fact_group_refs, original.fact_group_refs);
    assert.equal(x.scope, original.scope);
    assert.equal(x.closure_evidence, "MATERIAL_SOURCE_CLOSURE.md");
  }
  assert.deepEqual(
    p.dependency_boundary,
    baseline.dependency_inventory.map((x) => ({
      dependency_id: x.dependency_id,
      classification: x.classification,
      approved_for_execution_evidence:
        x.classification === "REQUIRED_AND_RESOLVED",
    })),
  );
  assert.deepEqual(
    p.proposal_evidence,
    baseline.proposal_evidence.map((x) => ({
      source_id: x.source_id,
      legal_status: "PROPOSED",
      executable: false,
      content_sha256: x.content_sha256,
      approved_for_execution_evidence: false,
    })),
  );
}

function checkGolden(g) {
  assert.equal(g.status, "ACTIVE");
  assert.equal(g.review_status, approved);
  assert.equal(g.reviewer_name, reviewer);
  assert.equal(g.review_date, "2026-09-10");
  assert.equal(g.review_evidence, "ACTIVATION_RECORD.json");
  assert.equal(g.executable, false);
  assert.equal(g.specimen_kind, "APPROVED_EXPECTATIONS_NOT_EXECUTED_RESULT");
  assert.deepEqual(g.accepted_fixture, candidate.accepted_fixture);
  assert.deepEqual(g.context, {
    ...boundary.context,
    regulatory_regime: "STANDARDIZED",
    ruleset_version: version,
  });
  assert.deepEqual(g.reviewed_candidates, [
    {
      path: "GOLDEN_CASE_CANDIDATE.json",
      sha256: pins["GOLDEN_CASE_CANDIDATE.json"],
    },
    {
      path: "GOLDEN_CASE_SOURCE_BOUNDARY.json",
      sha256: pins["GOLDEN_CASE_SOURCE_BOUNDARY.json"],
    },
  ]);
  assert.deepEqual(
    Object.keys(g.fact_groups),
    Object.keys(boundary.fact_groups),
  );
  for (const [name, x] of Object.entries(g.fact_groups)) {
    assert.deepEqual(x.facts, boundary.fact_groups[name].facts);
    assert.deepEqual(
      x.dependency_ids,
      boundary.fact_groups[name].dependency_ids,
    );
    assert.equal(x.review_status, approved);
  }
  assert.deepEqual(g.exposure_facts, {
    ...candidate.candidate_facts.exposure,
    carrying_value_reconciliation_review: approved,
  });
  assert.equal(g.definition_screen.length, 14);
  g.definition_screen.forEach((x, i) => {
    const old = candidate.candidate_facts.definition_screen[i];
    assert.equal(x.assessment_id, old.assessment_id);
    assert.equal(x.rule_ref, old.rule_ref);
    assert.equal(x.locator, old.locator);
    assert.equal(x.reviewer_evidence, "ACTIVATION_RECORD.json");
    assert.deepEqual(
      x.alternative_assessments.map((y) => y.concept),
      old.alternative_assessments.map((y) => y.concept),
    );
    for (const alternative of x.alternative_assessments) {
      assert.equal(alternative.outcome, "NO");
      assert.equal(alternative.review_status, approved);
      assert.ok(alternative.provenance.includes("Owner approval"));
    }
  });
  assert.deepEqual(
    g.treatment_scope_assessments.map((x) => x.concept),
    candidate.candidate_facts.treatment_scope_assessments.map((x) => x.concept),
  );
  for (const x of g.treatment_scope_assessments) {
    assert.equal(x.outcome, "NO");
    assert.equal(x.review_status, approved);
    assert.match(x.review_evidence, /outer negative screen only/);
  }
  const expected = structuredClone(candidate.candidate_result);
  expected.regulatory_treatment = "ORDINARY_US_STANDARDIZED_CORPORATE";
  expected.warnings = [
    "INTERNAL_PROTOTYPE_ONLY",
    "EDUCATIONAL_ONLY",
    "NOT_ECONOMIC_CAPITAL",
    "NOT_COMPLETE_REQUIRED_REGULATORY_CAPITAL",
  ];
  expected.capital_teaching_outputs[0].warnings.push(
    "NOT_ECONOMIC_CAPITAL",
    "NOT_COMPLETE_REQUIRED_REGULATORY_CAPITAL",
  );
  expected.ruleset_version = version;
  expected.rule_versions = Object.fromEntries(
    pack.approved_rules.map((x) => [x.rule_id, x.rule_version]),
  );
  assert.deepEqual(
    g.expected_result,
    expected,
    "Only approval metadata/warnings change; numeric expectations stay fixed; runtime evidence stays null",
  );
  assert.deepEqual(g.accepted_simplifications, {
    gaap_carrying_value: "10000000.00",
    currency: "USD",
    credit_loss_allowance: "0.00",
    write_offs: "0.00",
    premium_discount: "0.00",
    accrued_interest_fee_adjustment: "0.00",
    pcd: false,
    crm: "NONE",
    past_due: false,
    nonaccrual: false,
  });
  assert.deepEqual(
    g.accepted_simplifications,
    activation.review_evidence.accepted_simplifications,
  );
  for (const warning of [
    "NOT a CECL estimate",
    "arbitrary real-bank",
    "economic capital",
    "complete required regulatory capital",
    "capital adequacy conclusion",
    "NOT EXECUTED",
  ])
    assert.ok(g.limitations.join(" ").includes(warning), warning);
}

test("all reviewed snapshots retain exact pinned content", () => {
  for (const [path, expected] of Object.entries(pins))
    assert.equal(hash(path), expected, path);
});
test("explicit confirmed human approval is internal-only and does not permit implementation before merge", () =>
  checkHuman(activation));
test("source approval is paragraph/dependency scoped, effective for one date only", () =>
  checkPackage(pack));
test("approved Golden values and every material fact retain their reviewed boundary", () =>
  checkGolden(golden));
test("approval record cannot omit responsibility, change identity, expand authority or claim implementation", () => {
  for (const mutate of [
    (x) => {
      x.reviewer_name = "AI reviewer";
    },
    (x) => {
      x.responsibilities_accepted = false;
    },
    (x) => {
      x.review_decision = "APPROVED";
    },
    (x) => {
      x.reviewer_qualification_or_authority = "Independent legal certification";
    },
    (x) => {
      x.implementation.authorized = true;
    },
    (x) => {
      x.activation_pr.merged = true;
    },
    (x) => {
      x.review_evidence.source_closure = [];
    },
  ]) {
    const changed = structuredClone(activation);
    mutate(changed);
    assert.throws(() => checkHuman(changed));
  }
});
test("approval cannot widen dates, invent legal endpoints, substitute proposal or approve all sources", () => {
  for (const mutate of [
    (x) => {
      x.selection_policy.approved_as_of_dates.push("2025-01-02");
    },
    (x) => {
      x.selection_policy.unknown_endpoint_is_open_ended = true;
    },
    (x) => {
      x.approved_rules[0].effective_to = "2099-01-01";
    },
    (x) => {
      x.approved_rules[0].source_refs[0].source_id = "R-1888-PROPOSAL";
    },
    (x) => {
      x.approved_rules[0].source_refs[0].content_sha256 = "0".repeat(64);
    },
    (x) => {
      x.approved_rules[0].locators = ["All Part 217"];
    },
    (x) => {
      x.approved_required_dependencies.push(
        structuredClone(x.approved_required_dependencies[0]),
      );
    },
    (x) => {
      x.dependency_boundary.find(
        (y) => y.dependency_id === "DEP-AOCI",
      ).approved_for_execution_evidence = true;
    },
    (x) => {
      x.proposal_evidence[0].legal_status = "CURRENT";
      x.proposal_evidence[0].executable = true;
    },
    (x) => {
      x.required_but_unresolved_ids.push("DEP-PPP");
    },
    (x) => {
      x.approved_rules[0].reviewer_name = null;
    },
  ]) {
    const changed = structuredClone(pack);
    mutate(changed);
    assert.throws(() => checkPackage(changed));
  }
});
test("approval cannot drop a material source, dependency or definition alternative", () => {
  for (const mutate of [
    (x) => {
      x.approved_required_dependencies.pop();
    },
    (x) => {
      x.approved_required_dependencies
        .find((y) => y.dependency_id === "DEP-PPP")
        .source_refs.pop();
    },
    (x) => {
      x.approved_rules.pop();
    },
  ]) {
    const changed = structuredClone(pack);
    mutate(changed);
    assert.throws(() => checkPackage(changed));
  }
  const changed = structuredClone(golden);
  changed.definition_screen[0].alternative_assessments.pop();
  assert.throws(() => checkGolden(changed));
});
test("changed facts, values, EAD aliases, missing warnings and fabricated traces fail closed", () => {
  for (const mutate of [
    (x) => {
      x.fact_groups.ppp.facts.ppp_loan = true;
    },
    (x) => {
      delete x.fact_groups.accounting.facts.credit_loss_allowance;
    },
    (x) => {
      x.fact_groups.accounting.facts.pcd = true;
    },
    (x) => {
      x.fact_groups.market_risk.facts.foreign_exchange_position = true;
    },
    (x) => {
      x.expected_result.risk_weight.value = "0.75";
    },
    (x) => {
      x.expected_result.rwa.amount = "7500000.00";
    },
    (x) => {
      x.expected_result.ead = "10000000.00";
    },
    (x) => {
      x.expected_result.capital_teaching_outputs[0].warnings = [];
    },
    (x) => {
      x.expected_result.calculation_trace = [];
    },
    (x) => {
      x.accepted_simplifications.nonaccrual = true;
    },
    (x) => {
      x.context.as_of_date = "2026-09-10";
    },
  ]) {
    const changed = structuredClone(golden);
    mutate(changed);
    assert.throws(() => checkGolden(changed));
  }
});
test("current controls record merged activation before implementation and retain historical review", () => {
  for (const path of [
    "SPRINT.md",
    "FRAMEWORK_SCOPE.md",
    "ACCEPTANCE_CRITERIA.md",
    "REVIEW.md",
    "SOURCE_REVIEW.md",
    "MATERIAL_SOURCE_CLOSURE.md",
    "PLANNED_TESTS.md",
  ]) {
    assert.ok(
      read(path).split("\n").slice(0, 5).join("\n").includes("Status: ACTIVE"),
      path,
    );
  }
  assert.match(read("REVIEW.md"), /Historical planning review/);
  assert.match(read("SOURCE_REVIEW.md"), /Historical documentary assessment/);
  assert.match(
    read("../../docs/adr/0004-generalized-regulatory-engine.md"),
    /Status: ACCEPTED/,
  );
  assert.match(
    read("SPRINT.md"),
    /Only after review and merge may implementation start/,
  );
  const implementation = json("IMPLEMENTATION_RECORD.json");
  assert.equal(implementation.activation_pr, 4);
  assert.equal(implementation.activation_merged, true);
  assert.equal(
    implementation.activation_merge_commit,
    "a89eeb60727c5f615514f75ecc27f57f19ec23cf",
  );
  assert.equal(implementation.branch, "codex/sprint-02-us-corporate-engine");
  assert.equal(implementation.status, "IMPLEMENTED_PENDING_REVIEW");
  assert.equal(implementation.implementation_accepted, false);
  assert.equal(implementation.ruleset_version, version);
  // The signed activation-time record is historical, never rewritten as software acceptance.
  assert.match(read("SPRINT.md"), /Current implementation stop condition/);
});
