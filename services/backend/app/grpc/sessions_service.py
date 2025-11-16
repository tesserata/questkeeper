import grpc
from loguru import logger
from qk_api_contracts.grpc.sessions.commands_service_pb2 import (
    CancelSessionRequest,
    EditBasicsRequest,
    EditCapacityRequest,
    EditGMRequest,
    EditOrganizationRequest,
    EditScheduleRequest,
    PublishSessionRequest,
    SetCharacterRequest,
    SignOutRequest,
    SwitchMainRequest,
    SwitchReserveRequest,
)
from qk_api_contracts.grpc.sessions.commands_service_pb2_grpc import (
    SessionCommandsServicer,
    SignupCommandsServicer,
)
from qk_api_contracts.grpc.sessions.models_pb2 import (
    Session,
    SessionInfo,
    SessionSummary,
    SessionView,
    Signup,
)
from qk_api_contracts.grpc.sessions.query_service_pb2 import (
    GetSessionRequest,
    ListSessionsRequest,
    ListSessionsResponse,
)
from qk_api_contracts.grpc.sessions.query_service_pb2_grpc import SessionsQueryServicer

from app.application.sessions import create_session
from app.grpc.mappers.session import session_domain_to_pb, session_info_pb_to_domain


class SessionsCommandsService(SessionCommandsServicer):
    async def CreateSession(
        self, request: SessionInfo, context: grpc.aio.ServicerContext
    ) -> Session:
        try:
            payload = session_info_pb_to_domain(request)
            session = await create_session(payload)

            return session_domain_to_pb(session)

        except Exception as e:
            logger.exception(e)
            return Session()

    async def EditBasics(
        self, request: EditBasicsRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def EditSchedule(
        self, request: EditScheduleRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def EditCapacity(
        self, request: EditCapacityRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def EditOrganization(
        self, request: EditOrganizationRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def EditGM(self, request: EditGMRequest, context: grpc.aio.ServicerContext) -> Session:
        pass

    async def PublishSession(
        self, request: PublishSessionRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def CancelSession(
        self, request: CancelSessionRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass


class SessionsQueryService(SessionsQueryServicer):
    async def GetSession(
        self, request: GetSessionRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def GetSessionView(
        self, request: GetSessionRequest, context: grpc.aio.ServicerContext
    ) -> SessionView:
        pass

    async def GetSessionSummary(
        self, request: GetSessionRequest, context: grpc.aio.ServicerContext
    ) -> SessionSummary:
        pass

    async def ListSessions(
        self, request: ListSessionsRequest, context: grpc.aio.ServicerContext
    ) -> ListSessionsResponse:
        pass


class SignupsCommandsService(SignupCommandsServicer):
    async def SignupToSession(self, request: Signup, context: grpc.aio.ServicerContext) -> Signup:
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
