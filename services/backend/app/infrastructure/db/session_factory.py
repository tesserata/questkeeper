from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import get_config

engine = create_async_engine(
    get_config().SQLALCHEMY_DATABASE_URI.unicode_string(), pool_size=10, max_overflow=20
)
session_factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
