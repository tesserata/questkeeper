from uuid import UUID

from app.domain.character import Character, PlayRecord
from app.infrastructure.db.uow import UnitOfWork


# Character commands
async def create_character(
    payload: Character,
) -> Character:
    async with UnitOfWork() as uow:
        await uow.characters.create_character(payload)
        # await uow.outbox.enqueue(
        #     topic="discord.session.created",
        #     key=session_id,
        #     payload={"session_id": session_id, "version": version},
        # )
    return payload


async def delete_character(character_id: UUID) -> None:
    async with UnitOfWork() as uow:
        await uow.characters.delete_character(character_id)


# Character queries
async def get_character_by_id(character_id: UUID) -> Character:
    async with UnitOfWork() as uow:
        return await uow.characters.get_character_by_id(character_id)


async def get_character_play_history(character_id: UUID) -> list[PlayRecord]:
    async with UnitOfWork() as uow:
        return await uow.characters.get_character_play_history(character_id)
