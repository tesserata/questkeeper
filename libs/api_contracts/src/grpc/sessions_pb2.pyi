import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import enums_pb2 as _enums_pb2
import signups_pb2 as _signups_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ("meta", "session")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session: Session
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("meta", "session_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ("meta", "session_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ("meta", "session_id", "expected_version", "basics", "event", "organization", "schedule", "capacity")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    BASICS_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    expected_version: int
    basics: UpdateBasics
    event: UpdateEvent
    organization: UpdateOrganization
    schedule: UpdateSchedule
    capacity: UpdateCapacity
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ..., expected_version: _Optional[int] = ..., basics: _Optional[_Union[UpdateBasics, _Mapping]] = ..., event: _Optional[_Union[UpdateEvent, _Mapping]] = ..., organization: _Optional[_Union[UpdateOrganization, _Mapping]] = ..., schedule: _Optional[_Union[UpdateSchedule, _Mapping]] = ..., capacity: _Optional[_Union[UpdateCapacity, _Mapping]] = ...) -> None: ...

class UpdateBasics(_message.Message):
    __slots__ = ("title", "summary", "system")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    title: str
    summary: str
    system: _enums_pb2.GameSystem
    def __init__(self, title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[_Union[_enums_pb2.GameSystem, str]] = ...) -> None: ...

class UpdateEvent(_message.Message):
    __slots__ = ("event_id",)
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    def __init__(self, event_id: _Optional[str] = ...) -> None: ...

class UpdateOrganization(_message.Message):
    __slots__ = ("vtt_link", "location", "additional_links")
    VTT_LINK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
    vtt_link: str
    location: str
    additional_links: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vtt_link: _Optional[str] = ..., location: _Optional[str] = ..., additional_links: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateSchedule(_message.Message):
    __slots__ = ("starts_at", "duration_minutes", "timezone")
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    starts_at: _timestamp_pb2.Timestamp
    duration_minutes: int
    timezone: str
    def __init__(self, starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_minutes: _Optional[int] = ..., timezone: _Optional[str] = ...) -> None: ...

class UpdateCapacity(_message.Message):
    __slots__ = ("capacity_main",)
    CAPACITY_MAIN_FIELD_NUMBER: _ClassVar[int]
    capacity_main: int
    def __init__(self, capacity_main: _Optional[int] = ...) -> None: ...

class PublishSessionRequest(_message.Message):
    __slots__ = ("meta", "session_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class PublishSessionResponse(_message.Message):
    __slots__ = ("session", "outbox_id")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    OUTBOX_ID_FIELD_NUMBER: _ClassVar[int]
    session: Session
    outbox_id: str
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., outbox_id: _Optional[str] = ...) -> None: ...

class CancelSessionRequest(_message.Message):
    __slots__ = ("meta", "session_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class SetMessageIdRequest(_message.Message):
    __slots__ = ("meta", "session_id", "message_id", "expected_version")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    message_id: str
    expected_version: int
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ..., message_id: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ("meta", "guild_id", "gm_user_id", "user_id", "system_id", "event_id", "status", "start", "end", "page")
    META_FIELD_NUMBER: _ClassVar[int]
    GUILD_ID_FIELD_NUMBER: _ClassVar[int]
    GM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    guild_id: str
    gm_user_id: int
    user_id: int
    system_id: str
    event_id: str
    status: _enums_pb2.SessionStatus
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    page: _common_pb2.PageRequest
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., guild_id: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., user_id: _Optional[int] = ..., system_id: _Optional[str] = ..., event_id: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2.SessionStatus, str]] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("items", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Session]
    page: _common_pb2.Page
    def __init__(self, items: _Optional[_Iterable[_Union[Session, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("session_id", "server_id", "event_id", "gm_user_id", "role_mentions", "title", "summary", "system", "vtt_link", "location", "additional_links", "starts_at", "duration_minutes", "timezone", "capacity", "channel_id", "message_id", "status", "main_signups", "reserve_signups", "version", "created_at", "updated_at")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    GM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    VTT_LINK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAIN_SIGNUPS_FIELD_NUMBER: _ClassVar[int]
    RESERVE_SIGNUPS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    server_id: str
    event_id: str
    gm_user_id: int
    role_mentions: _containers.RepeatedScalarFieldContainer[str]
    title: str
    summary: str
    system: _enums_pb2.GameSystem
    vtt_link: str
    location: str
    additional_links: _containers.RepeatedScalarFieldContainer[str]
    starts_at: _timestamp_pb2.Timestamp
    duration_minutes: int
    timezone: str
    capacity: int
    channel_id: str
    message_id: str
    status: _enums_pb2.SessionStatus
    main_signups: _containers.RepeatedCompositeFieldContainer[_signups_pb2.Signup]
    reserve_signups: _containers.RepeatedCompositeFieldContainer[_signups_pb2.Signup]
    version: _common_pb2.VersionHeader
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, session_id: _Optional[str] = ..., server_id: _Optional[str] = ..., event_id: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., role_mentions: _Optional[_Iterable[str]] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[_Union[_enums_pb2.GameSystem, str]] = ..., vtt_link: _Optional[str] = ..., location: _Optional[str] = ..., additional_links: _Optional[_Iterable[str]] = ..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_minutes: _Optional[int] = ..., timezone: _Optional[str] = ..., capacity: _Optional[int] = ..., channel_id: _Optional[str] = ..., message_id: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2.SessionStatus, str]] = ..., main_signups: _Optional[_Iterable[_Union[_signups_pb2.Signup, _Mapping]]] = ..., reserve_signups: _Optional[_Iterable[_Union[_signups_pb2.Signup, _Mapping]]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SessionResponse(_message.Message):
    __slots__ = ("session", "version")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    version: _common_pb2.VersionHeader
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...
