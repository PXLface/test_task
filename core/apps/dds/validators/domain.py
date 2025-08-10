from decimal import Decimal

from django.forms import ValidationError


class DDSDomainValidator:
    """Базовые доменные проверки"""

    @staticmethod
    def validate_positive_amount(amount: Decimal):
        if amount <= 0:
            raise ValidationError({
                "field": "amount",
                "message": "Сумма должна быть положительной",
            })
