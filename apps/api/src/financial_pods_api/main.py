"""FastAPI application entry point."""

from typing import Final

from fastapi import FastAPI, Request

from financial_pods_api import __version__
from financial_pods_api.correlation import CORRELATION_ID_HEADER, CorrelationIdMiddleware
from financial_pods_api.schemas import HealthResponse

SERVICE_NAME: Final = "financial-pods-api"

app = FastAPI(
    title="Financial Pods API",
    summary="Sprint 00 service foundation.",
    version=__version__,
)
app.add_middleware(CorrelationIdMiddleware)


@app.get(
    "/health",
    response_model=HealthResponse,
    response_model_exclude_none=True,
    summary="Check API process health",
    tags=["system"],
    responses={
        200: {
            "description": "The API process is healthy.",
            "headers": {
                CORRELATION_ID_HEADER: {
                    "description": "Validated or generated request correlation identifier.",
                    "schema": {"type": "string"},
                }
            },
        }
    },
)
async def health(request: Request) -> HealthResponse:
    """Return stable process-level status without probing future dependencies."""
    return HealthResponse(
        status="ok",
        service=SERVICE_NAME,
        version=__version__,
        trace_id=request.state.trace_id,
    )
