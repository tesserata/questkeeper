from uuid import UUID

import grpc
from qk_api_contracts.grpc.characters.models_pb2 import Character, CharacterInfo
from qk_api_contracts.grpc.characters.service_pb2 import (
    CharacterIdRequest,
    DeleteCharacterRequest,
    EditClassRequest,
    EditLevelRequest,
    EditNameRequest,
    EditNotesRequest,
    EditRaceRequest,
    EditSystemRequest,
    ListCharactersRequest,
    ListCharactersResponse,
    PlayHistoryResponse,
)
from qk_api_contracts.grpc.characters.service_pb2_grpc import CharactersServicer

from app.application.characters import create_character, delete_character, get_character_by_id
from app.grpc.mappers.character import character_domain_to_pb, character_info_pb_to_domain


class CharactersServiceImpl(CharactersServicer):
    async def CreateCharacter(
        self, request: CharacterInfo, context: grpc.aio.ServicerContext
    ) -> Character | None:
        payload = character_info_pb_to_domain(request)
        character = await create_character(payload=payload)
        return character_domain_to_pb(character)

    async def EditName(
        self, request: EditNameRequest, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

    async def EditSystem(
        self, request: EditSystemRequest, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

    async def EditClass(
        self, request: EditClassRequest, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

    async def EditRace(
        self, request: EditRaceRequest, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

    async def EditLevel(
        self, request: EditLevelRequest, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

    async def EditNotes(
        self, request: EditNotesRequest, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

    async def DeleteCharacter(
        self, request: DeleteCharacterRequest, context: grpc.aio.ServicerContext
    ) -> None:
        await delete_character(character_id=UUID(request.character_id))

    async def GetCharacter(
        self, request: CharacterIdRequest, context: grpc.aio.ServicerContext
    ) -> Character | None:
        character = await get_character_by_id(character_id=UUID(request.character_id))
        pb = character_domain_to_pb(character)
        return pb

    async def ListCharacters(
        self, request: ListCharactersRequest, context: grpc.aio.ServicerContext
    ) -> ListCharactersResponse:
        pass

    async def GetCharacterPlayHistory(
        self, request: CharacterIdRequest, context: grpc.aio.ServicerContext
    ) -> PlayHistoryResponse:
        pass
