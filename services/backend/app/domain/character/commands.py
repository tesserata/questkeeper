from dataclasses import dataclass


@dataclass
class CreateCharacterCommand:
    user_id: int
    guild_id: int
    system: str
    name: str
    class_name: str | None
    subclass_name: str | None
    level: int
    race: str | None
    notes: str | None


@dataclass
class UpdateCharacterCommand:
    character_id: str
    user_id: int
    guild_id: int
    changes: dict[str, object]
    expected_version: int
