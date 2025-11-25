from fastapi import Depends, Header
from pydantic import BaseModel

from .auth import AuthContext, get_auth_context


class RequestMeta(BaseModel):
    request_id: int
    idempotency_key: str | None
    tenant_server_id: int
    user_id: int
    roles: frozenset[int]
    expected_version: int | None


async def get_request_meta(
    auth: AuthContext = Depends(get_auth_context),
    x_request_id: str = Header(default=None, alias="X-Request-ID"),
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
    if_match: str | None = Header(default=None, alias="If-Match"),
) -> RequestMeta:
    try:
        expected_version = int(if_match) if if_match else None
    except ValueError:
        expected_version = None

    return RequestMeta(
        request_id=int(x_request_id),
        idempotency_key=idempotency_key,
        tenant_server_id=auth.server_id,
        user_id=auth.user_id,
        roles=auth.roles,
        expected_version=expected_version,
    )
