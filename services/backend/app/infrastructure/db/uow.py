from __future__ import annotations

from contextlib import AbstractAsyncContextManager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import get_config
from app.infrastructure.db.repositories.characters_repo import CharactersRepository
from app.infrastructure.db.repositories.server_settings_repo import (
    ServerSettingsRepository,
)
from app.infrastructure.db.repositories.sessions_repo import SessionsRepository
from app.infrastructure.outbox import OutboxWriter

engine = create_async_engine(
    get_config().SQLALCHEMY_DATABASE_URI.unicode_string(), pool_size=10, max_overflow=20
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class UnitOfWork(AbstractAsyncContextManager):
    session: AsyncSession | None = None
    _sessions_repo: SessionsRepository | None = None
    _characters_repo: CharactersRepository | None = None
    _server_settings_repo: ServerSettingsRepository | None = None
    _outbox: OutboxWriter | None = None

    def __init__(self) -> None:
        self._session_factory = SessionLocal
        self._sessions_repo_factory = SessionsRepository
        self._characters_repo_factory = CharactersRepository
        self._server_settings_repo_factory = ServerSettingsRepository
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
    def server_settings(self) -> ServerSettingsRepository:
        assert self.session is not None, "UoW not entered"
        if self._server_settings_repo is None:
            self._server_settings_repo = self._server_settings_repo_factory(self.session)
        return self._server_settings_repo

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
