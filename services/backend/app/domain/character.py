from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from qk_api_contracts.enums import GameSystem

from app.domain.common import VersionHeader

# class InvalidEdit(DomainError):


@dataclass
class PlayRecord:
    session_title: str
    gm_user_id: int
    time: datetime

    server_id: int
    channel_id: int
    message_id: int


@dataclass
class Character:
    user_id: int
    system: GameSystem

    name: str
    level: int = field(default=1)
    notes: str = field(default="")

    character_id: UUID = field(default_factory=uuid4)

    race: str = ""
    class_name: str = ""
    subclass_name: str = ""

    version_header: VersionHeader = field(default_factory=VersionHeader)

    def _bump(self):
        self.version += 1
        self.updated_at = datetime.now(UTC)
