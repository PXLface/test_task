from rest_framework import serializers

from core.apps.dds.entities.dds import DDS


class DDSSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    operation_type = serializers.CharField()
    category = serializers.CharField()
    subcategory = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    comment = serializers.CharField()
    
    @staticmethod
    def from_entity(entity: DDS) -> dict:
        return{
            'id': entity.id,
            'status': entity.status,
            'operation_type': entity.operation_type,
            'category': entity.category,
            'subcategory': entity.subcategory,
            'amount': entity.amount,
            'comment': entity.comment
        }
    