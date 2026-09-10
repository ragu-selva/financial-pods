"""U.S. provider's pinned evidence adapter. Loading is outside the calculation core."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from hashlib import sha256
from pathlib import Path
from typing import cast

from ..fixtures import load_case_fixture
from ..primitives import Currency
from .contracts import (
    FactProvenance,
    Immutable,
    RegulatoryContext,
    RegulatoryFact,
    RegulatoryFactSnapshot,
    RequestMetadata,
    RuleReference,
    RulesetIdentity,
    SourceCitation,
    money,
)
from .errors import ErrorCode, fail
from .serialization import array, decimal_text, object_value, parse_json, string

US_VERSION = "US_FRB_PART217_STANDARDIZED@2025-01-01.internal-v1"
US_FAMILY = "US_FRB_PART217_STANDARDIZED"
US_DATE = date(2025, 1, 1)
APPROVED = "APPROVED_FOR_INTERNAL_PROTOTYPE"
MANIFEST_HASH = "1a693c8acaee30642e7ff9ed02914296568d3f44fbe8884f96d224e4eddfa5ed"
BASELINE_HASH = "acae53f92c283487d9d7bbd2692d6e25900cc0d63ebb1cfe9a0e2666f92862f2"
GOLDEN_HASH = "59e87b7748d4b506adb513d7c657b0e3d4e23d7581428b91810b19e96692e29e"
APPROVAL_HASH = "58c65c7bc05f75db2ab167ab950aa104f57930fe7884b8838c240f559998f838"
CATALOG_ID = "us-frb-internal-v1:activation-pr-4:a89eeb6"
RULE_IDS = ("US-SCOPE", "US-CLASS", "US-MEASURE", "US-CORP-RW", "US-RWA", "US-TEACHING")


def authored_hash(raw: bytes) -> str:
    # Authored JSON permits checkout CRLF; raw source captures are NEVER normalized.
    return sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


@dataclass(frozen=True, slots=True, kw_only=True)
class SourceBlob(Immutable):
    source_id: str
    content: bytes


@dataclass(frozen=True, slots=True, kw_only=True)
class USSourcePackage(Immutable):
    manifest: bytes
    baseline: bytes
    golden: bytes
    approval: bytes
    captures: tuple[SourceBlob, ...]

    def validate(self) -> None:
        manifest, approval = parse_json(self.manifest), parse_json(self.approval)
        if (
            manifest.get("approval_status") != APPROVED
            or approval.get("review_decision") != APPROVED
        ):
            fail(ErrorCode.RULESET_NOT_APPROVED, "manifest", "Human approval is required")
        if approval.get("responsibilities_accepted") is not True:
            fail(
                ErrorCode.RULESET_NOT_APPROVED, "approval", "Reviewer did not accept responsibility"
            )
        for value in array(manifest.get("approved_rules"), "approved_rules"):
            rule = object_value(value, "rule")
            if rule.get("legal_status") != "CURRENT":
                fail(
                    ErrorCode.RULESET_STATUS_NOT_EXECUTABLE,
                    "rule",
                    "Only the approved current-as-of rule may execute",
                )
            if (
                rule.get("review_status") != APPROVED
                or rule.get("approved_for_execution_evidence") is not True
            ):
                fail(
                    ErrorCode.RULESET_NOT_APPROVED,
                    "rule",
                    "Rule is not approved execution evidence",
                )
            if rule.get("approved_as_of_dates") != ["2025-01-01"]:
                fail(ErrorCode.RULESET_NOT_EFFECTIVE, "rule", "Wrong approved date")
            for value_ref in array(rule.get("source_refs"), "source_refs"):
                if object_value(value_ref, "source_ref").get("source_id") == "R-1888-PROPOSAL":
                    fail(
                        ErrorCode.RULESET_STATUS_NOT_EXECUTABLE,
                        "source_ref",
                        "R-1888 is never executable",
                    )
        for name, raw, expected in (
            ("manifest", self.manifest, MANIFEST_HASH),
            ("baseline", self.baseline, BASELINE_HASH),
            ("golden", self.golden, GOLDEN_HASH),
            ("approval", self.approval, APPROVAL_HASH),
        ):
            if authored_hash(raw) != expected:
                fail(
                    ErrorCode.SOURCE_HASH_MISMATCH,
                    name,
                    "Content differs from approved immutable version",
                )
        baseline = parse_json(self.baseline)
        records = [
            object_value(item, "source")
            for group in ("sources", "supporting_evidence", "proposal_evidence")
            for item in array(baseline[group], group)
        ]
        blobs = {item.source_id: item.content for item in self.captures}
        if len(blobs) != len(self.captures) or set(blobs) != {
            item["source_id"] for item in records
        }:
            fail(
                ErrorCode.SOURCE_EVIDENCE_INCOMPLETE,
                "captures",
                "Missing, duplicate or extra source evidence",
            )
        for item in records:
            source_id = string(item["source_id"], "source_id")
            raw = blobs[source_id]
            if len(raw) != item["byte_length"] or sha256(raw).hexdigest() != item["content_sha256"]:
                fail(
                    ErrorCode.SOURCE_HASH_MISMATCH,
                    source_id,
                    "Raw source bytes do not match approved evidence",
                )

    @property
    def identity(self) -> RulesetIdentity:
        return RulesetIdentity(
            jurisdiction="US",
            regulator="FRB",
            regime="STANDARDIZED",
            ruleset_id=US_FAMILY,
            ruleset_version=US_VERSION,
            approved_as_of=US_DATE,
            manifest_hash=MANIFEST_HASH,
            catalog_snapshot_id=CATALOG_ID,
            legal_status="CURRENT",
            approved=True,
        )

    def rule(self, rule_id: str) -> RuleReference:
        manifest, baseline = parse_json(self.manifest), parse_json(self.baseline)
        rules = [object_value(item, "rule") for item in array(manifest["approved_rules"], "rules")]
        match = next((item for item in rules if item["rule_id"] == rule_id), None)
        if match is None:
            fail(ErrorCode.SOURCE_EVIDENCE_INCOMPLETE, rule_id, "Rule not in approved package")
        records = {
            string(item["source_id"], "source_id"): item
            for group in ("sources", "supporting_evidence")
            for raw in array(baseline[group], group)
            for item in (object_value(raw, "source"),)
        }
        relevant = [match]
        dependencies = [
            object_value(item, "dependency")
            for item in array(manifest["approved_required_dependencies"], "dependencies")
        ]
        relevant.extend(
            item
            for item in dependencies
            if item["dependency_id"] in array(match["dependency_ids"], "dependency_ids")
        )
        citations: dict[str, SourceCitation] = {}
        locators: list[str] = []
        for scope in relevant:
            locators.extend(
                string(item, "locator") for item in array(scope["locators"], "locators")
            )
            for raw_ref in array(scope["source_refs"], "source_refs"):
                source = records[string(object_value(raw_ref, "ref")["source_id"], "source_id")]
                source_id = string(source["source_id"], "source_id")
                locator = source.get("source_locator", source.get("source_version_metadata", {}))
                # Retain recorded metadata, including uncertain dates, without inventing dates.
                citations[source_id] = SourceCitation(
                    source_id=source_id,
                    authority=string(source["authority"], "authority")
                    if "authority" in source
                    else None,
                    canonical_source=string(
                        source.get("canonical_source", source["retrieval_url"]), "canonical_source"
                    ),
                    locator=locator
                    if isinstance(locator, str)
                    else json.dumps(locator, sort_keys=True),
                    content_sha256=string(source["content_sha256"], "content_sha256"),
                    retrieval_date=string(source["retrieval_date"], "retrieval_date"),
                    version_evidence=json.dumps(
                        {
                            key: source[key]
                            for key in (
                                "source_version_metadata",
                                "publication_date",
                                "point_in_time_date",
                                "source_locator",
                                "federal_register_references_as_printed",
                            )
                            if key in source
                        },
                        sort_keys=True,
                    ),
                )
        return RuleReference(
            rule_id=rule_id,
            rule_version=string(match["rule_version"], "rule_version"),
            authority=string(
                records[
                    string(
                        object_value(array(match["source_refs"], "refs")[0], "ref")["source_id"],
                        "source_id",
                    )
                ]["authority"],
                "authority",
            ),
            locators=tuple(dict.fromkeys(locators)),
            citations=tuple(citations[key] for key in sorted(citations)),
            effective_from=date.fromisoformat(string(match["effective_from"], "effective_from")),
            approved_as_of=US_DATE,
            reviewer_name=string(match["reviewer_name"], "reviewer_name"),
            review_date=date.fromisoformat(string(match["review_date"], "review_date")),
            review_status="APPROVED_FOR_INTERNAL_PROTOTYPE",
        )

    def fact_specification(self) -> tuple[RegulatoryFact, ...]:
        golden = parse_json(self.golden)
        groups = object_value(golden["fact_groups"], "fact_groups")
        values: dict[str, object] = {}
        for name, value in groups.items():
            group = object_value(value, name)
            for key, item in object_value(group["facts"], name + ".facts").items():
                values[f"{name}.{key}"] = item
        for name, value in object_value(golden["exposure_facts"], "exposure_facts").items():
            if not name.endswith("_review"):
                values["exposure." + name] = value
        for raw in array(golden["definition_screen"], "definition_screen"):
            screen = object_value(raw, "screen")
            for value in array(screen["alternative_assessments"], "alternatives"):
                item = object_value(value, "assessment")
                values["definition." + string(item["concept"], "concept")] = item["outcome"] != "NO"
        result: list[RegulatoryFact] = []
        for path, raw in sorted(values.items()):
            if isinstance(raw, str) and re.fullmatch(r"-?\d+\.\d+", raw):
                value = money(decimal_text(raw, path), Currency("USD"))
            elif type(raw) in (bool, int, str):
                value = cast(str | bool | int, raw)
            else:
                fail(ErrorCode.INVALID_SCHEMA, path, "Unsupported approved fact type")
            result.append(
                RegulatoryFact(
                    path=path,
                    value=value,
                    provenance=FactProvenance(
                        source_ref="GOLDEN_CASE_APPROVED.json#" + path,
                        source_version=GOLDEN_HASH,
                        assumption_id="INTERNAL-PROTOTYPE:" + path,
                        review_status="APPROVED_FOR_INTERNAL_PROTOTYPE",
                    ),
                )
            )
        return tuple(result)


def _read(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        fail(ErrorCode.SOURCE_EVIDENCE_INCOMPLETE, str(path), str(exc))


def load_us_source_package(directory: Path) -> USSourcePackage:
    directory = directory.resolve()
    baseline_raw = _read(directory / "SOURCE_MANIFEST.reviewed-v0.4.json")
    if authored_hash(baseline_raw) != BASELINE_HASH:
        fail(ErrorCode.SOURCE_HASH_MISMATCH, "baseline", "Unapproved evidence index")
    baseline = parse_json(baseline_raw)
    captures: list[SourceBlob] = []
    evidence_root = (directory / "evidence").resolve()
    for group in ("sources", "supporting_evidence", "proposal_evidence"):
        for raw in array(baseline[group], group):
            item = object_value(raw, "source")
            path = (directory / string(item["local_path"], "path")).resolve()
            if not path.is_relative_to(evidence_root):
                fail(
                    ErrorCode.SOURCE_EVIDENCE_INCOMPLETE,
                    "path",
                    "Evidence escapes capture directory",
                )
            captures.append(
                SourceBlob(source_id=string(item["source_id"], "source_id"), content=_read(path))
            )
    package = USSourcePackage(
        manifest=_read(directory / "SOURCE_MANIFEST.json"),
        baseline=baseline_raw,
        golden=_read(directory / "GOLDEN_CASE_APPROVED.json"),
        approval=_read(directory / "ACTIVATION_RECORD.json"),
        captures=tuple(captures),
    )
    package.validate()
    return package


def load_golden_snapshot(repository: Path, package: USSourcePackage) -> RegulatoryFactSnapshot:
    package.validate()
    golden = parse_json(package.golden)
    fixture = object_value(golden["accepted_fixture"], "accepted_fixture")
    # File path belongs to the fixture adapter, never to classifier predicates.
    path = repository / "data" / "finbank" / "alpha_manufacturing_v1.json"
    if authored_hash(_read(path)) != fixture["sha256"]:
        fail(ErrorCode.SOURCE_HASH_MISMATCH, "fixture", "Accepted Sprint 01 fixture changed")
    case = load_case_fixture(path)
    facts = package.fact_specification()
    values = {item.path: item.value for item in facts}
    if (
        values["exposure.original_principal"] != case.facility.original_principal
        or values["exposure.outstanding_balance"] != case.exposure.outstanding_principal
        or case.exposure.as_of_date != US_DATE
    ):
        fail(ErrorCode.CONFLICTING_FACTS, "fixture", "Accepted fixture and enrichment disagree")
    return RegulatoryFactSnapshot(
        context=RegulatoryContext(
            jurisdiction="US",
            regulator="FRB",
            regime="STANDARDIZED",
            as_of_date=case.exposure.as_of_date,
            ruleset_version=US_VERSION,
        ),
        facts=facts,
        fixture_version=case.fixture_version,
        metadata=RequestMetadata(
            case_id=str(case.exposure.id),
            counterparty_id=str(case.counterparty.id),
            institution_id=str(case.institution.id),
            borrower_name=case.counterparty.legal_name,
        ),
    )
