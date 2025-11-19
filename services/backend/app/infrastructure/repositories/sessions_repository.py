from uuid import UUID

from qk_api_contracts.enums import SignupRole
from sqlalchemy import select, text, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.session import Session
from app.infrastructure.db.models.session import SessionORM, SignupORM
from app.infrastructure.repositories.mappers import (
    session_domain_to_orm,
    session_orm_to_domain,
    signup_orm_to_domain,
)


class SessionsRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def create_session(self, entity: Session) -> None:
        self._db.add(session_domain_to_orm(entity))

    async def get_session(self, session_id: UUID, with_signups: bool = False) -> Session:
        session_row = (
            await self._db.execute(select(SessionORM).where(SessionORM.session_id == session_id))
        ).scalar_one()
        session = session_orm_to_domain(session_row)

        if with_signups:
            signup_rows = await self._db.execute(
                select(SignupORM).where(SignupORM.session_id == session_id)
            )
            signups = [signup_orm_to_domain(s) for s in signup_rows.scalars()]

            session.main_signups = [s for s in signups if s.role == SignupRole.MAIN]
            session.reserve_signups = [s for s in signups if s.role == SignupRole.RESERVE]

        return session

    async def update(self, entity: Session) -> None:
        # Upsert session
        await self._db.execute(
            update(SessionORM)
            .where(SessionORM.session_id == entity.session_id)
            .values(
                title=entity.title,
                summary=entity.summary,
                capacity=entity.capacity,
                version=entity.version,
            )
        )
        # Replace signup rows for simplicity (small cardinality). For high write rate, do diffing.
        await self._db.execute(
            text("DELETE FROM session_signups WHERE session_id = :sid"), {"sid": entity.session_id}
        )
        self._db.add_all(
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
