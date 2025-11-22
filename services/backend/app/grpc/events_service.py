import grpc
from qk_api_contracts.grpc.events.models_pb2 import (
    Event,
    EventInfo,
    EventSummary,
    EventView,
)
from qk_api_contracts.grpc.events.service_pb2 import (
    EditBasicsRequest,
    EditOrganizationRequest,
    EditScheduleRequest,
    EventOperationRequest,
    GetEventRequest,
    ListEventsRequest,
    ListEventsResponse,
)
from qk_api_contracts.grpc.events.service_pb2_grpc import EventsServicer


class EventsServiceImpl(EventsServicer):
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
        self, request: EventOperationRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass

    async def CancelEvent(
        self, request: EventOperationRequest, context: grpc.aio.ServicerContext
    ) -> Event:
        pass

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
