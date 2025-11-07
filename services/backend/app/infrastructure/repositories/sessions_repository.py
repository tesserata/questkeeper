from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from ..db.models import SessionRow, SignupRow
from ...domain.session import Session, Signup, SignupRole

class SessionsRepo:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def load(self, session_id: str, *, for_update: bool = False) -> Session:
        q = select(SessionRow).where(SessionRow.id == session_id)
        if for_update:
            q = q.with_for_update()
        row = (await self._db.execute(q)).scalar_one()
        # assemble domain aggregate
        signups = {}
        rs = await self._db.execute(select(SignupRow).where(SignupRow.session_id == session_id))
        for s in rs.scalars():
            signups[s.user_id] = Signup(
                user_id=s.user_id,
                role=SignupRole[s.role],
                active=s.active,
                character_id=s.character_id,
                no_show=s.no_show,
                created_at=s.created_at,
                updated_at=s.updated_at,
            )
        return Session(
            session_id=row.id,
            server_id=row.server_id,
            event_id=row.event_id,
            gm_user_id=row.gm_user_id,
            title=row.title,
            summary=row.summary,
            capacity=row.capacity,
            signups=signups,
            version=row.version,
        )

    async def save(self, agg: Session) -> None:
        # Upsert session
        await self._db.execute(
            update(SessionRow)
            .where(SessionRow.id == agg.session_id)
            .values(
                title=agg.title,
                summary=agg.summary,
                capacity=agg.capacity,
                version=agg.version,
            )
        )
        # Replace signup rows for simplicity (small cardinality). For high write rate, do diffing.
        await self._db.execute(
            # sa.text("DELETE FROM session_signups WHERE session_id = :sid"), {"sid": agg.session_id}
        )
        self._db.add_all(
            SignupRow(
                session_id=agg.session_id,
                user_id=s.user_id,
                role=s.role.name,
                active=s.active,
                character_id=s.character_id,
                no_show=s.no_show,
                created_at=s.created_at,
                updated_at=s.updated_at,
            ) for s in agg.signups.values()
        )
