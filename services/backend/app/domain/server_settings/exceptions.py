from app.domain.exceptions import DomainError


class RoleNotFound(DomainError):
    """Raised when a role mapping is not found in server settings."""

    def __init__(self, server_id: int, role_id: int) -> None:
        super().__init__(f"Role mapping for role_id {role_id} not found in server {server_id}.")
