# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0
# Pydantic Version: 2.12.3
import typing
from datetime import datetime

from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .common_p2p import Page, PageRequest, RequestMeta, VersionHeader
from .enums_p2p import EventStatus, GameSystem
from .sessions_p2p import Session


class Event(BaseModel):
    """
    models
    """

    model_config = ConfigDict(validate_default=True)
    event_id: str = Field(default="")
    server_id: str = Field(default="")
    role_mentions: typing.List[str] = Field(default_factory=list)
    title: str = Field(default="")
    summary: str = Field(default="")
    system: GameSystem = Field(default=0)
    starts_at: datetime = Field(default_factory=datetime.now)
    ends_at: datetime = Field(default_factory=datetime.now)
    channel_id: str = Field(default="")
    message_id: str = Field(default="")  # filled by worker post-publish
    status: EventStatus = Field(default=0)
    sessions: typing.List[Session] = Field(default_factory=list)
    version: VersionHeader = Field(default_factory=VersionHeader)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class CreateEventRequest(BaseModel):
    """
    create
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    event: Event = Field(default_factory=Event)


class GetEventRequest(BaseModel):
    """
    read
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    event_id: str = Field(default="")


class DeleteEventRequest(BaseModel):
    """
    delete
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    event_id: str = Field(default="")


class UpdateBasics(BaseModel):
    model_config = ConfigDict(validate_default=True)
    title: str = Field(default="")
    summary: str = Field(default="")
    system: GameSystem = Field(default=0)


class UpdateSchedule(BaseModel):
    starts_at: datetime = Field(default_factory=datetime.now)
    ends_at: datetime = Field(default_factory=datetime.now)


class UpdateSessions(BaseModel):
    capacity_main: int = Field(default=0)  # must be >= main_active_count


class UpdateEventRequest(BaseModel):
    """
    update
    """

    _one_of_dict = {
        "UpdateEventRequest.patch": {"fields": {"basics", "capacity", "schedule"}}
    }
    one_of_validator = model_validator(mode="before")(check_one_of)
    meta: RequestMeta = Field(default_factory=RequestMeta)
    event_id: str = Field(default="")
    expected_version: int = Field(default=0)
    basics: UpdateBasics = Field(default_factory=UpdateBasics)
    schedule: UpdateSchedule = Field(default_factory=UpdateSchedule)
    capacity: UpdateSessions = Field(default_factory=UpdateSessions)


class PublishEventRequest(BaseModel):
    """
    publish
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    event_id: str = Field(default="")


class PublishEventResponse(BaseModel):
    event: Event = Field(default_factory=Event)
    outbox_id: str = Field(default="")


class CancelEventRequest(BaseModel):
    """
    cancel
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    event_id: str = Field(default="")


class SetMessageIdRequest(BaseModel):
    """
    set message, worker-only
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    event_id: str = Field(default="")
    message_id: str = Field(default="")
    expected_version: int = Field(default=0)  # optional safety


class ListEventsRequest(BaseModel):
    """
    get list
    """

    model_config = ConfigDict(validate_default=True)
    meta: RequestMeta = Field(default_factory=RequestMeta)
    guild_id: str = Field(default="")
    gm_user_id: int = Field(default=0)
    user_id: int = Field(default=0)
    system_id: str = Field(default="")
    event_id: str = Field(default="")
    status: EventStatus = Field(default=0)
    start: datetime = Field(default_factory=datetime.now)
    end: datetime = Field(default_factory=datetime.now)
    page: PageRequest = Field(default_factory=PageRequest)


class ListEventsResponse(BaseModel):
    items: typing.List[Event] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)


class EventResponse(BaseModel):
    event: Event = Field(default_factory=Event)
    version: VersionHeader = Field(default_factory=VersionHeader)
