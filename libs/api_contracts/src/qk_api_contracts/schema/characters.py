from uuid import UUID

from pydantic import Field

from qk_api_contracts.enums import GameSystem
from qk_api_contracts.schema._base import NonEmptyStr, QkSchema


class CharacterBase(QkSchema):
    system: GameSystem
    name: NonEmptyStr
    class_name: NonEmptyStr | None = None
    subclass_name: NonEmptyStr | None = None
    level: int = Field(ge=1, le=20)
    race: NonEmptyStr | None = None
    notes: str | None = None


class CharacterCreate(CharacterBase):
    """POST; Client → server representation"""

    pass


class CharacterUpdate(CharacterBase):
    """PATCH; everything optional"""

    pass


class CharacterRead(CharacterBase):
    """GET; Server → client representation"""

    character_id: UUID
    user_id: int


class CharacterList(QkSchema):
    """GET; Server -> client representation with pagination"""

    items: list[CharacterRead]
    next_page_token: str | None = None
    total_size: int | None = None
