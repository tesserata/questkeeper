import grpc
from qk_api_contracts.grpc.characters.commands_service_pb2 import (
    DeleteCharacterRequest,
    EditClassRequest,
    EditLevelRequest,
    EditNameRequest,
    EditNotesRequest,
    EditRaceRequest,
    EditSystemRequest,
)
from qk_api_contracts.grpc.characters.commands_service_pb2_grpc import CharacterCommandsServicer
from qk_api_contracts.grpc.characters.models_pb2 import Character, CharacterInfo, CharacterSummary
from qk_api_contracts.grpc.characters.query_service_pb2 import (
    GetCharacterRequest,
    ListCharactersRequest,
    ListCharactersResponse,
)
from qk_api_contracts.grpc.characters.query_service_pb2_grpc import CharactersQueryServicer


class CharactersService(CharacterCommandsServicer):
    async def CreateCharacter(
        self, request: CharacterInfo, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

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
        pass


class CharactersQueryService(CharactersQueryServicer):
    async def GetCharacter(
        self, request: GetCharacterRequest, context: grpc.aio.ServicerContext
    ) -> Character:
        pass

    async def GetCharacterSummary(
        self, request: GetCharacterRequest, context: grpc.aio.ServicerContext
    ) -> CharacterSummary:
        pass

    async def ListCharacters(
        self, request: ListCharactersRequest, context: grpc.aio.ServicerContext
    ) -> ListCharactersResponse:
        pass
