from dataclasses import dataclass, field

from qk_api_contracts.enums import AppRole, GameSystem

from app.domain.version import VersionHeader


@dataclass
class ServerSettings:
    server_id: int
    default_announcement_channel_id: int
    default_system: GameSystem

    dm_notifications_enabled: bool = False
    mentionable_roles: list[int] = field(default_factory=list)
    role_mappings: dict[int, AppRole] = field(default_factory=dict)

    version_header: VersionHeader = field(default_factory=VersionHeader)
