# Contributing

## Start here

Read `AGENTS.md` and its required documents. Confirm the active sprint and acceptance criteria before editing.

## Workflow

1. Create a small issue/task tied to an active-sprint acceptance criterion.
2. Use a focused branch and keep changes reviewable.
3. Add tests with behavior; add citations and version metadata with regulatory content.
4. Run formatting, lint, type checks, tests, and builds through the task runner.
5. Update the active sprint review evidence and documentation.
6. Request review; do not merge with failing required checks.

## Conventions

- Conventional commits are preferred: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `build:`, `ci:`, `chore:`.
- Python uses Ruff formatting/lint, mypy, pytest, explicit types, and Pydantic boundary validation.
- TypeScript uses strict mode, ESLint, Prettier, Vitest, and Playwright where applicable.
- Never commit `.env`, credentials, customer information, generated output, caches, local databases, or Terraform state.
- Do not alter finalized files in `docs/reference-artifacts/`.

## Review priorities

Correctness, regulatory traceability, calculation determinism, security/privacy, tests, accessibility, maintainability, and sprint scope.
