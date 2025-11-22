import asyncio
import signal

import grpc
from loguru import logger
from qk_api_contracts.grpc.characters.service_pb2_grpc import (
    add_CharactersServicer_to_server,
)
from qk_api_contracts.grpc.events.service_pb2_grpc import (
    add_EventsServicer_to_server,
)
from qk_api_contracts.grpc.servers_pb2_grpc import add_ServersServicer_to_server
from qk_api_contracts.grpc.sessions.service_pb2_grpc import (
    add_SessionsServicer_to_server,
    add_SignupsServicer_to_server,
)
from qk_api_contracts.grpc.worker_service_pb2_grpc import add_WorkerServicer_to_server

from app.config import CONFIG
from app.grpc.characters_service import CharactersServiceImpl
from app.grpc.events_service import EventsServiceImpl
from app.grpc.servers_service import ServersServiceImpl
from app.grpc.sessions_service import SessionsServiceImpl, SignupsServiceImpl
from app.grpc.workers_service import WorkersServiceImpl

# Constants
MAX_MESSAGE_SIZE = 20 * 1024 * 1024
SSL_CERT_PATH = "/run/ssl/backend.pem"
SSL_KEY_PATH = "/run/ssl/backend.key"
SSL_CA_PATH = "/run/ssl/ca.pem"


def _create_grpc_server() -> grpc.aio.Server:
    return grpc.aio.server(
        options=[
            ("grpc.max_send_message_length", MAX_MESSAGE_SIZE),
            ("grpc.max_receive_message_length", MAX_MESSAGE_SIZE),
        ]
    )


def _register_services(server: grpc.aio.Server) -> None:
    """Register all gRPC services with the server."""
    add_CharactersServicer_to_server(CharactersServiceImpl(), server)
    add_EventsServicer_to_server(EventsServiceImpl(), server)
    add_SessionsServicer_to_server(SessionsServiceImpl(), server)
    add_SignupsServicer_to_server(SignupsServiceImpl(), server)

    add_ServersServicer_to_server(ServersServiceImpl(), server)
    add_WorkerServicer_to_server(WorkersServiceImpl(), server)


def _load_ssl_credentials() -> grpc.ServerCredentials:
    """Load SSL certificates and create server credentials."""
    with open(SSL_CERT_PATH, "rb") as f:
        cert = f.read()
    with open(SSL_KEY_PATH, "rb") as f:
        key = f.read()
    with open(SSL_CA_PATH, "rb") as f:
        root = f.read()

    return grpc.ssl_server_credentials(
        [(key, cert)],
        root_certificates=root,
        require_client_auth=True,
    )


def _configure_server_port(server: grpc.aio.Server) -> None:
    """Configure server port based on TLS and UDS settings."""
    if not CONFIG.use_tls and CONFIG.uds_path:
        server.add_insecure_port(f"unix://{CONFIG.uds_path}")
        logger.info(f"Starting UDS connection on {CONFIG.uds_path}")
    else:
        if CONFIG.secure:
            credentials = _load_ssl_credentials()
            server.add_secure_port(CONFIG.grpc_addr, credentials)
            logger.info(f"Starting secure connection on {CONFIG.grpc_addr}")
        else:
            server.add_insecure_port(CONFIG.grpc_addr)
            logger.info(f"Starting insecure connection on {CONFIG.grpc_addr}")


def _setup_signal_handlers(stop_event: asyncio.Event) -> None:
    """Set up signal handlers for graceful shutdown."""

    def signal_handler(*_):
        stop_event.set()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, signal_handler)
        except NotImplementedError:
            # Signal handlers not supported on this platform
            pass


async def serve() -> None:
    """Start and run the gRPC server."""
    server = _create_grpc_server()
    _register_services(server)
    _configure_server_port(server)

    await server.start()
    logger.info("gRPC started")

    stop_event = asyncio.Event()
    _setup_signal_handlers(stop_event)

    await stop_event.wait()
    await server.stop(grace=None)


if __name__ == "__main__":
    asyncio.run(serve())
