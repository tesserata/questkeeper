import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from app.infrastructure.db.models.base import Base, TimestampMixin, VersionMixin
from app.infrastructure.db.models.domain import Event, Session, Character, CharacterHistory, Signup
from app.infrastructure.db.models.idempotency import IdempotencyKey
from app.infrastructure.db.models.outbox import Outbox, OutboxDLQ
from app.infrastructure.db.models.server_settings import ServerSettings, ServerRoleMapping


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata

def get_url() -> str:
    user = os.getenv("POSTGRES_USER")
    pwd = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    return f"postgresql+psycopg://{user}:{pwd}@{host}:{port}/{db}?sslmode=disable"


def run_migrations_offline() -> None:
    # url = config.get_main_option("sqlalchemy.url")
    # url = f"postgresql+apsyncpg://qk_admin:password@0.0.0.0:5432/questkeeper"
    url = get_url()

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = get_url()
    print(configuration)

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()