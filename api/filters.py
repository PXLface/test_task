from dataclasses import dataclass


@dataclass
class PaginationIn:
    offset: int = 0
    limit: int = 20
