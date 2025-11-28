from uuid import UUID

from app.domain.characters import Character, PlayRecord
from app.domain.exceptions import ConcurrencyError
from app.infrastructure.db.repositories.characters_repo import CharactersRepository
from app.infrastructure.db.uow import UnitOfWork
from app.services.pagination import PaginationParams, decode_page_token, encode_page_token


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

        return await uow.characters.get_character_by_id(payload.character_id)


async def delete_character(character_id: UUID, expected_version: int) -> None:
    async with CharactersRepository() as repo:
        deleted = await repo.delete_character(character_id, expected_version)
    if not deleted:
        raise ConcurrencyError("character", str(character_id), expected_version)


async def update_character(payload: Character, expected_version: int) -> Character:
    async with UnitOfWork() as uow:
        await uow.characters.update_character(payload, expected_version)
        return await uow.characters.get_character_by_id(payload.character_id)


# Character queries
async def get_character_by_id(character_id: UUID) -> Character:
    async with CharactersRepository() as repo:
        return await repo.get_character_by_id(character_id)


async def list_characters(
    pagination: PaginationParams,
    user_ids: list[int] | None = None,
    system: str | None = None,
    level_min: int | None = None,
    level_max: int | None = None,
) -> tuple[list[Character], str | None]:
    cursor = decode_page_token(pagination.next_token) if pagination.next_token else None

    async with CharactersRepository() as repo:
        rows, next_cursor = await repo.list_characters(
            user_ids=user_ids,
            system=system,
            level_min=level_min,
            level_max=level_max,
            page_size=pagination.size,
            cursor=cursor,
        )

    next_page_token = encode_page_token(next_cursor) if next_cursor else None
    return rows, next_page_token


async def get_character_play_history(character_id: UUID) -> list[PlayRecord]:
    async with CharactersRepository() as repo:
        return await repo.get_character_play_history(character_id)
