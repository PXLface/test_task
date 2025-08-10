from typing import Dict

from rest_framework import serializers

from core.apps.dds.dto.inputs.create_dds import CreateDDSDTO
from core.apps.dds.dto.outputs.get_dds import DDSResponseDTO


class DDSSerializer(serializers.Serializer):
    """Сериализатор для данных при работе с ДДС."""
    id = serializers.IntegerField() # noqa
    status = serializers.CharField()
    operation_type = serializers.CharField()
    category = serializers.CharField()
    subcategory = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    comment = serializers.CharField()
    created_at = serializers.DateField()

    @staticmethod
    def from_dto(dto: DDSResponseDTO) -> dict:
        """Конвертирует DTO в словарь, пригодный для сериализации в JSON."""
        return {
            'id': dto.id,
            'status': dto.status,
            'operation_type': dto.operation_type,
            'category': dto.category,
            'subcategory': dto.subcategory,
            'amount': dto.amount,
            'comment': dto.comment,
            'created_at': dto.created_at,
        }


class CreateDDSSerializer(serializers.Serializer):
    """Сериализатор при создании DDS.

    Поле id необязательно так как генерируется БД.
    """
    id = serializers.IntegerField(required=False) # noqa
    status = serializers.CharField()
    operation_type = serializers.CharField()
    category = serializers.CharField()
    subcategory = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    comment = serializers.CharField()
    created_at = serializers.DateField()

    def to_dto(self) -> CreateDDSDTO:
        """Преобразует валидированные данные в DTO для передачи в сервисный слой."""
        return CreateDDSDTO(
            id=None,
            status=self.validated_data['status'],
            operation_type=self.validated_data['operation_type'],
            category=self.validated_data['category'],
            subcategory=self.validated_data['subcategory'],
            amount=self.validated_data['amount'],
            comment=self.validated_data['comment'],
            created_at=self.validated_data['created_at'],
        )

    @staticmethod
    def from_dto(dto: CreateDDSDTO) -> Dict:
        """Конвертирует DTO в словарь для сериализации в API.

        Преобразует Decimal в строку для безопасной JSON сериализации.
        """
        return {
            'id': dto.id,
            'status': dto.status,
            'operation_type': dto.operation_type,
            'category': dto.category,
            'subcategory': dto.subcategory,
            'amount': str(dto.amount),
            'comment': dto.comment,
            'created_at': dto.created_at,
        }
