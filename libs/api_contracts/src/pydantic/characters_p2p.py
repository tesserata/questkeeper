# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing
from datetime import datetime

from google.protobuf.message import Message  # type: ignore

from pydantic import BaseModel, ConfigDict, Field

from .common_p2p import Page, PageRequest, RequestMeta, VersionHeader
from .enums_p2p import GameSystem


class Character(BaseModel):
    """
    models
    """

    model_config = ConfigDict(validate_default=True)
    character_id: str = Field(default="")
    user_id: int = Field(default=0)
    system: GameSystem = Field(default=0)
    level: int = Field(default=0)
    name: str = Field(default="")
    race: str = Field(default="")
    subclass: str = Field(default="")
    notes: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class CreateCharacterRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    character: Character = Field(default_factory=Character)


class GetCharacterRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    character_id: str = Field(default="")


class DeleteCharacterRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    character_id: str = Field(default="")


class UpdateCharacter(BaseModel):
    name: typing.Optional[str] = Field(default="")
    race: typing.Optional[str] = Field(default="")
    level: typing.Optional[int] = Field(default=0)
    notes: typing.Optional[str] = Field(default="")


class UpdateCharacterRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    character_id: str = Field(default="")
    update: UpdateCharacter = Field(default_factory=UpdateCharacter)


class GetCharacterHistoryRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    character_id: str = Field(default="")


class CharacterHistoryEntry(BaseModel):
    session_id: str = Field(default="")
    event_id: str = Field(default="")


class GetCharacterHistoryResponse(BaseModel):
    history: CharacterHistoryEntry = Field(default_factory=CharacterHistoryEntry)


class ListCharactersRequest(BaseModel):
    meta: RequestMeta = Field(default_factory=RequestMeta)
    page: PageRequest = Field(default_factory=PageRequest)
    user_id: int = Field(default=0)


class ListCharactersResponse(BaseModel):
    characters: typing.List[Character] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)


class CharacterResponse(BaseModel):
    character: Character = Field(default_factory=Character)
    version: VersionHeader = Field(default_factory=VersionHeader)
