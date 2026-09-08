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
  for (const record of [manifest, golden, activation])
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
    .filter((x) => /\.(xml|json|txt)$/.test(x));
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
