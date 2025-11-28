class DomainError(Exception):
    """Base class for domain-specific errors."""

    pass


class ConcurrencyError(DomainError):
    def __init__(self, resource: str, id_: str, expected: int):
        self.resource = resource
        self.id_ = id_
        self.expected = expected
        msg = f"Concurrency conflict on {resource} {id_} (version {expected} is not the latest version)"
        super().__init__(msg)
