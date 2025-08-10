from datetime import date

from django.db import models


class TimeBaseModel(models.Model):
    """Модель с готовым полем created_at.

    Как для тестового задания не является полезной и обязательной.
    Добавлена как common модель если необходимо добавить какую-то модель с created_at
    """
    created_at = models.DateField(
        verbose_name="Дата создания",
        default=date.today,
    )

    class Meta:
        abstract = True
