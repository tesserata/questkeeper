from uuid import UUID

from pydantic import Field

from qk_api_contracts.enums import GameSystem
from qk_api_contracts.schema._base import LimitedStr, NonEmptyLimitedStr, Page, QkSchema


class Character(QkSchema):
    name: NonEmptyLimitedStr
    system: GameSystem
    level: int = Field(ge=1, le=20)
    class_name: LimitedStr | None = None
    subclass_name: LimitedStr | None = None
    race: LimitedStr | None = None
    notes: str | None = None


class CharacterRead(Character):
    """GET; Server → client representation"""

    character_id: UUID
    user_id: int


class CharacterList(QkSchema):
    """GET; Server -> client representation with pagination"""

    items: list[CharacterRead]
    next_page_token: str | None = None


class CharacterListQuery(QkSchema):
    # filters
    user_ids: list[int] | None = None
    system: GameSystem | None = None
    level_min: int | None
    level_max: int | None

    pagination: Page = Field(default_factory=Page)
