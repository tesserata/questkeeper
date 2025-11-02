import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
import common_pb2 as _common_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSignupRequest(_message.Message):
    __slots__ = ("meta", "signup")
    META_FIELD_NUMBER: _ClassVar[int]
    SIGNUP_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    signup: Signup
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., signup: _Optional[_Union[Signup, _Mapping]] = ...) -> None: ...

class GetSignupRequest(_message.Message):
    __slots__ = ("meta", "session_id", "signup_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNUP_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    signup_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ..., signup_id: _Optional[str] = ...) -> None: ...

class DeleteSignupRequest(_message.Message):
    __slots__ = ("meta", "session_id", "signup_id")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNUP_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    signup_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ..., signup_id: _Optional[str] = ...) -> None: ...

class UpdateSignupRequest(_message.Message):
    __slots__ = ("meta", "session_id", "signup_id", "expected_version", "character", "seat")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNUP_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    SEAT_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    signup_id: str
    expected_version: int
    character: UpdateCharacter
    seat: UpdateSeat
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ..., signup_id: _Optional[str] = ..., expected_version: _Optional[int] = ..., character: _Optional[_Union[UpdateCharacter, _Mapping]] = ..., seat: _Optional[_Union[UpdateSeat, _Mapping]] = ...) -> None: ...

class UpdateCharacter(_message.Message):
    __slots__ = ("character_id",)
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    def __init__(self, character_id: _Optional[str] = ...) -> None: ...

class UpdateSeat(_message.Message):
    __slots__ = ("seat",)
    SEAT_FIELD_NUMBER: _ClassVar[int]
    seat: _enums_pb2.Seat
    def __init__(self, seat: _Optional[_Union[_enums_pb2.Seat, str]] = ...) -> None: ...

class ListSignupsRequest(_message.Message):
    __slots__ = ("meta", "session_id", "seat", "page")
    META_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    session_id: str
    seat: _enums_pb2.Seat
    page: _common_pb2.PageRequest
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., session_id: _Optional[str] = ..., seat: _Optional[_Union[_enums_pb2.Seat, str]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListSignupsResponse(_message.Message):
    __slots__ = ("items", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Signup]
    page: _common_pb2.Page
    def __init__(self, items: _Optional[_Iterable[_Union[Signup, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...

class Signup(_message.Message):
    __slots__ = ("session_id", "user_id", "character_id", "seat", "created_at", "updated_at")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: int
    character_id: str
    seat: _enums_pb2.Seat
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[int] = ..., character_id: _Optional[str] = ..., seat: _Optional[_Union[_enums_pb2.Seat, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SignupResponse(_message.Message):
    __slots__ = ("signup", "version")
    SIGNUP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    signup: Signup
    version: _common_pb2.VersionHeader
    def __init__(self, signup: _Optional[_Union[Signup, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...
