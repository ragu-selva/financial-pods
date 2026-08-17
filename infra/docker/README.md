# Local container services

Sprint 00 runs four local services through the root `compose.yaml`:

- `web`: the Next.js placeholder application on `http://localhost:3000`
- `api`: the FastAPI skeleton on `http://localhost:8000`
- `postgres`: PostgreSQL with the `vector` extension enabled
- `redis`: disposable cache/coordination storage

Copy `.env.example` to `.env` only when overriding the safe local defaults.
Do not reuse the example database password outside local development.

PostgreSQL data is kept in the named `postgres_data` volume. Redis persistence
is intentionally disabled because Redis is not a system of record. Removing
the PostgreSQL volume destroys local database data and is therefore not part
of the normal `down` command.
