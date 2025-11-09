import json
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.session import SessionORM, SessionViewORM
from app.infrastructure.db.models.signup import SignupORM


async def update_view(db: AsyncSession, session_id: UUID, version: int) -> int:
    # pull current state
    s = (
        await db.execute(select(SessionORM).where(SessionORM.session_id == session_id))
    ).scalar_one()
    rs = await db.execute(select(SignupORM).where(SessionORM.session_id == session_id))
    signups = [
        dict(user_id=r.user_id, role=r.role, character_id=r.character_id) for r in rs.scalars()
    ]
    view = {
        "session_id": s.session_id,
        "title": s.title,
        "summary": s.summary,
        "capacity": s.capacity,
        "version": version,
        "signups": signups,
    }
    payload = json.dumps(view, separators=(",", ":"))

    row = await db.get(SessionViewORM, session_id)
    if row:
        await db.execute(
            update(SessionViewORM)
            .where(SessionViewORM.session_id == session_id)
            .set({"view_json": payload, "version": version})
        )
    else:
        db.add(SessionViewORM(session_id=session_id, view_json=payload, version=version))
    return version
