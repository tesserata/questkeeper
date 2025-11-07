from qk_api_contracts.enums import GameSystem
from sqlalchemy import (
    BigInteger,
    Boolean,
    ForeignKey,
    Index,
    Integer,
    PrimaryKeyConstraint,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, VersionMixin


class ServerSettings(Base, TimestampMixin, VersionMixin):
    __tablename__ = "server_settings"
    __table_args__ = (
        Index("ix_server_settings_default_system", "default_system"),
        {"schema": "service"},
    )

    server_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    default_announcement_channel_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    default_system: Mapped[str] = mapped_column(
        Text, nullable=False, server_default=text(f"'{GameSystem.PATHFINDER_2E}'")
    )
    dm_notifications_enabled: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )
    mentionable_roles: Mapped[list[str]] = mapped_column(
        ARRAY(Text), nullable=False, server_default=text("'{}'")
    )

    # Relationships
    role_mappings: Mapped[list["ServerRoleMapping"]] = relationship(back_populates="server")


class ServerRoleMapping(Base, TimestampMixin):
    __tablename__ = "server_role_mapping"
    __table_args__ = (
        PrimaryKeyConstraint("server_id", "discord_role_id"),
        Index("ix_server_role_mapping_server_id", "server_id"),
        {"schema": "service"},
    )

    server_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("service.server_settings.server_id"), nullable=False
    )
    discord_role_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    app_role: Mapped[str] = mapped_column(Text, nullable=False)

    # Relationships
    server: Mapped["ServerSettings"] = relationship(back_populates="role_mappings")
