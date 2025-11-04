import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
from sessions import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventInfo(_message.Message):
    __slots__ = ("server_id", "title", "summary", "system", "location", "additional_links", "time_start", "time_end", "role_mentions")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
    TIME_START_FIELD_NUMBER: _ClassVar[int]
    TIME_END_FIELD_NUMBER: _ClassVar[int]
    ROLE_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    server_id: int
    title: str
    summary: str
    system: str
    location: str
    additional_links: _containers.RepeatedScalarFieldContainer[str]
    time_start: _timestamp_pb2.Timestamp
    time_end: _timestamp_pb2.Timestamp
    role_mentions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_id: _Optional[int] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[str] = ..., location: _Optional[str] = ..., additional_links: _Optional[_Iterable[str]] = ..., time_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., time_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., role_mentions: _Optional[_Iterable[str]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("event_id", "info", "channel_id", "message_id", "status", "version")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    info: EventInfo
    channel_id: int
    message_id: int
    status: str
    version: _common_pb2.VersionHeader
    def __init__(self, event_id: _Optional[str] = ..., info: _Optional[_Union[EventInfo, _Mapping]] = ..., channel_id: _Optional[int] = ..., message_id: _Optional[int] = ..., status: _Optional[str] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class EventSummary(_message.Message):
    __slots__ = ("title", "game_system", "status", "time_start", "time_end", "server_id", "channel_id", "message_id", "event_id", "version")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    GAME_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIME_START_FIELD_NUMBER: _ClassVar[int]
    TIME_END_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    title: str
    game_system: str
    status: str
    time_start: _timestamp_pb2.Timestamp
    time_end: _timestamp_pb2.Timestamp
    server_id: int
    channel_id: int
    message_id: int
    event_id: str
    version: _common_pb2.VersionHeader
    def __init__(self, title: _Optional[str] = ..., game_system: _Optional[str] = ..., status: _Optional[str] = ..., time_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., time_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., server_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., message_id: _Optional[int] = ..., event_id: _Optional[str] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class EventView(_message.Message):
    __slots__ = ("event", "seats_taken", "sessions")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SEATS_TAKEN_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    event: Event
    seats_taken: int
    sessions: _containers.RepeatedCompositeFieldContainer[_models_pb2.SessionSummary]
    def __init__(self, event: _Optional[_Union[Event, _Mapping]] = ..., seats_taken: _Optional[int] = ..., sessions: _Optional[_Iterable[_Union[_models_pb2.SessionSummary, _Mapping]]] = ...) -> None: ...
