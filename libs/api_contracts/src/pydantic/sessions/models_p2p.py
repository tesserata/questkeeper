# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing
from datetime import datetime

from google.protobuf.message import Message  # type: ignore
from models_p2p import CharacterSummary

from pydantic import BaseModel, Field

from ..common_p2p import VersionHeader


class SessionInfo(BaseModel):
    """
    write input (client -> server)
    """

    server_id: int = Field(default=0)
    event_id: str = Field(default="")
    title: str = Field(default="")
    summary: str = Field(default="")
    system: str = Field(default="")
    gm_user_id: int = Field(default=0)
    vtt_link: str = Field(default="")
    location: str = Field(default="")
    additional_links: typing.List[str] = Field(default_factory=list)
    time: datetime = Field(default_factory=datetime.now)
    duration_minutes: int = Field(default=0)
    capacity: int = Field(default=0)
    role_mentions: typing.List[str] = Field(default_factory=list)


class SignupInfo(BaseModel):
    session_id: str = Field(default="")
    user_id: int = Field(default=0)
    character_id: str = Field(default="")
    seat: str = Field(default="")


class Session(BaseModel):
    """
    resource (server -> client)
    """

    session_id: str = Field(default="")
    info: SessionInfo = Field(default_factory=SessionInfo)
    channel_id: int = Field(default=0)
    message_id: int = Field(default=0)
    status: str = Field(default="")
    version: VersionHeader = Field(default_factory=VersionHeader)


class Signup(BaseModel):
    info: SignupInfo = Field(default_factory=SignupInfo)
    version: VersionHeader = Field(default_factory=VersionHeader)


class SessionSummary(BaseModel):  #  manual field selection to optimize data sent
    """
    summary (UI-friendly projection)
    """

    title: str = Field(default="")
    game_system: str = Field(default="")
    gm_user_id: int = Field(default=0)
    status: str = Field(default="")
    time: datetime = Field(default_factory=datetime.now)
    capacity: int = Field(default=0)
    seats_taken: int = Field(default=0)
    server_id: int = Field(default=0)
    channel_id: int = Field(default=0)
    message_id: int = Field(default=0)
    session_id: str = Field(default="")
    version: VersionHeader = Field(default_factory=VersionHeader)


class SignupView(BaseModel):
    user_id: str = Field(default="")
    character: CharacterSummary = Field(default_factory=CharacterSummary)


class SessionView(BaseModel):
    """
    view (UI-friendly projection)
    """

    session: Session = Field(default_factory=Session)
    seats_taken: int = Field(default=0)
    main_signups: typing.List[SignupView] = Field(default_factory=list)
    reserve_signups: typing.List[SignupView] = Field(default_factory=list)
