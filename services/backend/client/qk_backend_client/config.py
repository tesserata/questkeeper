from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class BackendGrpcConfig:
    """
    Configuration for the backend (domain) gRPC connection.
    """

    # Either set uds_path OR host/port
    uds_path: str | None = None  # = "/var/run/backend/backend-grpc.sock"
    host: str | None = None
    port: int | None = None

    use_tls: bool = False
    root_certificates: bytes | None = None
    private_key: bytes | None = None
    certificate_chain: bytes | None = None

    default_timeout_s: float = 2.0

    channel_options: Sequence[tuple[str, Any]] = field(default_factory=tuple)

    def target(self) -> str:
        if self.uds_path:
            return f"unix://{self.uds_path}"
        if self.host and self.port:
            return f"{self.host}:{self.port}"
        raise ValueError("BackendGrpcConfig: either uds_path or host+port must be set")
