# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing
from datetime import datetime

from google.protobuf.message import Message  # type: ignore
from models_p2p import SessionSummary

from pydantic import BaseModel, Field

from ..common_p2p import VersionHeader


class EventInfo(BaseModel):
    """
    write input (client -> server)
    """

    server_id: int = Field(default=0)
    title: str = Field(default="")
    summary: str = Field(default="")
    system: str = Field(default="")
    location: str = Field(default="")
    additional_links: typing.List[str] = Field(default_factory=list)
    time_start: datetime = Field(default_factory=datetime.now)
    time_end: datetime = Field(default_factory=datetime.now)
    role_mentions: typing.List[str] = Field(default_factory=list)


class Event(BaseModel):
    """
    resource (server -> client)
    """

    event_id: str = Field(default="")
    info: EventInfo = Field(default_factory=EventInfo)
    channel_id: int = Field(default=0)
    message_id: int = Field(default=0)
    status: str = Field(default="")
    version: VersionHeader = Field(default_factory=VersionHeader)


class EventSummary(BaseModel):  #  manual field selection to optimize data sent
    """
    summary (UI-friendly projection)
    """

    title: str = Field(default="")
    game_system: str = Field(default="")
    status: str = Field(default="")
    time_start: datetime = Field(default_factory=datetime.now)
    time_end: datetime = Field(default_factory=datetime.now)
    server_id: int = Field(default=0)
    channel_id: int = Field(default=0)
    message_id: int = Field(default=0)
    event_id: str = Field(default="")
    version: VersionHeader = Field(default_factory=VersionHeader)


class EventView(BaseModel):
    """
    view (UI-friendly projection)
    """

    event: Event = Field(default_factory=Event)
    seats_taken: int = Field(default=0)
    sessions: typing.List[SessionSummary] = Field(default_factory=list)
