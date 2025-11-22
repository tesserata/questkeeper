from uuid import UUID

import grpc
from loguru import logger
from qk_api_contracts.grpc.sessions.models_pb2 import (
    Session,
    SessionInfo,
    SessionSummary,
    SessionView,
    Signup,
)
from qk_api_contracts.grpc.sessions.service_pb2 import (
    EditBasicsRequest,
    EditCapacityRequest,
    EditGMRequest,
    EditOrganizationRequest,
    EditScheduleRequest,
    GetSessionRequest,
    ListSessionsRequest,
    ListSessionsResponse,
    SessionOperationRequest,
    SetCharacterRequest,
    SignupOperationRequest,
)
from qk_api_contracts.grpc.sessions.service_pb2_grpc import (
    SessionsServicer,
    SignupsServicer,
)

from app.application.sessions import create_session, get_session, get_session_view
from app.grpc.mappers.session import (
    session_domain_to_pb,
    session_domain_to_summary_pb,
    session_domain_to_view_pb,
    session_info_pb_to_domain,
)


class SessionsServiceImpl(SessionsServicer):
    async def CreateSession(
        self, request: SessionInfo, context: grpc.aio.ServicerContext
    ) -> Session | None:
        try:
            payload = session_info_pb_to_domain(request)
            session = await create_session(payload)

            return session_domain_to_pb(session)

        except Exception as e:
            logger.exception(e)

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
        self, request: SessionOperationRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def CancelSession(
        self, request: SessionOperationRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def GetSession(
        self, request: GetSessionRequest, context: grpc.aio.ServicerContext
    ) -> Session | None:
        try:
            session = await get_session(session_id=UUID(request.session_id))
            return session_domain_to_pb(session)
        except Exception as e:
            logger.exception(e)

    async def GetSessionView(
        self, request: GetSessionRequest, context: grpc.aio.ServicerContext
    ) -> SessionView | None:
        try:
            session, characters = await get_session_view(session_id=UUID(request.session_id))
            return session_domain_to_view_pb(session, characters=characters)
        except Exception as e:
            logger.exception(e)

    async def GetSessionSummary(
        self, request: GetSessionRequest, context: grpc.aio.ServicerContext
    ) -> SessionSummary | None:
        try:
            session = await get_session(session_id=UUID(request.session_id), with_signups=True)
            return session_domain_to_summary_pb(session)
        except Exception as e:
            logger.exception(e)

    async def ListSessions(
        self, request: ListSessionsRequest, context: grpc.aio.ServicerContext
    ) -> ListSessionsResponse:
        pass


class SignupsServiceImpl(SignupsServicer):
    async def SignupToSession(self, request: Signup, context: grpc.aio.ServicerContext) -> Signup:
        pass

    async def SwitchMain(
        self, request: SignupOperationRequest, context: grpc.aio.ServicerContext
    ) -> Signup:
        pass

    async def SwitchReserve(
        self, request: SessionOperationRequest, context: grpc.aio.ServicerContext
    ) -> Signup:
        pass

    async def SignOut(
        self, request: SignupOperationRequest, context: grpc.aio.ServicerContext
    ) -> None:
        pass

    async def SetCharacter(
        self, request: SetCharacterRequest, context: grpc.aio.ServicerContext
    ) -> Signup:
        pass
