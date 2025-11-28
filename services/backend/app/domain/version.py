from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass
class VersionHeader:
    version: int = 1
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def touch(self) -> None:
        self.updated_at = datetime.now(UTC)

    def bump(self) -> None:
        self.version += 1
        self.touch()
