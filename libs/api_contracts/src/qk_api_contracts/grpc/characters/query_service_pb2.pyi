from qk_api_contracts.grpc import common_pb2 as _common_pb2
from qk_api_contracts.grpc.characters import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CharacterIdRequest(_message.Message):
    __slots__ = ("character_id",)
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    def __init__(self, character_id: _Optional[str] = ...) -> None: ...

class ListCharactersRequest(_message.Message):
    __slots__ = ("user_id", "system", "page")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    system: str
    page: _common_pb2.PageRequest
    def __init__(self, user_id: _Optional[int] = ..., system: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListCharactersResponse(_message.Message):
    __slots__ = ("items", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_models_pb2.Character]
    page: _common_pb2.Page
    def __init__(self, items: _Optional[_Iterable[_Union[_models_pb2.Character, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...

class PlayHistoryResponse(_message.Message):
    __slots__ = ("records", "character_id", "page")
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[_models_pb2.PlayRecord]
    character_id: str
    page: _common_pb2.Page
    def __init__(self, records: _Optional[_Iterable[_Union[_models_pb2.PlayRecord, _Mapping]]] = ..., character_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...
