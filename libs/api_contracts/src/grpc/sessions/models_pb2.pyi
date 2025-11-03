import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
from characters import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionInfo(_message.Message):
    __slots__ = ("server_id", "event_id", "title", "summary", "system", "gm_user_id", "vtt_link", "location", "additional_links", "time", "duration_minutes", "capacity", "role_mentions")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    GM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    VTT_LINK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ROLE_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    server_id: int
    event_id: str
    title: str
    summary: str
    system: str
    gm_user_id: int
    vtt_link: str
    location: str
    additional_links: _containers.RepeatedScalarFieldContainer[str]
    time: _timestamp_pb2.Timestamp
    duration_minutes: int
    capacity: int
    role_mentions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_id: _Optional[int] = ..., event_id: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., vtt_link: _Optional[str] = ..., location: _Optional[str] = ..., additional_links: _Optional[_Iterable[str]] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_minutes: _Optional[int] = ..., capacity: _Optional[int] = ..., role_mentions: _Optional[_Iterable[str]] = ...) -> None: ...

class SignupInfo(_message.Message):
    __slots__ = ("session_id", "user_id", "character_id", "seat")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: int
    character_id: str
    seat: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[int] = ..., character_id: _Optional[str] = ..., seat: _Optional[str] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("session_id", "info", "channel_id", "message_id", "status", "version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    info: SessionInfo
    channel_id: int
    message_id: int
    status: str
    version: _common_pb2.VersionHeader
    def __init__(self, session_id: _Optional[str] = ..., info: _Optional[_Union[SessionInfo, _Mapping]] = ..., channel_id: _Optional[int] = ..., message_id: _Optional[int] = ..., status: _Optional[str] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class Signup(_message.Message):
    __slots__ = ("info", "version")
    INFO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    info: SignupInfo
    version: _common_pb2.VersionHeader
    def __init__(self, info: _Optional[_Union[SignupInfo, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class SessionSummary(_message.Message):
    __slots__ = ("title", "game_system", "gm_user_id", "status", "time", "capacity", "seats_taken", "server_id", "channel_id", "message_id", "session_id", "version")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    GAME_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    GM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    SEATS_TAKEN_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    title: str
    game_system: str
    gm_user_id: int
    status: str
    time: _timestamp_pb2.Timestamp
    capacity: int
    seats_taken: int
    server_id: int
    channel_id: int
    message_id: int
    session_id: str
    version: _common_pb2.VersionHeader
    def __init__(self, title: _Optional[str] = ..., game_system: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., status: _Optional[str] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., capacity: _Optional[int] = ..., seats_taken: _Optional[int] = ..., server_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., message_id: _Optional[int] = ..., session_id: _Optional[str] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class SessionView(_message.Message):
    __slots__ = ("session", "seats_taken", "main_signups", "reserve_signups")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SEATS_TAKEN_FIELD_NUMBER: _ClassVar[int]
    MAIN_SIGNUPS_FIELD_NUMBER: _ClassVar[int]
    RESERVE_SIGNUPS_FIELD_NUMBER: _ClassVar[int]
    session: Session
    seats_taken: int
    main_signups: _containers.RepeatedCompositeFieldContainer[SignupView]
    reserve_signups: _containers.RepeatedCompositeFieldContainer[SignupView]
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., seats_taken: _Optional[int] = ..., main_signups: _Optional[_Iterable[_Union[SignupView, _Mapping]]] = ..., reserve_signups: _Optional[_Iterable[_Union[SignupView, _Mapping]]] = ...) -> None: ...

class SignupView(_message.Message):
    __slots__ = ("user_id", "character")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    character: _models_pb2.CharacterSummary
    def __init__(self, user_id: _Optional[str] = ..., character: _Optional[_Union[_models_pb2.CharacterSummary, _Mapping]] = ...) -> None: ...
