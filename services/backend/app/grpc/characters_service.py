from uuid import UUID

import grpc
from loguru import logger
from qk_api_contracts.grpc.characters.commands_service_pb2 import (
    DeleteCharacterRequest,
    EditClassRequest,
    EditLevelRequest,
    EditNameRequest,
    EditNotesRequest,
    EditRaceRequest,
    EditSystemRequest,
)
from qk_api_contracts.grpc.characters.commands_service_pb2_grpc import CharactersCommandsServicer
from qk_api_contracts.grpc.characters.models_pb2 import Character, CharacterInfo
from qk_api_contracts.grpc.characters.query_service_pb2 import (
    CharacterIdRequest,
    ListCharactersRequest,
    ListCharactersResponse,
    PlayHistoryResponse,
)
from qk_api_contracts.grpc.characters.query_service_pb2_grpc import CharactersQueryServicer

from app.application.characters import create_character, delete_character, get_character_by_id
from app.grpc.mappers.character import character_domain_to_pb, character_info_pb_to_domain


class CharactersCommandsService(CharactersCommandsServicer):
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

class CharactersQueryService(CharactersQueryServicer):
    async def GetCharacter(
        self, request: CharacterIdRequest, context: grpc.aio.ServicerContext
    ) -> Character | None:
        character = await get_character_by_id(character_id=UUID(request.character_id))
        logger.info("Domain:")
        logger.info(character)
        pb = character_domain_to_pb(character)
        logger.info("Protobuf:")
        logger.info(pb)
        return pb

    async def ListCharacters(
        self, request: ListCharactersRequest, context: grpc.aio.ServicerContext
    ) -> ListCharactersResponse:
        pass

    async def GetCharacterPlayHistory(
        self, request: CharacterIdRequest, context: grpc.aio.ServicerContext
    ) -> PlayHistoryResponse:
        pass
