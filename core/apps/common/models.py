from datetime import date

from django.db import models


class TimeBaseModel(models.Model):
    created_at = models.DateField(
        verbose_name="Дата создания",
        default=date.today,
    )

    class Meta:
        abstract = True
