from collections.abc import Iterable
from uuid import UUID

from qk_api_contracts.enums import GameSystem
from sqlalchemy import Row, delete, select, tuple_, update

from app.domain.characters import Character, PlayRecord
from app.infrastructure.db.helpers import Cursor, get_version_header
from app.infrastructure.db.models.character import CharacterORM, CharacterPlayHistoryORM
from app.infrastructure.db.models.session import SessionORM
from app.infrastructure.db.repositories._base import BaseRepository


class CharactersRepository(BaseRepository):
    async def create_character(self, entity: Character) -> None:
        value = _character_domain_to_orm(entity)
        self._session.add(value)

    async def delete_character(self, character_id: UUID, expected_version: int) -> bool:
        stmt = delete(CharacterORM).where(
            CharacterORM.character_id == character_id,
            CharacterORM.version == expected_version,
        )
        result = await self._session.execute(stmt)
        return result.rowcount == 1

    async def update_character(self, entity: Character, expected_version: int) -> bool:
        value_mapping = {
            "user_id": entity.user_id,
            "system": entity.system,
            "name": entity.name,
            "level": entity.level,
            "race": entity.race,
            "class_name": entity.class_name,
            "subclass_name": entity.subclass_name,
            "notes": entity.notes,
        }
        stmt = (
            update(CharacterORM)
            .where(
                CharacterORM.character_id == entity.character_id,
                CharacterORM.version == expected_version,
            )
            .values(**value_mapping)
        )
        result = await self._session.execute(stmt)
        return result.rowcount == 1

    async def get_character_by_id(self, character_id: UUID) -> Character:
        stmt = select(CharacterORM).where(CharacterORM.character_id == character_id)

        character_row = (await self._session.execute(stmt)).scalar_one()
        return _character_orm_to_domain(character_row)

    async def get_many_by_ids(self, character_ids: Iterable[UUID]) -> dict[UUID, Character]:
        stmt = select(CharacterORM).where(CharacterORM.character_id.in_(character_ids))

        character_rows = (await self._session.execute(stmt)).scalars().all()
        return {row.character_id: _character_orm_to_domain(row) for row in character_rows}

    async def list_characters(
        self,
        page_size: int,
        user_ids: list[int] | None = None,
        system: str | None = None,
        level_min: int | None = None,
        level_max: int | None = None,
        cursor: Cursor | None = None,
    ) -> tuple[list[Character], Cursor | None]:
        stmt = (
            select(CharacterORM)
            .order_by(CharacterORM.created_at, CharacterORM.character_id)
            .limit(page_size + 1)
        )

        if user_ids:
            stmt = stmt.where(CharacterORM.user_id.in_(user_ids))
        if system:
            stmt = stmt.where(CharacterORM.system == system)

        if level_min is not None:  # to avoid skipping 0
            stmt = stmt.where(CharacterORM.level >= level_min)

        if level_max is not None:
            stmt = stmt.where(CharacterORM.level <= level_max)

        if cursor:
            # WHERE (created_at, character_id) > (:created_at, :character_id)
            stmt = stmt.where(
                tuple_(CharacterORM.created_at, CharacterORM.character_id)
                > tuple_(cursor.created_at, cursor.last_id)
            )

        result = await self._session.scalars(stmt)
        rows = list(result)

        has_next = len(rows) > page_size
        next_cursor: Cursor | None = None

        if has_next:
            rows = rows[:page_size]
            last = rows[-1]
            next_cursor = Cursor(
                created_at=last.created_at,
                last_id=last.character_id,
            )

        rows = [_character_orm_to_domain(row) for row in rows]

        return rows, next_cursor

    async def get_character_play_history(self, character_id: UUID) -> list[PlayRecord]:
        record_rows = (
            await self._session.execute(
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


# Mappings
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
