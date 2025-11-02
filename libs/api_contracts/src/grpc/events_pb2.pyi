import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import enums_pb2 as _enums_pb2
import sessions_pb2 as _sessions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEventRequest(_message.Message):
    __slots__ = ("meta", "event")
    META_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    event: Event
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class GetEventRequest(_message.Message):
    __slots__ = ("meta", "event_id")
    META_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    event_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., event_id: _Optional[str] = ...) -> None: ...

class DeleteEventRequest(_message.Message):
    __slots__ = ("meta", "event_id")
    META_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    event_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., event_id: _Optional[str] = ...) -> None: ...

class UpdateEventRequest(_message.Message):
    __slots__ = ("meta", "event_id", "expected_version", "basics", "schedule", "capacity")
    META_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    BASICS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    event_id: str
    expected_version: int
    basics: UpdateBasics
    schedule: UpdateSchedule
    capacity: UpdateSessions
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., event_id: _Optional[str] = ..., expected_version: _Optional[int] = ..., basics: _Optional[_Union[UpdateBasics, _Mapping]] = ..., schedule: _Optional[_Union[UpdateSchedule, _Mapping]] = ..., capacity: _Optional[_Union[UpdateSessions, _Mapping]] = ...) -> None: ...

class UpdateBasics(_message.Message):
    __slots__ = ("title", "summary", "system")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    title: str
    summary: str
    system: _enums_pb2.GameSystem
    def __init__(self, title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[_Union[_enums_pb2.GameSystem, str]] = ...) -> None: ...

class UpdateSchedule(_message.Message):
    __slots__ = ("starts_at", "ends_at")
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    def __init__(self, starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateSessions(_message.Message):
    __slots__ = ("capacity_main",)
    CAPACITY_MAIN_FIELD_NUMBER: _ClassVar[int]
    capacity_main: int
    def __init__(self, capacity_main: _Optional[int] = ...) -> None: ...

class PublishEventRequest(_message.Message):
    __slots__ = ("meta", "event_id")
    META_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    event_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., event_id: _Optional[str] = ...) -> None: ...

class PublishEventResponse(_message.Message):
    __slots__ = ("event", "outbox_id")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    OUTBOX_ID_FIELD_NUMBER: _ClassVar[int]
    event: Event
    outbox_id: str
    def __init__(self, event: _Optional[_Union[Event, _Mapping]] = ..., outbox_id: _Optional[str] = ...) -> None: ...

class CancelEventRequest(_message.Message):
    __slots__ = ("meta", "event_id")
    META_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    event_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., event_id: _Optional[str] = ...) -> None: ...

class SetMessageIdRequest(_message.Message):
    __slots__ = ("meta", "event_id", "message_id", "expected_version")
    META_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    event_id: str
    message_id: str
    expected_version: int
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., event_id: _Optional[str] = ..., message_id: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class ListEventsRequest(_message.Message):
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
    status: _enums_pb2.EventStatus
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    page: _common_pb2.PageRequest
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., guild_id: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., user_id: _Optional[int] = ..., system_id: _Optional[str] = ..., event_id: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2.EventStatus, str]] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListEventsResponse(_message.Message):
    __slots__ = ("items", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Event]
    page: _common_pb2.Page
    def __init__(self, items: _Optional[_Iterable[_Union[Event, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("event_id", "server_id", "role_mentions", "title", "summary", "system", "starts_at", "ends_at", "channel_id", "message_id", "status", "sessions", "version", "created_at", "updated_at")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    server_id: str
    role_mentions: _containers.RepeatedScalarFieldContainer[str]
    title: str
    summary: str
    system: _enums_pb2.GameSystem
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    channel_id: str
    message_id: str
    status: _enums_pb2.EventStatus
    sessions: _containers.RepeatedCompositeFieldContainer[_sessions_pb2.Session]
    version: _common_pb2.VersionHeader
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, event_id: _Optional[str] = ..., server_id: _Optional[str] = ..., role_mentions: _Optional[_Iterable[str]] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[_Union[_enums_pb2.GameSystem, str]] = ..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., channel_id: _Optional[str] = ..., message_id: _Optional[str] = ..., status: _Optional[_Union[_enums_pb2.EventStatus, str]] = ..., sessions: _Optional[_Iterable[_Union[_sessions_pb2.Session, _Mapping]]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EventResponse(_message.Message):
    __slots__ = ("event", "version")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    event: Event
    version: _common_pb2.VersionHeader
    def __init__(self, event: _Optional[_Union[Event, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...
