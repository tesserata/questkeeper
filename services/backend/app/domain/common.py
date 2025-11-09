from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass
class VersionHeader:
    version: int = 0
    weak_etag: str = ""
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
