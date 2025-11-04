# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
from datetime import datetime

from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel, Field

from ..common_p2p import VersionHeader


class CharacterInfo(BaseModel):
    """
    write input (client -> server)
    """

    user_id: int = Field(default=0)
    game_system: str = Field(default="")
    name: str = Field(default="")
    subclass: str = Field(default="")
    level: int = Field(default=0)
    race: str = Field(default="")
    notes: str = Field(default="")


class Character(BaseModel):
    """
    resource (server -> client)
    """

    character_id: str = Field(default="")
    info: CharacterInfo = Field(default_factory=CharacterInfo)
    version: VersionHeader = Field(default_factory=VersionHeader)


class CharacterSummary(BaseModel):
    """
    summary (UI-friendly projection)
    """

    user_id: int = Field(default=0)
    character_id: str = Field(default="")
    name: str = Field(default="")
    snippet: str = Field(default="")
    version: VersionHeader = Field(default_factory=VersionHeader)


class PlayRecord(BaseModel):
    session_title: str = Field(default="")
    gm_user_id: int = Field(default=0)
    time: datetime = Field(default_factory=datetime.now)
    server_id: int = Field(default=0)
    channel_id: int = Field(default=0)
    message_id: int = Field(default=0)
    version: VersionHeader = Field(default_factory=VersionHeader)
