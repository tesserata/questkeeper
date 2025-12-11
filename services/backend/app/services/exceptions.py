class ServiceException(Exception):
    name: str = "ServiceException"

    def __init__(self, msg: str = "Service is unavailable"):
        self.msg = msg


class AggregateNotFoundException(ServiceException):
    name: str = "AggregateNotFoundException"

    def __init__(self, resource: str, id_: str):
        self.resource = resource
        self.id_ = id_
        msg = f"{resource} {id_} not found"
        super().__init__(msg=msg)


class ConcurrencyConflictException(ServiceException):
    name: str = "ConcurrencyConflictException"

    def __init__(self, resource: str, id_: str, expected: int):
        self.resource = resource
        self.id_ = id_
        self.expected = expected
        msg = f"Concurrency conflict on {resource} {id_} (version {expected} is not the latest)"
        super().__init__(msg=msg)


class PermissionDeniedException(ServiceException):
    name: str = "PermissionDeniedException"

    def __init__(self, resource: str, id_: str | None = None):
        self.resource = resource
        self.id_ = id_ if id_ else ""
        msg = f"Permission denied on {resource} {id_}"
        super().__init__(msg=msg)


class RequiredRoleMissingException(ServiceException):
    name: str = "RequiredRoleMissingException"

    def __init__(self, role: str):
        self.role = role
        msg = f"Required role missing: {role}"
        super().__init__(msg=msg)
