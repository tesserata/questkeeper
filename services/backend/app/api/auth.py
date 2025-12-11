import asyncio
from dataclasses import dataclass

from fastapi import Depends, Header, HTTPException, status
from qk_api_contracts.enums import AppRole

from app.services.exceptions import RequiredRoleMissingException
from app.services.server_settings_service import get_app_role


@dataclass(frozen=True)
class AuthContext:
    user_id: int  # discord user id
    server_id: int  # discord server id (= tenant)
    roles: frozenset[int]  # user discord role ids


async def get_auth_context(
    x_qk_user_id: str = Header(..., alias="X-QK-User-ID"),
    x_qk_server_id: str = Header(..., alias="X-QK-Guild-ID"),
    x_qk_roles: str | None = Header(default=None, alias="X-QK-Roles"),
) -> AuthContext:
    try:
        user_id = int(x_qk_user_id)
        server_id = int(x_qk_server_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    roles: set[int] = set()
    if x_qk_roles:
        for raw in x_qk_roles.split(","):
            raw = raw.strip()
            if raw:
                roles.add(int(raw))

    return AuthContext(
        user_id=user_id,
        server_id=server_id,
        roles=frozenset(roles),
    )


def require_permission(required_role: AppRole):
    async def _dependency(
        auth: AuthContext = Depends(get_auth_context),
    ) -> None:
        if auth.server_id:
            coros = [get_app_role(auth.server_id, role) for role in auth.roles]
            app_roles = await asyncio.gather(*coros)

            if required_role not in set(app_roles):
                # TODO add reverse mapping to actual required role id
                raise RequiredRoleMissingException(required_role)

    return _dependency
