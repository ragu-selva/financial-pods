"""Request correlation support for the API boundary."""

from __future__ import annotations

import re
from typing import Final
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

CORRELATION_ID_HEADER: Final = "X-Correlation-ID"
_CORRELATION_ID_PATTERN: Final = re.compile(r"^[A-Za-z0-9._:-]{1,128}$")


def resolve_correlation_id(candidate: str | None) -> str:
    """Return a safe caller-supplied correlation ID or generate a UUID."""
    if candidate is not None and _CORRELATION_ID_PATTERN.fullmatch(candidate):
        return candidate
    return str(uuid4())


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """Attach one validated correlation ID to every request and response."""

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        trace_id = resolve_correlation_id(request.headers.get(CORRELATION_ID_HEADER))
        request.state.trace_id = trace_id
        response = await call_next(request)
        response.headers[CORRELATION_ID_HEADER] = trace_id
        return response
