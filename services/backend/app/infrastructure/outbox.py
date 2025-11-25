import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum, auto
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.outbox import OutboxORM


class AggregateType(StrEnum):
    SESSION = auto()
    EVENT = auto()


class EventType(StrEnum):
    SESSION_UPSERT = "DISCORD.SESSION.UPSERT"
    SESSION_DELETE = "discord.session.delete"
    DM_SIGNUP_CREATED = "discord.dm.signup_created"
    DM_SIGNUP_CANCELLED = "discord.dm.signup_cancelled"
    DM_SESSION_CANCELLED = "discord.dm.session_cancelled"
    DM_SESSION_UPDATED = "discord.dm.session_updated"
    DM_SESSION_REMINDER = "discord.dm.session_reminder"
    DM_GM_SESSION_REMINDER = "discord.dm.gm_reminder"


class EventStatus(StrEnum):
    ENQUEUED = auto()
    PENDING = auto()
    PROCESSED = auto()
    FAILED = auto()


@dataclass
class OutboxMessage:
    aggregate_type: AggregateType
    aggregate_id: UUID

    event_type: EventType
    payload: dict[str, Any]
    headers: dict[str, Any]

    id: UUID = field(default_factory=uuid4)
    status: EventStatus = field(default=EventStatus.ENQUEUED)
    attempts: int = field(default=0)

    available_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    processed_at: datetime | None = field(default=None)
    last_error: str | None = field(default=None)


class OutboxWriter:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def enqueue(self, *, topic: str, key: str, payload: dict) -> None:
        self.db.add(
            OutboxORM(topic=topic, key=key, payload=json.dumps(payload, separators=(",", ":")))
        )
