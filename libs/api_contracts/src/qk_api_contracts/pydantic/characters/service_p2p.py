# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0 
# Pydantic Version: 2.12.3 
from ..common_p2p import Page
from ..common_p2p import PageRequest
from .models_p2p import Character
from .models_p2p import PlayRecord
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class EditNameRequest(BaseModel):
    character_id: str = Field(default="")
    name: str = Field(default="")
    expected_version: int = Field(default=0)

class EditSystemRequest(BaseModel):
    character_id: str = Field(default="")
    game_system: str = Field(default="")
    expected_version: int = Field(default=0)

class EditClassRequest(BaseModel):
    character_id: str = Field(default="")
    subclass: str = Field(default="")
    expected_version: int = Field(default=0)

class EditRaceRequest(BaseModel):
    character_id: str = Field(default="")
    race: str = Field(default="")
    expected_version: int = Field(default=0)

class EditLevelRequest(BaseModel):
    character_id: str = Field(default="")
    level: int = Field(default=0)
    expected_version: int = Field(default=0)

class EditNotesRequest(BaseModel):
    character_id: str = Field(default="")
    notes: str = Field(default="")
    expected_version: int = Field(default=0)

class DeleteCharacterRequest(BaseModel):
    character_id: str = Field(default="")
    expected_version: int = Field(default=0)

class CharacterIdRequest(BaseModel):
    character_id: str = Field(default="")

class ListCharactersRequest(BaseModel):
    user_id: int = Field(default=0)
    system: str = Field(default="")
    page: PageRequest = Field(default_factory=PageRequest)

class ListCharactersResponse(BaseModel):
    items: typing.List[Character] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)

class PlayHistoryResponse(BaseModel):
    records: typing.List[PlayRecord] = Field(default_factory=list)
    character_id: str = Field(default="")
    page: Page = Field(default_factory=Page)
