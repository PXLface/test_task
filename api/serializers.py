from rest_framework import serializers

from core.apps.dds.dto.inputs.create_dds import CreateDDSDTO
from core.apps.dds.dto.outputs.get_dds import DDSResponseDTO


class DDSSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    operation_type = serializers.CharField()
    category = serializers.CharField()
    subcategory = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    comment = serializers.CharField()
    created_at = serializers.DateField()
    
    @staticmethod
    def from_dto(dto: DDSResponseDTO) -> dict:
        return{
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
    status = serializers.CharField()
    operation_type = serializers.CharField()
    category = serializers.CharField()
    subcategory = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    comment = serializers.CharField()
    created_at = serializers.DateField()

    def to_dto(self) -> CreateDDSDTO:
        return CreateDDSDTO(
            status=self.validated_data['status'],
            operation_type=self.validated_data['operation_type'],
            category=self.validated_data['category'],
            subcategory=self.validated_data['subcategory'],
            amount=self.validated_data['amount'],
            comment=self.validated_data['comment'],
            created_at=self.validated_data['created_at'],
        )