# Financial Pods API

Sprint 00 provides only the FastAPI application skeleton and its health contract. It contains no
financial, regulatory, lesson, tutor, authentication, or publishing behavior.

## Runtime contract

- Python: 3.12+
- Application: `financial_pods_api.main:app`
- Port: `8000`
- Health: `GET /health`
- Correlation header: `X-Correlation-ID`

A successful health response is:

```json
{
  "status": "ok",
  "service": "financial-pods-api",
  "version": "0.1.0",
  "trace_id": "6d751bce-f0b7-4f78-8a56-f3ae50da12df"
}
```

The API accepts an inbound `X-Correlation-ID` when it is 1-128 characters and contains only
letters, numbers, `.`, `_`, `:`, or `-`. Otherwise, it generates a UUID. The effective value is
returned in both the response body and the `X-Correlation-ID` response header.

## Local verification

Install the complete locked environment with uv:

```text
uv sync --frozen
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
uv build
```

Run the service with:

```text
uv run uvicorn financial_pods_api.main:app --app-dir src --host 0.0.0.0 --port 8000
```

`uv.lock` supports reproducible uv-based development. The root setup task and CI consume the
fully pinned `requirements-dev.lock`; Docker consumes the fully pinned `requirements.lock`.
Direct runtime pins in `pyproject.toml` must remain synchronized with both lock formats.
