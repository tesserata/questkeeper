# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0 
# Pydantic Version: 2.12.3 
from ..common_p2p import Page
from ..common_p2p import PageRequest
from .models_p2p import EventSummary
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class EditBasicsRequest(BaseModel):
    event_id: str = Field(default="")
    title: str = Field(default="")
    summary: str = Field(default="")
    system: str = Field(default="")
    expected_version: int = Field(default=0)

class EditScheduleRequest(BaseModel):
    session_id: str = Field(default="")
    time_start: datetime = Field(default_factory=datetime.now)
    time_end: datetime = Field(default_factory=datetime.now)
    expected_version: int = Field(default=0)

class EditOrganizationRequest(BaseModel):
    location: str = Field(default="")
    additional_links: typing.List[str] = Field(default_factory=list)
    expected_version: int = Field(default=0)

class EventOperationRequest(BaseModel):
    event_id: str = Field(default="")
    expected_version: int = Field(default=0)

class GetEventRequest(BaseModel):
    event_id: str = Field(default="")

class ListEventsRequest(BaseModel):
    server_id: str = Field(default="")
    system: str = Field(default="")
    status: str = Field(default="")
    start: datetime = Field(default_factory=datetime.now)
    end: datetime = Field(default_factory=datetime.now)
    page: PageRequest = Field(default_factory=PageRequest)

class ListEventsResponse(BaseModel):
    items: typing.List[EventSummary] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)
