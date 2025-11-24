from dataclasses import dataclass

from ._clients.characters_client import CharactersClient
from ._transport import BackendGrpcTransport
from .config import BackendGrpcConfig


@dataclass
class BackendGrpcClient:
    transport: BackendGrpcTransport

    characters: CharactersClient

    @classmethod
    def create(cls, config: BackendGrpcConfig) -> "BackendGrpcClient":
        transport = BackendGrpcTransport.create(config)
        return cls(transport=transport, characters=CharactersClient(transport))

    async def aclose(self) -> None:
        await self.transport.aclose()
