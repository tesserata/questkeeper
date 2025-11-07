from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import (
    BigInteger,
    Boolean,
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
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, VersionMixin


class Event(Base, TimestampMixin, VersionMixin):
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
    sessions: Mapped[list["Session"]] = relationship(back_populates="event")


class Session(Base, TimestampMixin, VersionMixin):
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
    summary: Mapped[str] = mapped_column(Text, nullable=False, server_default=text("''"))
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
    event: Mapped[Optional["Event"]] = relationship(back_populates="sessions")
    signups: Mapped[list["Signup"]] = relationship(back_populates="session")
    character_histories: Mapped[list["CharacterHistory"]] = relationship(back_populates="session")


class Character(Base, TimestampMixin, VersionMixin):
    __tablename__ = "characters"
    __table_args__ = (
        Index("ix_characters_user_id", "user_id"),
        Index("ix_characters_system", "system"),
        CheckConstraint("level >= 0", name="check_level_positive"),
        {"schema": "service"},
    )

    character_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    system: Mapped[str] = mapped_column(Text, nullable=False)
    level: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text("1"))
    name: Mapped[str] = mapped_column(Text, nullable=False)
    race: Mapped[str | None] = mapped_column(Text, nullable=True)
    class_: Mapped[str | None] = mapped_column("class", Text, nullable=True)
    subclass: Mapped[str | None] = mapped_column(Text, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    signups: Mapped[list["Signup"]] = relationship(back_populates="character")
    character_histories: Mapped[list["CharacterHistory"]] = relationship(back_populates="character")


class CharacterHistory(Base):
    __tablename__ = "character_history"
    __table_args__ = (
        PrimaryKeyConstraint("character_id", "session_id"),
        Index("ix_character_history_character_created", "character_id", "created_at"),
        Index("ix_character_history_session_id", "session_id"),
        {"schema": "service"},
    )

    character_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("service.characters.character_id"), nullable=False
    )
    session_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("service.sessions.session_id"), nullable=False
    )
    event_id: Mapped[UUID | None] = mapped_column(PG_UUID(as_uuid=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    # Relationships
    character: Mapped["Character"] = relationship(back_populates="character_histories")
    session: Mapped["Session"] = relationship(back_populates="character_histories")


class Signup(Base, TimestampMixin, VersionMixin):
    __tablename__ = "signups"
    __table_args__ = (
        PrimaryKeyConstraint("session_id", "user_id"),
        Index("ix_signups_session_seat", "session_id", "seat"),
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
    seat: Mapped[str] = mapped_column(Text, nullable=False)

    # Relationships
    session: Mapped["Session"] = relationship(back_populates="signups")
    character: Mapped["Character"] = relationship(back_populates="signups")
