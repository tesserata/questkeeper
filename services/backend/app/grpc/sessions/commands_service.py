import grpc
from loguru import logger
from qk_api_contracts.grpc.common_pb2 import VersionHeader
from qk_api_contracts.grpc.sessions.commands_service_pb2 import (
    CancelSessionRequest,
    EditBasicsRequest,
    EditCapacityRequest,
    EditGMRequest,
    EditOrganizationRequest,
    EditScheduleRequest,
    PublishSessionRequest,
)
from qk_api_contracts.grpc.sessions.commands_service_pb2_grpc import (
    SessionCommandsServicer,
)
from qk_api_contracts.grpc.sessions.models_pb2 import (
    Session,
    SessionInfo,
)

from app.application.sessions import create_session


class SessionsCommandsService(SessionCommandsServicer):
    async def CreateSession(
        self, request: SessionInfo, context: grpc.aio.ServicerContext
    ) -> Session:
        try:
            session, version_header = await create_session(request)
            return Session(
                session_id=str(session.session_id),
                info=request,
                status=session.status,
                version=VersionHeader(
                    version=version_header.version,
                    weak_etag=version_header.weak_etag,
                    updated_at=version_header.updated_at,
                ),
            )
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
        self, request: PublishSessionRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def CancelSession(
        self, request: CancelSessionRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass
