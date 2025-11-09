from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Index,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import ARRAY, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.models.base import Base, TimestampMixin, VersionMixin


class EventORM(Base, TimestampMixin, VersionMixin):
    __tablename__ = "events"
    __table_args__ = (
        Index("events_server_id_idx", "server_id"),
        Index("events_status_idx", "status"),
        Index("events_time_idx", "time_start", "time_end"),
        Index("events_server_status_start_idx", "server_id", "status", "time_start"),
        CheckConstraint("time_end >= time_start", name="check_time_end_after_start"),
        {"schema": "service"},
    )

    event_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    server_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    role_mentions: Mapped[list[str]] = mapped_column(
        ARRAY(Text), nullable=False, server_default=text("'{}'")
    )
    title: Mapped[str] = mapped_column(Text, nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''"))
    system: Mapped[str] = mapped_column(Text, nullable=False)
    time_start: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    time_end: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    channel_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    message_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("'Draft'"))

    # Relationships
    # sessions: Mapped[list["SessionORM"]] = relationship(back_populates="event")
