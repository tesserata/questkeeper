from uuid import UUID

from qk_api_contracts.enums import GameSystem, ScheduleStatus, SignupRole
from sqlalchemy import select, text, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.sessions import Session, Signup
from app.infrastructure.db.helpers import get_version_header
from app.infrastructure.db.models.session import SessionORM, SignupORM


class SessionsRepository:
    def __init__(self, session: AsyncSession | None = None):
        self._session = session

    async def create_session(self, entity: Session) -> None:
        self._session.add(_session_domain_to_orm(entity))

    async def get_session(self, session_id: UUID, with_signups: bool = False) -> Session:
        session_row = (
            await self._session.execute(
                select(SessionORM).where(SessionORM.session_id == session_id)
            )
        ).scalar_one()
        session = _session_orm_to_domain(session_row)

        if with_signups:
            signup_rows = await self._session.execute(
                select(SignupORM).where(SignupORM.session_id == session_id)
            )
            signups = [_signup_orm_to_domain(s) for s in signup_rows.scalars()]

            session.main_signups = [s for s in signups if s.role == SignupRole.MAIN]
            session.reserve_signups = [s for s in signups if s.role == SignupRole.RESERVE]

        return session

    async def update(self, entity: Session) -> None:
        # Upsert session
        await self._session.execute(
            update(SessionORM)
            .where(SessionORM.session_id == entity.session_id)
            .values(
                title=entity.title,
                description=entity.description,
                capacity=entity.capacity,
                version=entity.version_header.version,
            )
        )
        # Replace signup rows for simplicity (small cardinality). For high write rate, do diffing.
        await self._session.execute(
            text("DELETE FROM session_signups WHERE session_id = :sid"),
            {"sid": entity.session_id},
        )
        self._session.add_all(
            SignupORM(
                session_id=entity.session_id,
                user_id=s.user_id,
                role=s.role.name,
                character_id=s.character_id,
                created_at=s.created_at,
                updated_at=s.updated_at,
            )
            for s in entity.signups.values()
        )


def _session_orm_to_domain(row: SessionORM) -> Session:
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
        version_header=get_version_header(row),
    )


def _session_domain_to_orm(entity: Session, row: SessionORM | None = None) -> SessionORM:
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


def _signup_orm_to_domain(row: SignupORM) -> Signup:
    return Signup(
        session_id=row.session_id,
        user_id=row.user_id,
        role=SignupRole(row.role),
        character_id=row.character_id,
    )


def _signup_domain_to_orm(entity: Signup, row: SignupORM | None = None) -> SignupORM:
    if row is None:
        row = SignupORM()
    row.session_id = entity.session_id
    row.user_id = entity.user_id
    row.character_id = entity.character_id
    row.role = entity.role
    return row
