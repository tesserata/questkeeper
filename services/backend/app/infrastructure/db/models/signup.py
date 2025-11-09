from uuid import UUID

from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Index,
    PrimaryKeyConstraint,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.models.base import Base, TimestampMixin, VersionMixin


class SignupORM(Base, TimestampMixin, VersionMixin):
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
