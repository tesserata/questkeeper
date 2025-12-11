from fastapi import Response

from app.domain.characters import Character
from app.domain.server_settings import ServerSettings
from app.domain.sessions import Session


def get_etag_header(model: Character | Session | ServerSettings, response: Response | None) -> None:
    if response is not None:
        version = model.version_header.version
        response.headers["ETag"] = f'W/"{version}"'
    return response

