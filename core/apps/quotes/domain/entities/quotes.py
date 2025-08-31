from dataclasses import dataclass

from core.apps.quotes.domain.entities.content import Content


@dataclass
class Quote:
    id: int | None  # noqa
    content: Content
    weight: int
    quote: str
    views_count: int
    likes_count: int
    dislikes_count: int
