# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0 
# Pydantic Version: 2.12.3 
from ..common_p2p import Page
from ..common_p2p import PageRequest
from .models_p2p import CharacterSummary
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class GetCharacterRequest(BaseModel):
    event_id: str = Field(default="")

class ListCharactersRequest(BaseModel):
    user_id: int = Field(default=0)
    system: str = Field(default="")
    page: PageRequest = Field(default_factory=PageRequest)

class ListCharactersResponse(BaseModel):
    items: typing.List[CharacterSummary] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)
