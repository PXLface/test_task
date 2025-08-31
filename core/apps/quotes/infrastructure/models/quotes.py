from django.db import models

from core.apps.common.models import TimeBaseModel
from core.apps.quotes.domain.entities.quotes import Quote as QuoteEntity


class QuoteModel(TimeBaseModel):
    content = models.ForeignKey(
        to='ContentModel',
        verbose_name='Произведение',
        related_name='Произведение_цитата',
        on_delete=models.CASCADE,
    )
    weight = models.IntegerField(verbose_name='Вес', default=1)
    quote = models.TextField(verbose_name='Цитата', unique=True)
    views_count = models.IntegerField('Количество просмотров', default=0)
    likes_count = models.IntegerField('Количество лайков', default=0)
    dislikes_count = models.IntegerField('Количество дизлайков', default=0)

    @classmethod
    def from_entity(cls, entity: QuoteEntity) -> 'QuoteModel':
        return cls(
            id=entity.id,
            content=entity.content,
            weight=entity.weight,
            quote=entity.quote,
            views_count=entity.views_count,
            likes_count=entity.likes_count,
            dislikes_count=entity.dislikes_count,
        )

    def to_entity(self) -> QuoteEntity:
        return QuoteEntity(
            id=self.pk,
            content=self.content,
            weight=self.weight,
            quote=self.quote,
            views_count=self.views_count,
            likes_count=self.likes_count,
            dislikes_count=self.dislikes_count,
        )

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
