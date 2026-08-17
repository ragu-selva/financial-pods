# Observability

Use OpenTelemetry instrumentation across web, API, workers and tutor flows.

## Required correlation dimensions
- trace_id
- request_id
- session_id
- tenant_id (non-sensitive identifier)
- lesson_id / lesson_version
- tutor_mode
- provider/model
- tool calls
- latency
- token/audio/video usage
- estimated cost

## SLO candidates
- learner web/API availability
- lesson start success
- tutor first-token latency
- voice first-audio latency
- calculation success/latency
- citation retrieval success
- content-publish workflow success

Never place full learner prompts, regulatory documents, secrets or sensitive enterprise payloads in unrestricted logs.
