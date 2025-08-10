from django.db import models

from smart_selects.db_fields import ChainedForeignKey

from core.apps.common.models import TimeBaseModel


class DDS(TimeBaseModel):
    """Модель движения денежных средств (ДДС).

    Тип операции, категория и подкатегория связаны через ChainedForeignKey.
    Тип операции -> категория, категория -> подкатегория.
    """
    status = models.ForeignKey(
        "ChoiceStatus",
        verbose_name="Статус",
        on_delete=models.PROTECT,
        blank=True,
    )
    operation_type = models.ForeignKey(
        "ChoiceOperationType",
        verbose_name="Тип операции",
        on_delete=models.PROTECT,
        blank=False,
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
        blank=False,
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        blank=True,
    )

    class Meta:
        verbose_name = 'Движение денежных средств'
        verbose_name_plural = 'Движения денежных средств'


class ChoiceStatus(models.Model):
    choice_value = models.CharField("Статус", max_length=50)

    def __str__(self) -> str:
        return self.choice_value

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class ChoiceOperationType(models.Model):
    choice_value = models.CharField("Тип операции", max_length=50)

    def __str__(self) -> str:
        return self.choice_value

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class ChoiceCategory(models.Model):
    choice_value = models.CharField("Категория", max_length=50)
    operation_type = models.ForeignKey(
        "ChoiceOperationType",
        verbose_name='Тип операции',
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return self.choice_value

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ChoiceSubcategory(models.Model):
    choice_value = models.CharField("Подкатегория", max_length=50)
    category = models.ForeignKey(
        "ChoiceCategory",
        verbose_name="Категория",
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return self.choice_value

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
