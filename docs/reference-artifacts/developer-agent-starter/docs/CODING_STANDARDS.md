# Coding Standards

## Python
- Python 3.12+ target unless a dependency blocks it.
- FastAPI + Pydantic v2 schemas; SQLAlchemy 2.x style; Alembic migrations.
- `ruff` for lint/format; `mypy` for type checking; `pytest` for tests.
- Domain functions are typed and side-effect-minimal.
- No bare `except`; no silent error swallowing.
- Monetary values use Decimal or fixed-point rules where authoritative calculations require it.
- Time values are timezone-aware UTC internally.

## TypeScript
- TypeScript strict mode.
- Next.js + React; server/client boundaries explicit.
- ESLint + Prettier; Vitest for units; Playwright for critical journeys.
- Avoid `any`; validate external payloads at boundaries.
- UI components do not contain finance/regulatory business logic.

## General
- Small modules with one reason to change.
- Configuration through typed settings; no magic constants.
- Feature flags for experimental AI/video/voice behavior.
- All public interfaces documented.
- No secrets in source, logs, tests, fixtures, or screenshots.
- Comments explain why, not restate what code does.
