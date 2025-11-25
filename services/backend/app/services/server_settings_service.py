from qk_api_contracts.enums import AppRole

from app.infrastructure.db.uow import UnitOfWork


async def get_app_role(
    server_id: int,
    role_id: int,
) -> AppRole | None:
    async with UnitOfWork() as uow:
        return await uow.server_settings.get_app_role(server_id, role_id)
