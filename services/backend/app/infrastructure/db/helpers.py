from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.version import VersionHeader
from app.infrastructure.db.models.base import VersionMixin


@dataclass(frozen=True)
class Cursor:
    created_at: datetime
    last_id: UUID

    def to_tuple(self) -> tuple[datetime, UUID]:
        return self.created_at, self.last_id


def get_version_header(row: VersionMixin) -> VersionHeader:
    return VersionHeader(version=row.version, created_at=row.created_at, updated_at=row.updated_at)
