from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    ForeignKey,
    Index,
    Integer,
    PrimaryKeyConstraint,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import ARRAY, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.models.base import Base, VersionMixin


class SessionORM(Base, VersionMixin):
    __tablename__ = "sessions"
    __table_args__ = (
        Index("ix_sessions_server_id", "server_id"),
        Index("ix_sessions_gm_user_id", "gm_user_id"),
        Index("ix_sessions_event_id", "event_id"),
        Index("ix_sessions_status", "status"),
        Index("ix_sessions_time", "time"),
        Index("ix_sessions_server_status_time", "server_id", "status", "time"),
        CheckConstraint("duration_minutes >= 0", name="check_duration_positive"),
        CheckConstraint("capacity >= 0", name="check_capacity_positive"),
        {"schema": "service"},
    )

    session_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    server_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    event_id: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("service.events.event_id"), nullable=True
    )
    gm_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    role_mentions: Mapped[list[str]] = mapped_column(
        ARRAY(Text), nullable=False, server_default=text("'{}'")
    )
    title: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''"))
    system: Mapped[str] = mapped_column(Text, nullable=False)
    vtt_link: Mapped[str | None] = mapped_column(Text, nullable=True)
    location: Mapped[str | None] = mapped_column(Text, nullable=True)
    additional_links: Mapped[list[str]] = mapped_column(
        ARRAY(Text), nullable=False, server_default=text("'{}'")
    )
    time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    channel_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    message_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("'Draft'"))

    # Relationships
    # event: Mapped[Optional["EventORM"]] = relationship(back_populates="sessions")
    # signups: Mapped[list["SignupORM"]] = relationship(back_populates="session")
    # character_histories: Mapped[list["CharacterHistoryORM"]] = relationship(
    #     back_populates="session"
    # )


class SignupORM(Base, VersionMixin):
    __tablename__ = "signups"
    __table_args__ = (
        PrimaryKeyConstraint("session_id", "user_id"),
        Index("ix_signups_session_role", "session_id", "role"),
        Index("ix_signups_character_id", "character_id"),
        {"schema": "service"},
    )

    session_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("service.sessions.session_id"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    character_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("service.characters.character_id"), nullable=False
    )
    role: Mapped[str] = mapped_column(Text, nullable=False)

    # Relationships
    # session: Mapped["SessionORM"] = relationship(back_populates="signups")
    # character: Mapped["CharacterORM"] = relationship(back_populates="signups")
