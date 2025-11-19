from __future__ import annotations

from contextlib import AbstractAsyncContextManager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import CONFIG
from app.infrastructure.outbox.writer import OutboxWriter
from app.infrastructure.repositories.characters_repository import CharactersRepository
from app.infrastructure.repositories.sessions_repository import SessionsRepository

engine = create_async_engine(CONFIG.db_dsn, pool_size=10, max_overflow=20)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class UnitOfWork(AbstractAsyncContextManager):
    session: AsyncSession | None = None
    _sessions_repo: SessionsRepository | None = None
    _characters_repo: CharactersRepository | None = None
    _outbox: OutboxWriter | None = None

    def __init__(self) -> None:
        self._session_factory = SessionLocal
        self._sessions_repo_factory = SessionsRepository
        self._characters_repo_factory = CharactersRepository
        self._outbox_factory = OutboxWriter

    @property
    def sessions(self) -> SessionsRepository:
        assert self.session is not None, "UoW not entered"
        if self._sessions_repo is None:
            self._sessions_repo = self._sessions_repo_factory(self.session)
        return self._sessions_repo

    @property
    def characters(self) -> CharactersRepository:
        assert self.session is not None, "UoW not entered"
        if self._characters_repo is None:
            self._characters_repo = self._characters_repo_factory(self.session)
        return self._characters_repo

    @property
    def outbox(self) -> OutboxWriter:
        assert self.session is not None, "UoW not entered"
        if self._outbox is None:
            self._outbox = self._outbox_factory(self.session)
        return self._outbox

    async def __aenter__(self) -> UnitOfWork:
        self.session = self._session_factory()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        try:
            if exc:
                await self.session.rollback()
                raise
            else:
                await self.session.commit()

        finally:
            self._sessions_repo = None
            self._outbox = None
            if self.session is not None:
                await self.session.close()
                self.session = None
