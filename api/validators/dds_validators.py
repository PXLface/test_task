

from decimal import Decimal

from django.forms import ValidationError
from rest_framework.request import Request


class DDSInputValidator:
    """Базовый валидатор для входных данных API."""

    @staticmethod
    def validate_amount(value: str):
        """Валидация суммы."""
        if value is not None:
            if Decimal(value=value) <= 0:
                raise ValidationError({
                    "field": "amount",
                    "message": "Сумма должна быть положительной",
                })

    @staticmethod
    def validate_dates(request: Request):
        """Валидация интервала поиска дат."""
        if 'date_from' in request.query_params and 'date_to' in request.query_params:
            if request.query_params.get('date_from') > request.query_params.get('date_to'):
                raise ValidationError({
                    "message": "Некорректный интервал",
                    "fields": ["date_from", "date_to"],
                })
