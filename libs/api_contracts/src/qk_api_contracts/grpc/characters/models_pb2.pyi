import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from qk_api_contracts.grpc import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CharacterInfo(_message.Message):
    __slots__ = ("user_id", "system", "name", "class_name", "subclass_name", "level", "race", "notes")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBCLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    RACE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    system: str
    name: str
    class_name: str
    subclass_name: str
    level: int
    race: str
    notes: str
    def __init__(self, user_id: _Optional[int] = ..., system: _Optional[str] = ..., name: _Optional[str] = ..., class_name: _Optional[str] = ..., subclass_name: _Optional[str] = ..., level: _Optional[int] = ..., race: _Optional[str] = ..., notes: _Optional[str] = ...) -> None: ...

class Character(_message.Message):
    __slots__ = ("character_id", "info", "version")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    character_id: str
    info: CharacterInfo
    version: _common_pb2.VersionHeader
    def __init__(self, character_id: _Optional[str] = ..., info: _Optional[_Union[CharacterInfo, _Mapping]] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...

class PlayRecord(_message.Message):
    __slots__ = ("session_title", "gm_user_id", "time", "server_id", "channel_id", "message_id", "version")
    SESSION_TITLE_FIELD_NUMBER: _ClassVar[int]
    GM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    session_title: str
    gm_user_id: int
    time: _timestamp_pb2.Timestamp
    server_id: int
    channel_id: int
    message_id: int
    version: _common_pb2.VersionHeader
    def __init__(self, session_title: _Optional[str] = ..., gm_user_id: _Optional[int] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., server_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., message_id: _Optional[int] = ..., version: _Optional[_Union[_common_pb2.VersionHeader, _Mapping]] = ...) -> None: ...
