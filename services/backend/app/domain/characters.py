from dataclasses import dataclass, field
from datetime import datetime, timezone

def utcnow(): return datetime.now(timezone.utc)


# class InvalidEdit(DomainError):


@dataclass
class Character:
    character_id: str
    owner_user_id: str
    server_id: str
    system: str
    name: str
    level: int
    tags: list[str] = field(default_factory=list)

    version: int = 0
    created_at: datetime = field(default_factory=utcnow)
    updated_at: datetime = field(default_factory=utcnow)

    # system-flavored basics (keep small; projection can expand)
    ancestry_or_race: str = ""
    class_name: str = ""
    key_attribute: str = ""    # e.g. "STR" (optional per system)

    def _bump(self): self.version += 1; self.updated_at = utcnow()

    def edit_basics(self, *, name: str | None = None, level: int | None = None,
                    tags: list[str] | None = None,
                    ancestry_or_race: str | None = None, class_name: str | None = None,
                    key_attribute: str | None = None):
        if name is not None: self.name = name
        if level is not None:
            if level < 1: pass
                # raise InvalidEdit("level must be >= 1")
            self.level = level
        if tags is not None: self.tags = list(tags)[:10]  # cap length
        if ancestry_or_race is not None: self.ancestry_or_race = ancestry_or_race
        if class_name is not None: self.class_name = class_name
        if key_attribute is not None: self.key_attribute = key_attribute
        self._bump()

    def assign_system(self, *, system: str):
        self.system = system
        self._bump()
