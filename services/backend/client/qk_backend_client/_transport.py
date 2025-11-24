from dataclasses import dataclass

import grpc
from grpc.aio import Channel
from qk_api_contracts.grpc.characters.service_pb2_grpc import CharactersStub
from qk_api_contracts.grpc.events.service_pb2_grpc import EventsStub
from qk_api_contracts.grpc.servers_pb2_grpc import ServersStub
from qk_api_contracts.grpc.sessions.service_pb2_grpc import SessionsStub
from qk_api_contracts.grpc.worker_service_pb2_grpc import WorkerStub

from .config import BackendGrpcConfig


def create_channel(config: BackendGrpcConfig) -> Channel:
    target = config.target()
    options = list(config.channel_options)

    if config.use_tls:
        creds = grpc.ssl_channel_credentials(
            root_certificates=config.root_certificates,
            private_key=config.private_key,
            certificate_chain=config.certificate_chain,
        )
        return grpc.aio.secure_channel(target, creds, options=options)

    return grpc.aio.insecure_channel(target, options=options)


@dataclass
class BackendGrpcTransport:
    """Connection to the backend gRPC service."""
    config: BackendGrpcConfig
    channel: Channel

    characters: CharactersStub
    sessions: SessionsStub
    events: EventsStub
    servers: ServersStub
    worker: WorkerStub

    @classmethod
    def create(cls, config: BackendGrpcConfig) -> "BackendGrpcTransport":
        ch = create_channel(config)
        return cls(
            config=config,
            channel=ch,
            characters=CharactersStub(ch),
            sessions=SessionsStub(ch),
            events=EventsStub(ch),
            servers=ServersStub(ch),
            worker=WorkerStub(ch),
        )

    async def aclose(self) -> None:
        await self.channel.close()
