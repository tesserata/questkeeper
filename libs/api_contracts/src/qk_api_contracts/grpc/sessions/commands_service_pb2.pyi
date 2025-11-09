import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from qk_api_contracts.grpc.sessions import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditBasicsRequest(_message.Message):
    __slots__ = ("session_id", "title", "summary", "system", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    title: str
    summary: str
    system: str
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditScheduleRequest(_message.Message):
    __slots__ = ("session_id", "time", "duration_minutes", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    time: _timestamp_pb2.Timestamp
    duration_minutes: int
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_minutes: _Optional[int] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditOrganizationRequest(_message.Message):
    __slots__ = ("vtt_link", "location", "additional_links", "expected_version")
    VTT_LINK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    vtt_link: str
    location: str
    additional_links: _containers.RepeatedScalarFieldContainer[str]
    expected_version: int
    def __init__(self, vtt_link: _Optional[str] = ..., location: _Optional[str] = ..., additional_links: _Optional[_Iterable[str]] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditCapacityRequest(_message.Message):
    __slots__ = ("session_id", "capacity", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    capacity: int
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., capacity: _Optional[int] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditGMRequest(_message.Message):
    __slots__ = ("session_id", "gm_user_id", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    GM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    gm_user_id: int
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., expected_version: _Optional[int] = ...) -> None: ...

class PublishSessionRequest(_message.Message):
    __slots__ = ("session_id", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class CancelSessionRequest(_message.Message):
    __slots__ = ("session_id", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class SwitchReserveRequest(_message.Message):
    __slots__ = ("session_id", "user_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SwitchMainRequest(_message.Message):
    __slots__ = ("session_id", "user_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SignOutRequest(_message.Message):
    __slots__ = ("session_id", "user_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SetCharacterRequest(_message.Message):
    __slots__ = ("session_id", "user_id", "character_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    character_id: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ..., character_id: _Optional[str] = ...) -> None: ...
