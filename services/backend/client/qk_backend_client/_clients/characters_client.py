import grpc
from qk_api_contracts._pydantic_generated.characters.models_p2p import Character, CharacterInfo
from qk_api_contracts.grpc.characters.models_pb2 import CharacterInfo as CharacterInfoPb
from qk_api_contracts.grpc.characters.service_pb2 import CharacterIdRequest, DeleteCharacterRequest
from qk_api_contracts.grpc.characters.service_pb2_grpc import CharactersStub
from qk_api_contracts.mappings import proto_to_pydantic, pydantic_to_proto

from .._transport import BackendGrpcTransport
from ..core import BackendGrpcError, RequestMetadata
from .base import BaseServiceClient


class CharactersClient(BaseServiceClient):
    def __init__(self, transport: BackendGrpcTransport) -> None:
        super().__init__(transport)
        self._stub: CharactersStub = transport.characters

    async def create_character(
        self,
        payload: CharacterInfo,
        metadata: RequestMetadata | None = None,
    ) -> Character:
        """
        Wraps: rpc CreateCharacter(CreateCharacterRequest) returns (Character);
        """
        pb_request = pydantic_to_proto(payload, CharacterInfoPb)
        pb_resp = await self._stub.CreateCharacter(
            pb_request,
            metadata=metadata.format(),
        )

        return proto_to_pydantic(pb_resp, Character)

    async def get_character(
        self,
        character_id: str,
        metadata: RequestMetadata | None = None,
    ) -> Character:
        """
        Wraps: rpc GetCharacter(GetCharacterRequest) returns (Character);
        """
        pb_request = CharacterIdRequest(character_id=character_id)
        pb_resp = await self._stub.GetCharacter(
            pb_request,
            metadata=metadata.format(),
        )
        return proto_to_pydantic(pb_resp, Character)

    async def delete_character(
        self,
        character_id: str,
        expected_version: int,
        metadata: RequestMetadata | None = None,
    ) -> None:
        pb_request = DeleteCharacterRequest(
            character_id=character_id, expected_version=expected_version
        )
        await self._stub.DeleteCharacter(
            pb_request,
            metadata=metadata.format(),
        )
