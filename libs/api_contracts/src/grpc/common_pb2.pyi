import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestMeta(_message.Message):
    __slots__ = ("request_id", "idempotency_key", "tenant_server_id", "user_id", "app_roles", "if_none_match")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ROLES_FIELD_NUMBER: _ClassVar[int]
    IF_NONE_MATCH_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    idempotency_key: str
    tenant_server_id: str
    user_id: str
    app_roles: _containers.RepeatedScalarFieldContainer[str]
    if_none_match: str
    def __init__(self, request_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., tenant_server_id: _Optional[str] = ..., user_id: _Optional[str] = ..., app_roles: _Optional[_Iterable[str]] = ..., if_none_match: _Optional[str] = ...) -> None: ...

class PageRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class Page(_message.Message):
    __slots__ = ("next_page_token", "total_size")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    total_size: int
    def __init__(self, next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class VersionHeader(_message.Message):
    __slots__ = ("version", "weak_etag", "updated_at")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WEAK_ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    version: int
    weak_etag: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, version: _Optional[int] = ..., weak_etag: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
