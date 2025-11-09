import json

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.outbox import OutboxORM


class OutboxWriter:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def enqueue(self, *, topic: str, key: str, payload: dict) -> None:
        self.db.add(
            OutboxORM(topic=topic, key=key, payload=json.dumps(payload, separators=(",", ":")))
        )
