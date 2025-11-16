from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass
class VersionHeader:
    version: int = 0
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
