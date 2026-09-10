"""Generic provider orchestration and trace assembly. No U.S. formulas or names."""

from dataclasses import dataclass
from typing import Protocol

from .contracts import (
    CalculationTrace,
    ClassificationResult,
    FailureDetail,
    RegulatoryCalculationResult,
    RegulatoryContext,
    RegulatoryExposureMeasure,
    RegulatoryFactSnapshot,
    RegulatoryTreatment,
    RiskWeight,
    RuleReference,
    RulesetIdentity,
    RwaResult,
    TeachingOutput,
    TraceCompletion,
    TraceStep,
    ValidationEvidence,
)
from .errors import ErrorCode, RegulatoryError, fail
from .serialization import snapshot_hash


class RegulatoryRuleset(Protocol):
    @property
    def identity(self) -> RulesetIdentity: ...
    def validate_evidence(self) -> None: ...
    def rule(self, rule_id: str) -> RuleReference: ...
    def validate_institution(self, facts: RegulatoryFactSnapshot) -> tuple[str, ...]: ...
    def validate_exposure(self, facts: RegulatoryFactSnapshot) -> tuple[str, ...]: ...
    def classification_scope_refs(self) -> tuple[RuleReference, ...]: ...
    def institution_scope_refs(self) -> tuple[RuleReference, ...]: ...
    def classify_exposure(self, facts: RegulatoryFactSnapshot) -> ClassificationResult: ...
    def resolve_treatment(self, classification: ClassificationResult) -> RegulatoryTreatment: ...
    def determine_regulatory_exposure_measure(
        self, facts: RegulatoryFactSnapshot
    ) -> RegulatoryExposureMeasure: ...
    def determine_risk_weight(self, facts: RegulatoryFactSnapshot) -> RiskWeight: ...
    def calculate_rwa(
        self, measure: RegulatoryExposureMeasure, weight: RiskWeight
    ) -> RwaResult: ...
    def calculate_capital_teaching_outputs(self, rwa: RwaResult) -> tuple[TeachingOutput, ...]: ...


@dataclass(frozen=True, slots=True)
class RulesetRegistry:
    providers: tuple[RegulatoryRuleset, ...]
    revoked_versions: tuple[str, ...] = ()
    prohibited_versions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for value in (self.providers, self.revoked_versions, self.prohibited_versions):
            if type(value) is not tuple:
                fail(
                    ErrorCode.INVALID_TYPE,
                    "registry",
                    "Registry collections must be immutable tuples",
                )

    def resolve(self, context: RegulatoryContext) -> RegulatoryRuleset:
        if context.ruleset_version in self.prohibited_versions:
            fail(
                ErrorCode.RULESET_STATUS_NOT_EXECUTABLE,
                "ruleset_version",
                "Proposed or prohibited version cannot execute",
            )
        if context.ruleset_version in self.revoked_versions:
            fail(ErrorCode.RULESET_NOT_APPROVED, "ruleset_version", "Approval has been revoked")
        perimeter = [
            p
            for p in self.providers
            if (p.identity.jurisdiction, p.identity.regulator, p.identity.regime)
            == (context.jurisdiction, context.regulator, context.regime)
        ]
        if not perimeter:
            fail(
                ErrorCode.UNSUPPORTED_JURISDICTION,
                "context",
                "No provider for jurisdiction/regulator/regime",
            )
        matches = [p for p in perimeter if p.identity.ruleset_version == context.ruleset_version]
        if not matches:
            fail(
                ErrorCode.UNKNOWN_RULESET,
                "ruleset_version",
                "Exact registered version required; no alias fallback",
            )
        if len(matches) != 1:
            fail(ErrorCode.AMBIGUOUS_RULESET, "ruleset_version", "Multiple registrations match")
        provider = matches[0]
        if provider.identity.legal_status != "CURRENT":
            fail(
                ErrorCode.RULESET_STATUS_NOT_EXECUTABLE,
                "ruleset_version",
                "Legal lifecycle is not executable",
            )
        if not provider.identity.approved:
            fail(ErrorCode.RULESET_NOT_APPROVED, "ruleset_version", "Provider has no approval")
        if context.as_of_date != provider.identity.approved_as_of:
            fail(
                ErrorCode.RULESET_NOT_EFFECTIVE,
                "as_of_date",
                "No approved applicability for this date; no broader historical replay",
            )
        return provider


class RegulatoryEngine:
    def __init__(self, registry: RulesetRegistry) -> None:
        self._registry = registry

    def calculate(self, facts: RegulatoryFactSnapshot) -> RegulatoryCalculationResult:
        steps: list[TraceStep] = []
        operation = "validate_regulatory_context"

        def record(
            output: (
                RegulatoryContext
                | RulesetIdentity
                | ValidationEvidence
                | ClassificationResult
                | RegulatoryTreatment
                | RegulatoryExposureMeasure
                | RiskWeight
                | RwaResult
                | TeachingOutput
                | TraceCompletion
                | FailureDetail
            ),
            inputs: tuple[str, ...],
            reason: str,
            refs: tuple[RuleReference, ...] = (),
            warnings: tuple[str, ...] = (),
        ) -> None:
            sequence = len(steps) + 1
            steps.append(
                TraceStep(
                    sequence=sequence,
                    step_id=f"STEP-{sequence:02d}",
                    operation=operation,
                    reason_code=reason,
                    inputs_used=inputs,
                    output=output,
                    rule_refs=refs,
                    engine_contract=None if refs else "regulatory-engine.v1",
                    warnings=warnings,
                )
            )

        try:
            if type(facts) is not RegulatoryFactSnapshot:
                fail(
                    ErrorCode.INVALID_TYPE,
                    "facts",
                    "Expected immutable typed RegulatoryFactSnapshot",
                )
            record(facts.context, ("context",), "CONTEXT_STRUCTURALLY_VALID")
            operation = "select_approved_ruleset"
            provider = self._registry.resolve(facts.context)
            record(
                provider.identity,
                ("context.ruleset_version", "context.as_of_date"),
                "EXACT_PROVIDER_SELECTED",
            )
            operation = "validate_source_evidence"
            provider.validate_evidence()
            record(
                provider.identity,
                ("manifest_hash", "source_hashes", "review_approval"),
                "PINNED_EVIDENCE_VERIFIED",
            )
            # The provider supplies evidence refs; orchestration contains no jurisdiction branches.
            operation = "validate_institution"
            paths = provider.validate_institution(facts)
            classification_preview_refs = provider.classification_scope_refs()
            record(
                ValidationEvidence(fact_paths=paths, conclusion="IN_SCOPE"),
                paths,
                "INSTITUTION_PERIMETER_VALID",
                provider.institution_scope_refs(),
            )
            operation = "validate_corporate_definition_screen"
            paths = provider.validate_exposure(facts)
            record(
                ValidationEvidence(fact_paths=paths, conclusion="NEGATIVE_SCREENS_VALID"),
                paths,
                "EXPLICIT_EXCLUSIONS_AND_RECONCILIATION_VALID",
                classification_preview_refs,
            )
            operation = "classify_exposure"
            classification = provider.classify_exposure(facts)
            record(
                classification, ("facts",), classification.reason_codes[0], classification.rule_refs
            )
            operation = "resolve_regulatory_treatment"
            treatment = provider.resolve_treatment(classification)
            record(treatment, ("classification",), "TREATMENT_RESOLVED", treatment.rule_refs)
            operation = "determine_regulatory_exposure_measure"
            measure = provider.determine_regulatory_exposure_measure(facts)
            record(
                measure,
                ("facts", "regulatory_treatment"),
                "REGULATORY_MEASURE_DETERMINED",
                measure.rule_refs,
            )
            operation = "determine_risk_weight"
            weight = provider.determine_risk_weight(facts)
            record(
                weight,
                ("facts", "regulatory_treatment"),
                "RISK_WEIGHT_DETERMINED",
                weight.rule_refs,
            )
            operation = "calculate_rwa"
            rwa = provider.calculate_rwa(measure, weight)
            record(
                rwa,
                ("regulatory_exposure_measure", "risk_weight"),
                "EXACT_RWA_CALCULATED",
                rwa.rule_refs,
            )
            operation = "calculate_educational_capital_equivalent"
            teaching = provider.calculate_capital_teaching_outputs(rwa)
            if len(teaching) != 1:
                fail(
                    ErrorCode.INVALID_SCHEMA,
                    "capital_teaching_outputs",
                    "This contract requires one teaching output",
                )
            record(
                teaching[0],
                ("rwa",),
                "EDUCATIONAL_TRANSFORMATION_ONLY",
                teaching[0].rule_refs,
                teaching[0].warnings,
            )
            operation = "attach_citations_warnings_exclusions"
            references = {ref.rule_id: ref for step in steps for ref in step.rule_refs}
            citations = {
                citation.source_id: citation
                for ref in references.values()
                for citation in ref.citations
            }
            ordered_citations = tuple(citations[key] for key in sorted(citations))
            record(
                TraceCompletion(
                    source_ids=tuple(sorted(citations)), exclusions=treatment.exclusions
                ),
                ("trace", "source_evidence"),
                "EVIDENCE_ATTACHED",
                warnings=teaching[0].warnings,
            )
            return RegulatoryCalculationResult(
                jurisdiction=facts.context.jurisdiction,
                as_of_date=facts.context.as_of_date,
                fixture_version=facts.fixture_version,
                fact_schema_version=facts.schema_version,
                classification=classification,
                regulatory_treatment=treatment,
                regulatory_exposure_measure=measure,
                risk_weight=weight,
                rwa=rwa,
                capital_teaching_outputs=teaching,
                ruleset=provider.identity,
                rule_versions=tuple(
                    sorted((key, value.rule_version) for key, value in references.items())
                ),
                input_snapshot_hash=snapshot_hash(facts),
                calculation_trace=CalculationTrace(steps=tuple(steps)),
                source_citations=ordered_citations,
                warnings=teaching[0].warnings,
                exclusions=treatment.exclusions,
                request_metadata=facts.metadata,
            )
        except RegulatoryError as exc:
            record(
                FailureDetail(code=exc.code.value, field_path=exc.field_path, message=exc.message),
                (exc.field_path,),
                exc.code.value,
            )
            exc.validation_trace = CalculationTrace(steps=tuple(steps))
            raise
