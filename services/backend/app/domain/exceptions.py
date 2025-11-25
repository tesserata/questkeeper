class DomainError(Exception):
    """Base class for domain-specific errors."""

    pass


class ConcurrencyError(DomainError):
    def __init__(self, resource: str, id_: str, expected: int, actual: int | None = None):
        self.resource = resource
        self.id_ = id_
        self.expected = expected
        self.actual = actual
        msg = f"Concurrency conflict on {resource} {id_} (expected={expected}, actual={actual})"
        super().__init__(msg)
