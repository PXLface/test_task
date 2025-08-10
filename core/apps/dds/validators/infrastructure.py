from django.forms import ValidationError

from core.apps.dds.models.dds import DDS


class RepositoryValidator:
    """Проверки на уровне репозиторий"""

    @staticmethod
    def check_duplicate_opertaion(instance: DDS):

        if DDS.objects.filter(
            operation_type=instance.operation_type,
            category=instance.category,
            amount=instance.amount,
            created_at=instance.created_at,
        ).exists():
            raise ValidationError("Дублирующая операция")

    @staticmethod
    def validate_relation(instance: DDS):
        if (
            instance.subcategory.category != instance.category or
            instance.category.operation_type != instance.operation_type
        ):
            raise ValidationError(
                "Нарушена связь: тип операции -> категория -> подкатегория",
            )
