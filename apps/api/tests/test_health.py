"""Contract tests for the Sprint 00 health endpoint."""

from uuid import UUID

from fastapi.testclient import TestClient

from financial_pods_api.correlation import CORRELATION_ID_HEADER
from financial_pods_api.main import app

client = TestClient(app)


def test_health_returns_stable_typed_payload() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload == {
        "status": "ok",
        "service": "financial-pods-api",
        "version": "0.1.0",
        "trace_id": response.headers[CORRELATION_ID_HEADER],
    }
    assert str(UUID(payload["trace_id"])) == payload["trace_id"]


def test_health_preserves_valid_correlation_id() -> None:
    trace_id = "client-request_2026:08.16"

    response = client.get("/health", headers={CORRELATION_ID_HEADER: trace_id})

    assert response.status_code == 200
    assert response.headers[CORRELATION_ID_HEADER] == trace_id
    assert response.json()["trace_id"] == trace_id


def test_health_replaces_invalid_correlation_id() -> None:
    response = client.get("/health", headers={CORRELATION_ID_HEADER: "not valid with spaces"})

    assert response.status_code == 200
    generated_trace_id = response.headers[CORRELATION_ID_HEADER]
    assert generated_trace_id != "not valid with spaces"
    assert str(UUID(generated_trace_id)) == generated_trace_id
    assert response.json()["trace_id"] == generated_trace_id


def test_openapi_documents_health_response_model() -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    health_operation = schema["paths"]["/health"]["get"]
    success_schema = health_operation["responses"]["200"]["content"]["application/json"]["schema"]
    assert success_schema == {"$ref": "#/components/schemas/HealthResponse"}


def test_correlation_header_is_added_to_non_health_responses() -> None:
    response = client.get("/missing")

    assert response.status_code == 404
    trace_id = response.headers[CORRELATION_ID_HEADER]
    assert str(UUID(trace_id)) == trace_id
