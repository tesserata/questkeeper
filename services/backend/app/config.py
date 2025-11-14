from pydantic_settings import BaseSettings


class Config(BaseSettings):
    db_dsn: str = "postgresql+asyncpg://qk_admin:password@db:5432/questkeeper"

    # Redis
    redis_url: str = "redis://redis:6379/0"

    # gRPC bind
    uds_path: str = "/tmp/qk_domain.sock"
    grpc_addr: str = "[::]:50051"
    use_tls: bool = True
    secure: bool = False
    ca_path: str | None = None
    cert_path: str | None = None
    key_path: str | None = None

    otlp_endpoint: str | None = None


CONFIG = Config()
