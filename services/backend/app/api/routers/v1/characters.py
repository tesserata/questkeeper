from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Query, Response, status
from qk_api_contracts.schema.characters import (
    Character,
    CharacterBase,
    CharacterList,
    CharacterListQuery,
)

from app.api.request_meta import RequestMeta, get_request_meta
from app.services import characters_service
from app.services.exceptions import (
    ConcurrencyConflictException,
    PermissionDeniedException,
)
from app.services.pagination import PaginationParams

from ._mappers import character_base_dto_to_domain, character_domain_to_dto

router = APIRouter(prefix="/v1/characters", tags=["characters"])


@router.post(
    "",
    response_model=Character,
    status_code=status.HTTP_201_CREATED,
    # dependencies=[Depends(require_permission(AppRole.PLAYER))],
)
async def create_character(
    payload: Annotated[CharacterBase, Body()],
    meta: RequestMeta = Depends(get_request_meta),
    response: Response = None,
) -> Character:
    character_create = character_base_dto_to_domain(payload)
    character_create.user_id = meta.user_id
    character = await characters_service.create_character(character_create)

    if response is not None:
        version = character.version_header.version
        response.headers["ETag"] = f'W/"{version}"'

    return character_domain_to_dto(character)


@router.delete(
    "/{character_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    # dependencies=[Depends(require_permission(AppRole.PLAYER))],
)
async def delete_character(
    character_id: UUID,
    meta: RequestMeta = Depends(get_request_meta),
) -> None:
    expected_version = meta.expected_version
    if not expected_version:
        raise ConcurrencyConflictException("character", str(character_id), expected_version)

    owner_id = await characters_service.get_owner(character_id)
    if owner_id != meta.user_id:
        raise PermissionDeniedException("character", str(character_id))

    await characters_service.delete_character(character_id, expected_version=expected_version)


@router.patch(
    "/{character_id}",
    status_code=status.HTTP_200_OK,
    response_model=Character,
    # dependencies=[Depends(require_permission(AppRole.PLAYER))],
)
async def update_character(
    character_id: UUID,
    payload: Annotated[CharacterBase, Body()],
    meta: RequestMeta = Depends(get_request_meta),
    response: Response = None,
) -> Character:
    expected_version = meta.expected_version
    if not expected_version:
        raise ConcurrencyConflictException("character", str(character_id), expected_version)

    owner_id = await characters_service.get_owner(character_id)
    if owner_id != meta.user_id:
        raise PermissionDeniedException("character", str(character_id))

    character_update = character_base_dto_to_domain(payload)
    character_update.user_id = meta.user_id
    character_update.character_id = character_id

    character = await characters_service.update_character(
        character_update,
        expected_version=expected_version,
    )

    if response is not None:
        version = character.version_header.version
        response.headers["ETag"] = f'W/"{version}"'

    return character_domain_to_dto(character)


@router.get(
    "/{character_id}",
    response_model=Character,
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(require_permission(AppRole.PLAYER))],
)
async def get_character(
    character_id: UUID, response: Response = None, meta: RequestMeta = Depends(get_request_meta)
) -> Character:
    owner_id = await characters_service.get_owner(character_id)
    if owner_id != meta.user_id:
        raise PermissionDeniedException("character", str(character_id))

    character = await characters_service.get_character_by_id(character_id)
    if response is not None:
        version = character.version_header.version
        response.headers["ETag"] = f'W/"{version}"'

    return character_domain_to_dto(character)


@router.get(
    "",
    response_model=CharacterList,
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(require_permission(AppRole.PLAYER))],
)
async def list_characters(
    query: Annotated[CharacterListQuery, Query()], meta: RequestMeta = Depends(get_request_meta)
) -> CharacterList:
    characters, next_token = await characters_service.list_characters(
        pagination=PaginationParams(size=query.page_size, next_token=query.next_page_token),
        user_ids=query.user_ids,
        system=query.system,
        level_min=query.level_min,
        level_max=query.level_max,
    )

    return CharacterList(
        items=[character_domain_to_dto(c) for c in characters],
        next_page_token=next_token,
    )
