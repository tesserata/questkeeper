import grpc
from qk_api_contracts.grpc.sessions.models_pb2 import (
    Session,
    SessionSummary,
    SessionView,
)
from qk_api_contracts.grpc.sessions.query_service_pb2 import (
    GetSessionRequest,
    ListSessionsRequest,
    ListSessionsResponse,
)
from qk_api_contracts.grpc.sessions.query_service_pb2_grpc import SessionsQueryServicer


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
