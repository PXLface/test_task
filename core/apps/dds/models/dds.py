from django.db import models

from core.apps.common.models import TimeBaseModel
from core.apps.dds.entities.dds import DDS as DDSEntity

class DDS(TimeBaseModel):
    status = models.ForeignKey(
        "ChoiceStatus",
        verbose_name="Статус",
        on_delete=models.PROTECT,
        blank=True
    )
    operation_type = models.ForeignKey(
        "ChoiceOperationType",
        verbose_name="Тип операции",
        on_delete=models.PROTECT,
        blank=False
    )
    category = models.ForeignKey(
        "ChoiceCategory",
        verbose_name="Категория",
        on_delete=models.PROTECT,
        blank=False
    )
    subcategory = models.ForeignKey(
        "ChoiceSubcategory",
        verbose_name="Подкатегория",
        on_delete=models.PROTECT,
        blank=False
    )
    amount = models.DecimalField(
        verbose_name="Сумма",
        max_digits=12,
        decimal_places=2,
        blank=False
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        blank=True
    )
    
    def to_entity(self) -> DDSEntity:
        return DDSEntity(
            id=self.id,
            status=self.status,
            operation_type=self.operation_type,
            category=self.category,
            subcategory=self.subcategory,
            amount=self.amount,
            comment=self.comment,
            created_at=self.created_at,
        )

    class Meta:
        verbose_name = 'Движение денежных средств'


class ChoiceStatus(models.Model):
    status_choice = models.CharField("Выбор статуса", max_length=50)


class ChoiceOperationType(models.Model):
    operation_type_choice = models.CharField("Выбор типа операции", max_length=50)


class ChoiceCategory(models.Model):
    category_choice = models.CharField("Выбор категории", max_length=50)


class ChoiceSubcategory(models.Model):
    subcategory_choice = models.CharField("Выбор подкатегории", max_length=50)
