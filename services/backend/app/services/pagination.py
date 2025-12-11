import base64
import json
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.infrastructure.db.helpers import Cursor


class InvalidPageToken(ValueError):
    pass


def encode_page_token(cursor: Cursor) -> str:
    payload = {
        "created_at": cursor.created_at.isoformat(),
        "last_id": str(cursor.last_id),
    }
    raw = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(raw).decode("ascii")


def decode_page_token(token: str) -> Cursor:
    try:
        raw = base64.urlsafe_b64decode(token.encode("ascii"))
        payload = json.loads(raw.decode("utf-8"))
        return Cursor(
            created_at=datetime.fromisoformat(payload["created_at"]),
            last_id=UUID(payload["last_id"]),
        )
    except Exception as exc:
        raise InvalidPageToken("Malformed page_token") from exc


@dataclass
class PaginationParams:
    size: int
    next_token: str | None = None
