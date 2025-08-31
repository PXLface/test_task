from datetime import datetime

from pydantic import BaseModel

from core.apps.quotes.domain.entities.content import Content as ContentEntity


class ContentSchema(BaseModel):
    id: int  # noqa
    content_type: str
    author: str
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity: ContentEntity) -> 'ContentSchema':
        return cls(
            id=entity.id,
            content_type=entity.content_type,
            author=entity.author,
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> ContentEntity:
        return ContentEntity(
            id=self.id,
            content_type=self.content_type,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
