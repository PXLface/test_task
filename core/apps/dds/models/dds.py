from django.db import models

from smart_selects.db_fields import ChainedForeignKey

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
    category = ChainedForeignKey(
        "ChoiceCategory",
        verbose_name="Категория",
        chained_field="operation_type",
        chained_model_field="operation_type",
        show_all=False,
        on_delete=models.PROTECT,
        blank=False,
    )
    subcategory = ChainedForeignKey(
        "ChoiceSubcategory",
        verbose_name="Подкатегория",
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        on_delete=models.PROTECT,
        blank=False,
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
            status=self.status.status_choice,
            operation_type=self.operation_type.operation_type_choice,
            category=self.category.category_choice,
            subcategory=self.subcategory.subcategory_choice,
            amount=self.amount,
            comment=self.comment,
            created_at=self.created_at,
        )

    class Meta:
        verbose_name = 'Движение денежных средств'
        verbose_name_plural = 'Движения денежных средств'


class ChoiceStatus(models.Model):
    status_choice = models.CharField("Статус", max_length=50)

    def __str__(self) -> str:
        return self.status_choice

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class ChoiceOperationType(models.Model):
    operation_type_choice = models.CharField("Тип операции", max_length=50)

    def __str__(self) -> str:
        return self.operation_type_choice

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class ChoiceCategory(models.Model):
    category_choice = models.CharField("Категория", max_length=50)
    operation_type = models.ForeignKey(
        "ChoiceOperationType",
        verbose_name='Тип операции',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.category_choice

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ChoiceSubcategory(models.Model):
    subcategory_choice = models.CharField("Подкатегория", max_length=50)
    category = models.ForeignKey(
        "ChoiceCategory",
        verbose_name="Категория",
        on_delete=models.PROTECT
    )
    
    def __str__(self) -> str:
        return self.subcategory_choice

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
