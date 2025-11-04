from sessions import models_pb2 as _models_pb2
from events import models_pb2 as _models_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetMessageIdRequest(_message.Message):
    __slots__ = ("session_id", "message_id", "expected_version")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    message_id: str
    expected_version: int
    def __init__(self, session_id: _Optional[str] = ..., message_id: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...
