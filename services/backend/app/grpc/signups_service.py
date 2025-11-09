import grpc
from qk_api_contracts.grpc.sessions.commands_service_pb2 import (
    SetCharacterRequest,
    SignOutRequest,
    SwitchMainRequest,
    SwitchReserveRequest,
)
from qk_api_contracts.grpc.sessions.commands_service_pb2_grpc import (
    SignupCommandsServicer,
)
from qk_api_contracts.grpc.sessions.models_pb2 import Signup


class SignupsCommandsService(SignupCommandsServicer):
    async def JoinSession(self, request: Signup, context: grpc.aio.ServicerContext) -> Signup:
        pass

    async def SwitchMain(
        self, request: SwitchMainRequest, context: grpc.aio.ServicerContext
    ) -> Signup:
        pass

    async def SwitchReserve(
        self, request: SwitchReserveRequest, context: grpc.aio.ServicerContext
    ) -> Signup:
        pass

    async def SignOut(self, request: SignOutRequest, context: grpc.aio.ServicerContext) -> None:
        pass

    async def SetCharacter(
        self, request: SetCharacterRequest, context: grpc.aio.ServicerContext
    ) -> Signup:
        pass
