# API Standards

- REST/JSON for CRUD and deterministic tools.
- Server-Sent Events for streamed text tutor responses unless bidirectional transport is required.
- WebRTC for browser realtime audio; WebSocket only when provider/server topology requires it.
- OpenAPI is generated from FastAPI and treated as a compatibility contract.
- Use explicit version prefix (`/api/v1`).
- Idempotency keys required for billable or state-changing async operations.
- Pagination uses cursor-based pagination for large collections.
- All responses include a request/trace ID.
- Errors follow one envelope: `code`, `message`, `details`, `trace_id`.
- Do not expose stack traces or provider secrets.
- Calculation responses include `ruleset_version`, `input_hash`, `result`, `steps`, and `source_rule_ids`.
- Tutor responses include grounded citation objects separately from natural-language text.
