from dataclasses import dataclass


@dataclass(frozen=True)
class ContentFilters:
    search: str | None = None
