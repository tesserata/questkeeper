# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0 
# Pydantic Version: 2.12.3 
from ..common_p2p import Page
from ..common_p2p import PageRequest
from .models_p2p import SessionSummary
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class EditBasicsRequest(BaseModel):
    session_id: str = Field(default="")
    title: str = Field(default="")
    summary: str = Field(default="")
    system: str = Field(default="")
    expected_version: int = Field(default=0)

class EditScheduleRequest(BaseModel):
    session_id: str = Field(default="")
    time: datetime = Field(default_factory=datetime.now)
    duration_minutes: int = Field(default=0)
    expected_version: int = Field(default=0)

class EditOrganizationRequest(BaseModel):
    vtt_link: str = Field(default="")
    location: str = Field(default="")
    additional_links: typing.List[str] = Field(default_factory=list)
    expected_version: int = Field(default=0)

class EditCapacityRequest(BaseModel):
    session_id: str = Field(default="")
    capacity: int = Field(default=0)
    expected_version: int = Field(default=0)

class EditGMRequest(BaseModel):
    session_id: str = Field(default="")
    gm_user_id: int = Field(default=0)
    expected_version: int = Field(default=0)

class SessionOperationRequest(BaseModel):
    session_id: str = Field(default="")
    expected_version: int = Field(default=0)

class SignupOperationRequest(BaseModel):
    """
     --- signup commands ---
    """

    session_id: str = Field(default="")
    user_id: str = Field(default="")

class SetCharacterRequest(BaseModel):
    session_id: str = Field(default="")
    user_id: str = Field(default="")
    character_id: str = Field(default="")

class GetSessionRequest(BaseModel):
    session_id: str = Field(default="")

class ListSessionsRequest(BaseModel):
    server_id: str = Field(default="")
    gm_user_id: int = Field(default=0)
    user_id: int = Field(default=0)
    system: str = Field(default="")
    event_id: str = Field(default="")
    status: str = Field(default="")
    start: datetime = Field(default_factory=datetime.now)
    end: datetime = Field(default_factory=datetime.now)
    page: PageRequest = Field(default_factory=PageRequest)

class ListSessionsResponse(BaseModel):
    items: typing.List[SessionSummary] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)
