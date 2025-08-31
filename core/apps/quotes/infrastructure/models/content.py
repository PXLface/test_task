from django.db import models

from core.apps.common.models import TimeBaseModel
from core.apps.quotes.domain.entities.content import Content as ContentEntity


class ContentModel(TimeBaseModel):
    content_type = models.CharField(verbose_name='Вид', max_length=50)
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание')
    author = models.CharField(verbose_name='Автор', max_length=50)

    @classmethod
    def from_entity(cls, entity: ContentEntity) -> 'ContentModel':
        return cls(
            pk=entity.id,
            content_type=entity.content_type,
            author=entity.author,
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> ContentEntity:
        return ContentEntity(
            id=self.pk,
            content_type=self.content_type,
            author=self.author,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        unique_together = [
            ('title', 'author'),
        ]
