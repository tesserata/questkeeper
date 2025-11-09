import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qk_api_contracts.grpc import common_pb2 as _common_pb2
from qk_api_contracts.grpc.sessions import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ("server_id", "gm_user_id", "user_id", "system", "event_id", "status", "start", "end", "page")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    GM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    gm_user_id: int
    user_id: int
    system: str
    event_id: str
    status: str
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    page: _common_pb2.PageRequest
    def __init__(self, server_id: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., user_id: _Optional[int] = ..., system: _Optional[str] = ..., event_id: _Optional[str] = ..., status: _Optional[str] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("items", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_models_pb2.SessionSummary]
    page: _common_pb2.Page
    def __init__(self, items: _Optional[_Iterable[_Union[_models_pb2.SessionSummary, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...
