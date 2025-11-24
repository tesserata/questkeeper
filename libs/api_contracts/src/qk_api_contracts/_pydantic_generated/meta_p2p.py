# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 6.33.0 
# Pydantic Version: 2.12.3 
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class HealthRequest(BaseModel):
    pass

class HealthResponse(BaseModel):
    status: str = Field(default="")

class VersionsRequest(BaseModel):
    pass

class VersionsResponse(BaseModel):
    components: "typing.Dict[str, str]" = Field(default_factory=dict)
