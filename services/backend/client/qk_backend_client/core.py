from collections.abc import Iterable
from dataclasses import dataclass


class BackendGrpcError(RuntimeError):
    """Top-level error for Gateway -> Backend gRPC failures."""


@dataclass
class RequestMetadata:
    request_id: int
    server_id: int
    user_id: int

    def format(self) -> Iterable[tuple[str, str]]:
        return [
            ("x-request-id", str(self.request_id)),
            ("x-server-id", str(self.server_id)),
            ("x-user-id", str(self.user_id)),
        ]
