from collections.abc import Iterable
from uuid import UUID

from loguru import logger
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.character import Character, PlayRecord
from app.infrastructure.db.models.character import CharacterORM, CharacterPlayHistoryORM
from app.infrastructure.db.models.session import SessionORM
from app.infrastructure.repositories.mappers import (
    character_domain_to_orm,
    character_orm_to_domain,
    play_history_orm_to_domain,
)


class CharactersRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def create_character(self, entity: Character) -> None:
        logger.info(character_domain_to_orm(entity))
        self._db.add(character_domain_to_orm(entity))

    async def get_character_by_id(self, character_id: UUID) -> Character:
        character_row = (
            await self._db.execute(
                select(CharacterORM).where(CharacterORM.character_id == character_id)
            )
        ).scalar_one()
        return character_orm_to_domain(character_row)

    async def get_many_by_ids(self, character_ids: Iterable[UUID]) -> dict[UUID, Character]:
        character_rows = (
            (
                await self._db.execute(
                    select(CharacterORM).where(CharacterORM.character_id.in_(character_ids))
                )
            )
            .scalars()
            .all()
        )
        return {row.character_id: character_orm_to_domain(row) for row in character_rows}

    async def delete_character(self, character_id: UUID) -> None:
        await self._db.execute(
            delete(CharacterORM).where(CharacterORM.character_id == character_id)
        )

    async def get_character_play_history(self, character_id: UUID) -> list[PlayRecord]:
        record_rows = (
            await self._db.execute(
                select(
                    SessionORM.title.label("session_title"),
                    SessionORM.gm_user_id,
                    SessionORM.time,
                    SessionORM.server_id,
                    SessionORM.channel_id,
                    SessionORM.message_id,
                )
                .select_from(CharacterPlayHistoryORM)
                .outerjoin(
                    SessionORM,
                    CharacterPlayHistoryORM.session_id == SessionORM.session_id,
                )
                .where(CharacterPlayHistoryORM.character_id == character_id)
                .order_by(CharacterPlayHistoryORM.created_at.desc())
            )
        ).all()

        return [play_history_orm_to_domain(row) for row in record_rows]
