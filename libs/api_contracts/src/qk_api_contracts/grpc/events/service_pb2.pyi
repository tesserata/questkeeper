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

class EditBasicsRequest(_message.Message):
    __slots__ = ("event_id", "title", "summary", "system", "expected_version")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    title: str
    summary: str
    system: str
    expected_version: int
    def __init__(self, event_id: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., system: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditScheduleRequest(_message.Message):
    __slots__ = ("session_id", "time_start", "time_end", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_START_FIELD_NUMBER: _ClassVar[int]
    TIME_END_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    time_start: _timestamp_pb2.Timestamp
    time_end: _timestamp_pb2.Timestamp
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., time_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., time_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditOrganizationRequest(_message.Message):
    __slots__ = ("location", "additional_links", "expected_version")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    location: str
    additional_links: _containers.RepeatedScalarFieldContainer[str]
    expected_version: int
    def __init__(self, location: _Optional[str] = ..., additional_links: _Optional[_Iterable[str]] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EventOperationRequest(_message.Message):
    __slots__ = ("event_id", "expected_version")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    expected_version: int
    def __init__(self, event_id: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

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
