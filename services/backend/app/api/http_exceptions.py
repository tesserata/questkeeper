from fastapi import HTTPException, status


class ExpectedVersionMissing(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_428_PRECONDITION_REQUIRED,
            detail="Expected version header is missing",
        )
