import grpc
from qk_api_contracts.grpc.events.commands_service_pb2 import (
    CancelEventRequest,
    EditBasicsRequest,
    EditOrganizationRequest,
    EditScheduleRequest,
    PublishEventRequest,
)
from qk_api_contracts.grpc.events.commands_service_pb2_grpc import EventsCommandsServicer
from qk_api_contracts.grpc.events.models_pb2 import Event, EventInfo, EventSummary, EventView
from qk_api_contracts.grpc.events.query_service_pb2 import (
    GetEventRequest,
    ListEventsRequest,
    ListEventsResponse,
)
from qk_api_contracts.grpc.events.query_service_pb2_grpc import EventsQueryServicer


class EventsCommandsService(EventsCommandsServicer):
    async def CreateEvent(self, request: EventInfo, context: grpc.aio.ServicerContext) -> Event:
        pass

    async def EditBasics(
        self, request: EditBasicsRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass

    async def EditSchedule(
        self, request: EditScheduleRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass

    async def EditOrganization(
        self, request: EditOrganizationRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass

    async def PublishEvent(
        self, request: PublishEventRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass

    async def CancelEvent(
        self, request: CancelEventRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass


class EventsQueryService(EventsQueryServicer):
    async def GetEvent(self, request: GetEventRequest, context: grpc.aio.ServicerContext) -> Event:
        pass

    async def GetEventView(
        self, request: GetEventRequest, context: grpc.aio.ServicerContext
    ) -> EventView:
        pass

    async def GetEventSummary(
        self, request: GetEventRequest, context: grpc.aio.ServicerContext
    ) -> EventSummary:
        pass

    async def ListEvents(
        self, request: ListEventsRequest, context: grpc.aio.ServicerContext
    ) -> ListEventsResponse:
        pass
