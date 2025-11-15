from qk_api_contracts.enums import GameSystem, ScheduleStatus, SignupRole

from app.domain.common import VersionHeader
from app.domain.session import Session, Signup
from app.infrastructure.db.models.base import VersionMixin
from app.infrastructure.db.models.session import SessionORM, SignupORM


def session_orm_to_domain(row: SessionORM) -> Session:
    return Session(
        session_id=row.session_id,
        server_id=row.server_id,
        event_id=row.event_id,
        gm_user_id=row.gm_user_id,
        title=row.title,
        summary=row.summary,
        capacity=row.capacity,
        vtt_link=row.vtt_link,
        location=row.location,
        system=GameSystem(row.system),
        additional_links=row.additional_links,
        role_mentions=row.role_mentions,
        status=ScheduleStatus(row.status),
        time=row.time,
        duration_minutes=row.duration_minutes,
        channel_id=row.channel_id,
        message_id=row.message_id,
        version_header=_get_version_header(row),
        created_at=row.created_at
    )


def session_domain_to_orm(entity: Session, row: SessionORM | None = None) -> SessionORM:
    if not row:
        row = SessionORM()
    row.server_id = entity.server_id
    row.event_id = entity.event_id
    row.title = entity.title
    row.summary = entity.summary
    row.system = entity.system
    row.gm_user_id = entity.gm_user_id
    row.vtt_link = entity.vtt_link
    row.location = entity.location
    row.additional_links = entity.additional_links
    row.time = entity.time
    row.duration_minutes = entity.duration_minutes
    row.capacity = entity.capacity
    row.role_mentions = entity.role_mentions

    return row


def signup_orm_to_domain(signup_row: SignupORM) -> Signup:
    return Signup(
        session_id=signup_row.session_id,
        user_id=signup_row.user_id,
        role=SignupRole(signup_row.role),
        character_id=signup_row.character_id,
    )


def signup_domain_to_orm(entity: Signup, row: SignupORM | None = None) -> SignupORM:
    if row is None:
        row = SignupORM()
    row.session_id = entity.session_id
    row.user_id = entity.user_id
    row.character_id = entity.character_id
    row.role = entity.role
    return row


def _get_version_header(row: VersionMixin) -> VersionHeader:
    return VersionHeader(version=row.version, updated_at=row.updated_at)
