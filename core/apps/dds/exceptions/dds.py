from dataclasses import dataclass
from typing import Optional

@dataclass
class DDSDomainError(Exception):
    message: str
    details: Optional[dict] = None
    http_status_code: int = 400


class InvalidPaginationError(DDSDomainError):
    def __init__(self, details: dict):
        super().__init__(
            message="Invalid pagination parameters",
            details=details,
            http_status_code=400
        )

class DDSServerError(DDSDomainError):
    def __init__(self, details: str):
        super().__init__(
            message="Iternal server error",
            details={"error": details},
            http_status_code=500
        )
