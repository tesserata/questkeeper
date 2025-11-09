from qk_api_contracts.enums import SignupRole
from sqlalchemy import select, text, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.session import Session, Signup
from app.infrastructure.db.models.event import EventORM     # noqa: F401
from app.infrastructure.db.models.session import SessionORM
from app.infrastructure.db.models.signup import SignupORM


class SessionsRepository:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def create(self, agg: Session) -> None:
        # insert session row
        self._db.add(
            SessionORM(
                server_id=agg.server_id,
                event_id=agg.event_id,
                title=agg.title,
                summary=agg.summary,
                system=agg.system,
                gm_user_id=agg.gm_user_id,
                vtt_link=agg.vtt_link,
                location=agg.location,
                additional_links=agg.additional_links,
                time=agg.time,
                duration_minutes=agg.duration_minutes,
                capacity=agg.capacity,
                role_mentions=agg.role_mentions,
            )
        )

    async def read(self, session_id: str, *, for_update: bool = False) -> Session:
        q = select(SessionORM).where(SessionORM.session_id == session_id)
        if for_update:
            q = q.with_for_update()
        row = (await self._db.execute(q)).scalar_one()
        # assemble domain aggregate
        signups = {}
        rs = await self._db.execute(select(SignupORM).where(SignupORM.session_id == session_id))
        for s in rs.scalars():
            signups[s.user_id] = Signup(
                user_id=s.user_id,
                role=SignupRole[s.role],
                character_id=s.character_id,
                created_at=s.created_at,
                updated_at=s.updated_at,
            )
        return Session(
            session_id=row.session_id,
            server_id=row.server_id,
            event_id=row.event_id,
            gm_user_id=row.gm_user_id,
            title=row.title,
            summary=row.summary,
            capacity=row.capacity,
            signups=signups,
            version=row.version,
        )

    async def update(self, agg: Session) -> None:
        # Upsert session
        await self._db.execute(
            update(SessionORM)
            .where(SessionORM.session_id == agg.session_id)
            .values(
                title=agg.title,
                summary=agg.summary,
                capacity=agg.capacity,
                version=agg.version,
            )
        )
        # Replace signup rows for simplicity (small cardinality). For high write rate, do diffing.
        await self._db.execute(
            text("DELETE FROM session_signups WHERE session_id = :sid"), {"sid": agg.session_id}
        )
        self._db.add_all(
            SignupORM(
                session_id=agg.session_id,
                user_id=s.user_id,
                role=s.role.name,
                character_id=s.character_id,
                created_at=s.created_at,
                updated_at=s.updated_at,
            )
            for s in agg.signups.values()
        )
