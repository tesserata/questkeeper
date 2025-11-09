import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qk_api_contracts.grpc import common_pb2 as _common_pb2
from qk_api_contracts.grpc.events import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEventRequest(_message.Message):
    __slots__ = ("event_id",)
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    def __init__(self, event_id: _Optional[str] = ...) -> None: ...

class ListEventsRequest(_message.Message):
    __slots__ = ("server_id", "system", "status", "start", "end", "page")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    system: str
    status: str
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    page: _common_pb2.PageRequest
    def __init__(self, server_id: _Optional[str] = ..., system: _Optional[str] = ..., status: _Optional[str] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListEventsResponse(_message.Message):
    __slots__ = ("items", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_models_pb2.EventSummary]
    page: _common_pb2.Page
    def __init__(self, items: _Optional[_Iterable[_Union[_models_pb2.EventSummary, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...
