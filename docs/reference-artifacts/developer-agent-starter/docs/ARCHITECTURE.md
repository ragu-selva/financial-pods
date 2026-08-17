# Architecture

## Architecture style
Modular monolith first, with clear service boundaries. Deploy separate web, API, worker, and realtime components, while preserving a shared domain package. Split into microservices only after independent scaling or organizational boundaries justify it.

## Primary components
- `apps/web`: Next.js/React/TypeScript learner and admin UI.
- `apps/api`: FastAPI control plane and REST/SSE APIs.
- `apps/worker`: durable/background jobs for content, indexing, media, analytics, and evaluations.
- `apps/realtime`: voice-session broker and realtime tutor gateway where needed.
- `packages/domain`: provider-independent domain entities and business rules.
- `packages/calculations`: deterministic Basel/finance calculation interfaces and adapters.
- `packages/ai`: tutor orchestration, tools, policies, retrieval, prompt versions, provider adapters.
- `packages/content`: lesson/rule schemas, publication state machine, localization.
- `packages/telemetry`: tracing, metrics, structured logging, cost events.

## Data stores
- PostgreSQL: source of truth for users, tenants, learning, content metadata, rules, versions, transactions, mastery.
- pgvector: semantic retrieval within PostgreSQL for V1.
- Redis: ephemeral session/cache/rate-limit state, never primary source of truth.
- Object storage: videos, audio, images, transcripts, exported evidence.
- Graph database: deferred. Model graph semantics in relational tables first; add Neo4j only when query complexity/performance proves need.

## Core dependency rule
UI -> API/application services -> domain interfaces -> infrastructure adapters.
LLM/voice/video vendors are infrastructure adapters, never domain dependencies.

## Runtime pathways
### Lesson playback
CDN -> web player -> semantic timeline metadata -> learner events -> mastery service.

### Text tutor
Web -> tutor API/SSE -> tutor orchestrator -> retrieval + tools -> policy validation -> streamed response -> transcript/mastery events.

### Voice tutor
Browser -> realtime WebRTC/provider -> tutor tools through server-authorized session -> transcript/events -> learner model. Do not expose permanent provider credentials to browser.

### Calculation
Tutor/UI -> calculation service -> versioned deterministic rules -> result + explanation metadata. LLM explains result; it does not compute the authoritative figure.

## Deployment recommendation
V1: AWS, one production region, ECS Fargate for stateless containers, RDS PostgreSQL, ElastiCache Redis, S3 + CloudFront, WAF, Secrets Manager/KMS, managed workflow/orchestration. Kubernetes is not required for V1.
