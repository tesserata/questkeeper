from typing import TypeVar

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.message import Message
from pydantic import BaseModel

TPydantic = TypeVar("TPydantic", bound=BaseModel)
TProto = TypeVar("TProto", bound=Message)


def pydantic_to_proto[TProto: Message](model: BaseModel, proto_cls: type[TProto]) -> TProto:
    data = model.model_dump(
        exclude_unset=True,
        by_alias=True,
    )

    msg = proto_cls()
    ParseDict(
        data,
        msg,
        ignore_unknown_fields=True,
    )
    return msg


def proto_to_pydantic[TPydantic: BaseModel](msg: Message, model_cls: type[TPydantic]) -> TPydantic:
    data = MessageToDict(
        msg,
        preserving_proto_field_name=True,
    )
    return model_cls.model_validate(data)
