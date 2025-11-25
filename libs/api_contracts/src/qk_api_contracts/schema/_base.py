from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

NonEmptyStr = Annotated[str, Field(min_length=1, max_length=100)]


class QkSchema(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True, validate_assignment=True)


class VersionHeader(QkSchema):
    version: int
    created_at: datetime
    updated_at: datetime
