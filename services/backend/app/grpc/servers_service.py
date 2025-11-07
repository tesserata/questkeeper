import grpc
from qk_api_contracts.grpc.servers_pb2 import (
    GetRoleMappingRequest,
    GetServerSettingsRequest,
    RoleMapping,
    ServerSettings,
)
from qk_api_contracts.grpc.servers_pb2_grpc import ServersServicer


class ServersService(ServersServicer):
    async def GetServerSettings(
        self, request: GetServerSettingsRequest, context: grpc.aio.ServicerContext
    ) -> ServerSettings:
        pass

    async def EditServerSettings(
        self, request: ServerSettings, context: grpc.aio.ServicerContext
    ) -> ServerSettings:
        pass

    async def GetRoleMapping(
        self, request: GetRoleMappingRequest, context: grpc.aio.ServicerContext
    ) -> RoleMapping:
        pass

    async def UpdateRoleMapping(
        self, request: RoleMapping, context: grpc.aio.ServicerContext
    ) -> RoleMapping:
        pass
