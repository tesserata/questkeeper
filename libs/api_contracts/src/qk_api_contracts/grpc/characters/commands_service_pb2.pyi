from google.protobuf import empty_pb2 as _empty_pb2
from qk_api_contracts.grpc.characters import models_pb2 as _models_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EditNameRequest(_message.Message):
    __slots__ = ("character_id", "name", "expected_version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    name: str
    expected_version: int
    def __init__(self, character_id: _Optional[str] = ..., name: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditSystemRequest(_message.Message):
    __slots__ = ("character_id", "game_system", "expected_version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    game_system: str
    expected_version: int
    def __init__(self, character_id: _Optional[str] = ..., game_system: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditClassRequest(_message.Message):
    __slots__ = ("character_id", "subclass", "expected_version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    SUBCLASS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    subclass: str
    expected_version: int
    def __init__(self, character_id: _Optional[str] = ..., subclass: _Optional[str] = ..., expected_version: _Optional[int] = ..., **kwargs) -> None: ...

class EditRaceRequest(_message.Message):
    __slots__ = ("character_id", "race", "expected_version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    RACE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    race: str
    expected_version: int
    def __init__(self, character_id: _Optional[str] = ..., race: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditLevelRequest(_message.Message):
    __slots__ = ("character_id", "level", "expected_version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    level: int
    expected_version: int
    def __init__(self, character_id: _Optional[str] = ..., level: _Optional[int] = ..., expected_version: _Optional[int] = ...) -> None: ...

class EditNotesRequest(_message.Message):
    __slots__ = ("character_id", "notes", "expected_version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    notes: str
    expected_version: int
    def __init__(self, character_id: _Optional[str] = ..., notes: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class DeleteCharacterRequest(_message.Message):
    __slots__ = ("character_id", "expected_version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    expected_version: int
    def __init__(self, character_id: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...
