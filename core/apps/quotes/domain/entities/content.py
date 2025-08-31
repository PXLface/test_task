import datetime
from dataclasses import dataclass


@dataclass
class Content:
    id: int | None  # noqa
    content_type: str
    author: str
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
