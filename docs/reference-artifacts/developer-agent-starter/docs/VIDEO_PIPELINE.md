# Video and Visual Content Pipeline

## Principle
Pre-render premium lessons; keep realtime AI for interruption, tutoring, whiteboard, calculations and assessments.

## Pipeline
1. Approved lesson outline and rule mappings.
2. Script generation from structured lesson object.
3. SME/editor review.
4. Storyboard with semantic segment IDs.
5. Generate visual assets (illustrative AI assets may use image-generation provider adapters).
6. Render authoritative formulas/tables/diagrams programmatically.
7. Generate narration/voice and optional avatar segments.
8. Compose video and captions.
9. Produce semantic timeline JSON.
10. QA visual, audio, citations, calculations and language.
11. Publish immutable lesson version to object storage/CDN.

## Rules
- Do not use generative-image text as the authoritative rendering of formulas or regulatory tables.
- Generated visuals must not imply they are regulator-issued diagrams.
- Maintain rights/provenance metadata for generated and human assets.
