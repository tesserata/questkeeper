from qk_api_contracts.enums import GameSystem, ScheduleStatus, SignupRole
from sqlalchemy import Row

from app.domain.character import Character, PlayRecord
from app.domain.common import VersionHeader
from app.domain.session import Session, Signup
from app.infrastructure.db.models.base import VersionMixin
from app.infrastructure.db.models.character import CharacterORM
from app.infrastructure.db.models.session import SessionORM, SignupORM


def session_orm_to_domain(row: SessionORM) -> Session:
    return Session(
        session_id=row.session_id,
        server_id=row.server_id,
        event_id=row.event_id,
        gm_user_id=row.gm_user_id,
        title=row.title,
        description=row.description,
        capacity=row.capacity,
        vtt_link=row.vtt_link,
        location=row.location,
        system=GameSystem(row.system) if row.system else None,
        additional_links=row.additional_links,
        role_mentions=row.role_mentions,
        status=ScheduleStatus(row.status),
        time=row.time,
        duration_minutes=row.duration_minutes,
        channel_id=row.channel_id,
        message_id=row.message_id,
        version_header=_get_version_header(row),
    )


def session_domain_to_orm(entity: Session, row: SessionORM | None = None) -> SessionORM:
    if not row:
        row = SessionORM()
    row.server_id = entity.server_id
    row.event_id = entity.event_id
    row.title = entity.title
    row.description = entity.description
    row.system = entity.system
    row.gm_user_id = entity.gm_user_id
    row.vtt_link = entity.vtt_link
    row.location = entity.location
    row.additional_links = list(entity.additional_links)
    row.time = entity.time
    row.duration_minutes = entity.duration_minutes
    row.capacity = entity.capacity
    row.role_mentions = list(entity.role_mentions)

    return row


def signup_orm_to_domain(row: SignupORM) -> Signup:
    return Signup(
        session_id=row.session_id,
        user_id=row.user_id,
        role=SignupRole(row.role),
        character_id=row.character_id,
    )


def signup_domain_to_orm(entity: Signup, row: SignupORM | None = None) -> SignupORM:
    if row is None:
        row = SignupORM()
    row.session_id = entity.session_id
    row.user_id = entity.user_id
    row.character_id = entity.character_id
    row.role = entity.role
    return row


def character_orm_to_domain(row: CharacterORM) -> Character:
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
        version_header=_get_version_header(row),
    )


def character_domain_to_orm(entity: Character, row: CharacterORM | None = None) -> CharacterORM:
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


def play_history_orm_to_domain(row: Row) -> PlayRecord:
    return PlayRecord(
        session_title=row.session_title,
        gm_user_id=row.gm_user_id,
        time=row.time,
        server_id=row.server_id,
        channel_id=row.channel_id,
        message_id=row.message_id,
    )


def _get_version_header(row: VersionMixin) -> VersionHeader:
    return VersionHeader(version=row.version, created_at=row.created_at, updated_at=row.updated_at)
