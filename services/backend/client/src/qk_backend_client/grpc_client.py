from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum

import grpc
from grpc.aio import Channel
from qk_api_contracts.grpc.characters.models_pb2 import CharacterInfo as CharacterInfoPb
from qk_api_contracts.grpc.characters.service_pb2 import CharacterIdRequest
from qk_api_contracts.grpc.characters.service_pb2_grpc import CharactersStub
from qk_api_contracts.grpc.events.service_pb2_grpc import EventsStub
from qk_api_contracts.grpc.servers_pb2_grpc import ServersStub
from qk_api_contracts.grpc.sessions.service_pb2_grpc import SessionsStub
from qk_api_contracts.grpc.worker_service_pb2_grpc import WorkerStub
from qk_api_contracts.mappings import proto_to_pydantic, pydantic_to_proto
from qk_api_contracts.pydantic.characters.models_p2p import Character, CharacterInfo

from .config import BackendGrpcConfig


class BackendGrpcError(RuntimeError):
    """Top-level error for Gateway -> Backend gRPC failures."""


class _Service(StrEnum):
    CHARACTERS = "characters"
    SESSIONS = "sessions"
    EVENTS = "events"
    SERVERS = "servers"
    WORKER = "worker"


@dataclass
class RequestMetadata:
    request_id: int
    server_id: int
    user_id: int

    def format(self) -> Iterable[tuple[str, str]]:
        return [
            ("x-request-id", str(self.request_id)),
            ("x-server-id", str(self.server_id)),
            ("x-user-id", str(self.user_id)),
        ]


def create_channel(config: BackendGrpcConfig) -> Channel:
    target = config.target()

    options = list(config.channel_options)

    if config.use_tls:
        creds = grpc.ssl_channel_credentials(
            root_certificates=config.root_certificates,
            private_key=config.private_key,
            certificate_chain=config.certificate_chain,
        )
        return grpc.aio.secure_channel(
            target,
            creds,
            options=options,
        )

    return grpc.aio.insecure_channel(
        target,
        options=options,
    )


class _BaseGrpcClient:
    """
    Async gRPC client for the Backend (Domain) service.

    - Owns / shares a grpc.aio.Channel.
    - Uses generated Pydantic models from libs/api_contracts at the boundary.
    - Hides protobuf stubs/messages behind a thin adapter.
    """

    def __init__(self, config: BackendGrpcConfig, *, channel: Channel | None = None):
        self._config = config
        self._owned_channel = channel is None
        self._channel: Channel = channel or create_channel(config)

        self._stubs = dict()
        self._setup_stubs()

    def _setup_stubs(self):
        self._stubs[_Service.CHARACTERS] = CharactersStub(self._channel)
        self._stubs[_Service.SESSIONS] = SessionsStub(self._channel)
        self._stubs[_Service.EVENTS] = EventsStub(self._channel)
        self._stubs[_Service.SERVERS] = ServersStub(self._channel)
        self._stubs[_Service.WORKER] = WorkerStub(self._channel)

    async def __aenter__(self) -> "_BaseGrpcClient":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._owned_channel:
            await self._channel.close()

    def _deadline(self, timeout_s: float | None) -> float:
        return timeout_s if timeout_s is not None else self._config.default_timeout_s


class BackendGrpcClient(_BaseGrpcClient):
    async def create_character(
        self,
        payload: CharacterInfo,
        metadata: RequestMetadata | None = None,
    ) -> Character:
        """
        Wraps: rpc CreateCharacter(CreateCharacterRequest) returns (Character);
        """
        pb_request = pydantic_to_proto(payload, CharacterInfoPb)
        stub: CharactersStub = self._stubs.get(_Service.CHARACTERS)
        try:
            pb_resp = await stub.CreateCharacter(
                pb_request,
                metadata=metadata.format(),
            )
        except grpc.aio.AioRpcError as exc:
            raise BackendGrpcError(f"CreateCharacter RPC failed: {exc}") from exc

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
        stub: CharactersStub = self._stubs.get(_Service.CHARACTERS)
        try:
            pb_resp = await stub.GetCharacter(
                pb_request,
                metadata=metadata.format(),
            )
        except grpc.aio.AioRpcError as exc:
            raise BackendGrpcError(f"GetCharacter RPC failed: {exc}") from exc

        return proto_to_pydantic(pb_resp, Character)
