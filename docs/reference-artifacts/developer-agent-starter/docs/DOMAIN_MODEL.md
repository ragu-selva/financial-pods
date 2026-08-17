# Domain Model

## Regulatory/content entities
- `RegulatorySource`: authority, jurisdiction, canonical URL, publication date.
- `RegulatoryDocument`: title, status, version, effective dates, source snapshot hash.
- `Rule`: canonical concept-level rule identifier.
- `JurisdictionRule`: jurisdiction implementation mapped to canonical Rule.
- `RuleCitation`: exact source locator, excerpt metadata, link.
- `Concept`: teachable finance concept with prerequisites.
- `Lesson`: pedagogical unit.
- `LessonVersion`: immutable published lesson version.
- `LessonSegment`: timestamped semantic segment linked to concepts/rules/examples/tools.
- `Example`: synthetic scenario with reviewed facts.
- `CalculationDefinition`: deterministic tool contract and rule-set version.

## Learner entities
- `LearnerProfile`: language, timezone, experience goals and accessibility preferences.
- `Enrollment`: course/path state.
- `LearningEvent`: append-only interaction event.
- `ConceptMastery`: current derived state by concept.
- `Misconception`: detected misconception with evidence and resolution state.
- `AssessmentAttempt`: quiz/viva/practice attempt.
- `TutorConversation`: session and transcript metadata.

## Platform entities
- `Tenant`, `User`, `Role`, `Entitlement`, `Subscription`.
- `ProviderUsage`: model/provider/tokens/audio/video/cost attribution.
- `ContentReview`: reviewer, decision, comments, evidence.
- `AuditEvent`: security/admin/content audit trail.

## Versioning
Published regulatory and learning objects are immutable. Corrections create new versions. Learner activity records the exact lesson/rule/calculation versions used at the time.
