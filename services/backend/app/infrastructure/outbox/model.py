from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum, auto
from typing import Any
from uuid import UUID, uuid4


class AggregateType(StrEnum):
    session = auto()
    event = auto()


class EventType(StrEnum):
    session_upsert = "discord.session.upsert"
    session_delete = "discord.session.delete"
    dm_signup_created = "discord.dm.signup_created"
    dm_signup_cancelled = "discord.dm.signup_cancelled"
    dm_session_cancelled = "discord.dm.session_cancelled"
    dm_session_updated = "discord.dm.session_updated"
    dm_session_reminder = "discord.dm.session_reminder"
    dm_gm_session_reminder = "discord.dm.gm_reminder"


class EventStatus(StrEnum):
    enqueued = auto()
    pending = auto()
    processed = auto()
    failed = auto()


@dataclass
class OutboxMessage:
    aggregate_type: AggregateType
    aggregate_id: UUID

    event_type: EventType
    payload: dict[str, Any]
    headers: dict[str, Any]


    id: UUID = field(default_factory=uuid4)
    status: EventStatus = field(default=EventStatus.enqueued)
    attempts: int = field(default=0)

    available_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    processed_at: datetime | None = field(default=None)
    last_error: str | None = field(default=None)
