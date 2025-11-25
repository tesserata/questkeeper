from collections.abc import Iterable
from uuid import UUID

from loguru import logger
from qk_api_contracts.enums import GameSystem
from sqlalchemy import Row, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.character.models import Character, PlayRecord
from app.infrastructure.db.models.character import CharacterORM, CharacterPlayHistoryORM
from app.infrastructure.db.models.session import SessionORM
from app.infrastructure.db.repositories._utility import get_version_header


class CharactersRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def create_character(self, entity: Character) -> None:
        logger.info(_character_domain_to_orm(entity))
        self._db.add(_character_domain_to_orm(entity))

    async def get_character_by_id(self, character_id: UUID) -> Character:
        character_row = (
            await self._db.execute(
                select(CharacterORM).where(CharacterORM.character_id == character_id)
            )
        ).scalar_one()
        return _character_orm_to_domain(character_row)

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
        return {row.character_id: _character_orm_to_domain(row) for row in character_rows}

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

        return [_play_history_orm_to_domain(row) for row in record_rows]


def _character_orm_to_domain(row: CharacterORM) -> Character:
    return Character(
        user_id=row.user_id,
        character_id=row.character_id,
        system=GameSystem(row.system) if row.system else None,
        name=row.name,
        level=row.level,
        race=row.race,
        class_name=row.class_name,
        subclass_name=row.subclass_name,
        notes=row.notes,
        version_header=get_version_header(row),
    )


def _character_domain_to_orm(entity: Character, row: CharacterORM | None = None) -> CharacterORM:
    if row is None:
        row = CharacterORM()
    row.character_id = entity.character_id
    row.user_id = entity.user_id
    row.system = entity.system
    row.name = entity.name
    row.level = entity.level
    row.race = entity.race
    row.class_name = entity.class_name
    row.subclass_name = entity.subclass_name
    row.notes = entity.notes

    return row


def _play_history_orm_to_domain(row: Row) -> PlayRecord:
    return PlayRecord(
        session_title=row.session_title,
        gm_user_id=row.gm_user_id,
        time=row.time,
        server_id=row.server_id,
        channel_id=row.channel_id,
        message_id=row.message_id,
    )
