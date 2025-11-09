from datetime import datetime
from typing import Any

from sqlalchemy import (
    BigInteger,
    Index,
    Integer,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class IdempotencyKeyORM(Base):
    __tablename__ = "idempotency_keys"
    __table_args__ = (
        Index("ix_idempotency_keys_server_created", "server_id", "created_at"),
        {"schema": "service"},
    )

    idempotency_key: Mapped[str] = mapped_column(Text, primary_key=True)
    server_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    request_hash: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False)
    response_code: Mapped[int | None] = mapped_column(Integer, nullable=True)
    response_body_hash: Mapped[str | None] = mapped_column(Text, nullable=True)
    meta: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, server_default=text("'{}'"))
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    locked_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    processed_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
