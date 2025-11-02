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

class CreateCharacterRequest(_message.Message):
    __slots__ = ("meta", "character")
    META_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    character: Character
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., character: _Optional[_Union[Character, _Mapping]] = ...) -> None: ...

class GetCharacterRequest(_message.Message):
    __slots__ = ("meta", "character_id")
    META_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    character_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., character_id: _Optional[str] = ...) -> None: ...

class DeleteCharacterRequest(_message.Message):
    __slots__ = ("meta", "character_id")
    META_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    character_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., character_id: _Optional[str] = ...) -> None: ...

class UpdateCharacterRequest(_message.Message):
    __slots__ = ("meta", "character_id", "update")
    META_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    character_id: str
    update: UpdateCharacter
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., character_id: _Optional[str] = ..., update: _Optional[_Union[UpdateCharacter, _Mapping]] = ...) -> None: ...

class UpdateCharacter(_message.Message):
    __slots__ = ("name", "race", "level", "notes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RACE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    race: str
    level: int
    notes: str
    def __init__(self, name: _Optional[str] = ..., race: _Optional[str] = ..., level: _Optional[int] = ..., notes: _Optional[str] = ..., **kwargs) -> None: ...

class GetCharacterHistoryRequest(_message.Message):
    __slots__ = ("meta", "character_id")
    META_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    character_id: str
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., character_id: _Optional[str] = ...) -> None: ...

class GetCharacterHistoryResponse(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[CharacterHistoryEntry]
    def __init__(self, history: _Optional[_Iterable[_Union[CharacterHistoryEntry, _Mapping]]] = ...) -> None: ...

class CharacterHistoryEntry(_message.Message):
    __slots__ = ("session_id", "event_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    event_id: str
    def __init__(self, session_id: _Optional[str] = ..., event_id: _Optional[str] = ...) -> None: ...

class ListCharactersRequest(_message.Message):
    __slots__ = ("meta", "page", "user_id")
    META_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    meta: _common_pb2.RequestMeta
    page: _common_pb2.PageRequest
    user_id: int
    def __init__(self, meta: _Optional[_Union[_common_pb2.RequestMeta, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ..., user_id: _Optional[int] = ...) -> None: ...

class ListCharactersResponse(_message.Message):
    __slots__ = ("characters", "page")
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[Character]
    page: _common_pb2.Page
    def __init__(self, characters: _Optional[_Iterable[_Union[Character, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...

class Character(_message.Message):
    __slots__ = ("character_id", "user_id", "system", "level", "name", "race", "subclass", "notes", "created_at", "updated_at")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RACE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    SUBCLASS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    user_id: int
    system: _enums_pb2.GameSystem
    level: int
    name: str
    race: str
    subclass: str
    notes: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, character_id: _Optional[str] = ..., user_id: _Optional[int] = ..., system: _Optional[_Union[_enums_pb2.GameSystem, str]] = ..., level: _Optional[int] = ..., name: _Optional[str] = ..., race: _Optional[str] = ..., subclass: _Optional[str] = ..., notes: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class CharacterResponse(_message.Message):
    __slots__ = ("character", "version")
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    character: Character
    version: _common_pb2.VersionHeader
    def __init__(self, character: _Optional[_Union[Character, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...
