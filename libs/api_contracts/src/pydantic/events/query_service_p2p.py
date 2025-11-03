# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing
from datetime import datetime

from google.protobuf.message import Message  # type: ignore

from pydantic import BaseModel, Field

from ..common_p2p import Page, PageRequest
from .models_p2p import EventSummary


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
