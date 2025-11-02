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
from .enums_p2p import GameSystem, SessionStatus
from .signups_p2p import Signup


class Session(BaseModel):
    """
    models
    """

    model_config = ConfigDict(validate_default=True)
    session_id: str = Field(default="")
    server_id: str = Field(default="")
    event_id: str = Field(default="")
    gm_user_id: int = Field(default=0)
    role_mentions: typing.List[str] = Field(default_factory=list)
    title: str = Field(default="")
    summary: str = Field(default="")
    system: GameSystem = Field(default=0)
    vtt_link: str = Field(default="")
    location: str = Field(default="")
    additional_links: typing.List[str] = Field(default_factory=list)
    starts_at: datetime = Field(default_factory=datetime.now)
    duration_minutes: int = Field(default=0)
    timezone: str = Field(default="")
    capacity: int = Field(default=0)
    channel_id: str = Field(default="")
    message_id: str = Field(default="")  # filled by worker post-publish
    status: SessionStatus = Field(default=0)
    main_signups: typing.List[Signup] = Field(default_factory=list)
    reserve_signups: typing.List[Signup] = Field(default_factory=list)
    version: VersionHeader = Field(default_factory=VersionHeader)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class CreateSessionRequest(BaseModel):
    """
    create
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    session: Session = Field(default_factory=Session)


class GetSessionRequest(BaseModel):
    """
    read
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")


class DeleteSessionRequest(BaseModel):
    """
    delete
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")


class UpdateBasics(BaseModel):
    model_config = ConfigDict(validate_default=True)
    title: str = Field(default="")
    summary: str = Field(default="")
    system: GameSystem = Field(default=0)


class UpdateEvent(BaseModel):
    event_id: str = Field(default="")


class UpdateOrganization(BaseModel):
    vtt_link: str = Field(default="")
    location: str = Field(default="")
    additional_links: typing.List[str] = Field(default_factory=list)


class UpdateSchedule(BaseModel):
    starts_at: datetime = Field(default_factory=datetime.now)
    duration_minutes: int = Field(default=0)
    timezone: str = Field(default="")


class UpdateCapacity(BaseModel):
    capacity_main: int = Field(default=0)  # must be >= main_active_count


class UpdateSessionRequest(BaseModel):
    """
    update
    """

    _one_of_dict = {
        "UpdateSessionRequest.patch": {
            "fields": {"basics", "capacity", "event", "organization", "schedule"}
        }
    }
    one_of_validator = model_validator(mode="before")(check_one_of)
    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")
    expected_version: int = Field(default=0)
    basics: UpdateBasics = Field(default_factory=UpdateBasics)
    event: UpdateEvent = Field(default_factory=UpdateEvent)
    organization: UpdateOrganization = Field(default_factory=UpdateOrganization)
    schedule: UpdateSchedule = Field(default_factory=UpdateSchedule)
    capacity: UpdateCapacity = Field(default_factory=UpdateCapacity)


class PublishSessionRequest(BaseModel):
    """
    publish
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")


class PublishSessionResponse(BaseModel):
    session: Session = Field(default_factory=Session)
    outbox_id: str = Field(default="")


class CancelSessionRequest(BaseModel):
    """
    cancel
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")


class SetMessageIdRequest(BaseModel):
    """
    set message, worker-only
    """

    meta: RequestMeta = Field(default_factory=RequestMeta)
    session_id: str = Field(default="")
    message_id: str = Field(default="")
    expected_version: int = Field(default=0)  # optional safety


class ListSessionsRequest(BaseModel):
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
    status: SessionStatus = Field(default=0)
    start: datetime = Field(default_factory=datetime.now)
    end: datetime = Field(default_factory=datetime.now)
    page: PageRequest = Field(default_factory=PageRequest)


class ListSessionsResponse(BaseModel):
    items: typing.List[Session] = Field(default_factory=list)
    page: Page = Field(default_factory=Page)


class SessionResponse(BaseModel):
    session: Session = Field(default_factory=Session)
    version: VersionHeader = Field(default_factory=VersionHeader)
