import logging

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.services.exceptions import (
    AggregateNotFoundException,
    ConcurrencyConflictException,
    PermissionDeniedException,
    ServiceException,
)

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    # ...
    @app.exception_handler(ServiceException)
    async def handle_service_exception(request: Request, exc: ServiceException):
        if isinstance(exc, AggregateNotFoundException):
            status_code = status.HTTP_404_NOT_FOUND
        elif isinstance(exc, ConcurrencyConflictException):
            status_code = status.HTTP_409_CONFLICT
        elif isinstance(exc, PermissionDeniedException):
            status_code = status.HTTP_403_FORBIDDEN
        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        detail = f"{exc.msg} [{exc.name}]"

        logger.info("Service error %s %s -> %s", request.method, request.url, detail)
        return JSONResponse(status_code=status_code, content={"detail": detail})
