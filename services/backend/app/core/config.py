from pydantic_settings import BaseSettings

class Config(BaseSettings):
    pg_dsn: str = "postgresql+asyncpg://backend:backend@postgres/backend"

    # Redis
    redis_url: str = "redis://redis:6379/0"

    # gRPC bind
    uds_path: str = "/tmp/qk_domain.sock"
    grpc_addr: str = "[::]:50051"
    use_tls: bool = False
    ca_path: str | None = None
    cert_path: str | None = None
    key_path: str | None = None

    otlp_endpoint: str | None = None

CONFIG = Config()
