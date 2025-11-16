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
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.models.base import Base, VersionMixin


class CharacterORM(Base, VersionMixin):
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
    # signups: Mapped[list["SignupORM"]] = relationship(back_populates="character")
    # character_histories: Mapped[list["CharacterHistoryORM"]] = relationship(
    #     back_populates="character"
    # )


class CharacterHistoryORM(Base):
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
    # character: Mapped["CharacterORM"] = relationship(back_populates="character_histories")
    # session: Mapped["SessionORM"] = relationship(back_populates="character_histories")
