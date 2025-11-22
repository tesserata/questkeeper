import grpc
from qk_api_contracts.grpc.events.models_pb2 import Event
from qk_api_contracts.grpc.sessions.models_pb2 import Session
from qk_api_contracts.grpc.worker_service_pb2 import SetMessageIdRequest
from qk_api_contracts.grpc.worker_service_pb2_grpc import WorkerServicer


class WorkersServiceImpl(WorkerServicer):
    async def SetSessionMessageId(
        self, request: SetMessageIdRequest, context: grpc.aio.ServicerContext
    ) -> Session:
        pass

    async def SetEventMessageId(
        self, request: SetMessageIdRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass
