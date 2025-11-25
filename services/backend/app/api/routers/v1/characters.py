from uuid import UUID

from fastapi import APIRouter, Depends, Response, status
from qk_api_contracts.enums import AppRole
from qk_api_contracts.schema.characters import (
    CharacterCreate,
    CharacterList,
    CharacterRead,
)

from app.api.auth import require_permission
from app.services import characters_service

from ._mappers import character_base_to_domain, character_domain_to_read

router = APIRouter(prefix="/v1/characters", tags=["characters"])


@router.post(
    "",
    response_model=CharacterRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AppRole.PLAYER))],
)
async def create_character(
    payload: CharacterCreate,
    response: Response = None,
):
    character = await characters_service.create_character(character_base_to_domain(payload))

    if response is not None:
        version = character.version_header.version
        response.headers["ETag"] = f"W/{version}"

    return character_domain_to_read(character)


@router.get(
    "/{character_id}",
    response_model=CharacterRead,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission(AppRole.PLAYER))],
)
async def get_character(
    character_id: str,
    response: Response = None,
):
    character = await characters_service.get_character_by_id(UUID(character_id))
    if response is not None:
        version = character.version_header.version
        response.headers["ETag"] = f"W/{version}"

    return character_domain_to_read(character)


@router.get("", response_model=CharacterList)
async def list_characters(): ...
