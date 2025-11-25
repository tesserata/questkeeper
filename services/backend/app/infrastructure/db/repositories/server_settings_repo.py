from qk_api_contracts.enums import AppRole
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.server_settings import ServerRoleMappingORM


class ServerSettingsRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def get_app_role(self, server_id: int, role_id: int) -> AppRole | None:
        role = (
            await self._db.execute(
                select(ServerRoleMappingORM.app_role).where(
                    (ServerRoleMappingORM.server_id == server_id)
                    & (ServerRoleMappingORM.discord_role_id == role_id)
                )
            )
        ).scalar_one()

        try:
            return AppRole(role)
        except ValueError:
            return None
