from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session_factory import session_factory


class BaseRepository:
    def __init__(self, session: AsyncSession | None = None):
        self._session = session

    async def __aenter__(self) -> "BaseRepository":
        self._session = session_factory()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._session:
            if exc:
                await self._session.rollback()
            await self._session.close()
