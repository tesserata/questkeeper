from .._transport import BackendGrpcTransport


class BaseServiceClient:
    def __init__(self, transport: BackendGrpcTransport) -> None:
        self._transport = transport

    def _deadline(self, timeout_s: float | None) -> float:
        return timeout_s if timeout_s is not None else self._transport.config.default_timeout_s
