from dataclasses import dataclass
from rest_framework import serializers

from core.apps.dds.filters.dds import DDSFilters

class DDSApiFilter(serializers.Serializer):
    status = serializers.CharField(required=False)
    operation_type = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    subcategory = serializers.CharField(required=False)
    date_from = serializers.DateField(required=False)
    date_to = serializers.DateField(required=False)

    def to_entity_filters(self) -> DDSFilters:
        return DDSFilters(
            status=self.get('status'),
            operation_type=self.get('operation_type'),
            category=self.get('category'),
            subcategory=self.get('subcategory'),
            date_from=self.get('date_from'),
            date_to=self.get('date_to'),
        )

@dataclass
class PaginationIn:
    offset: int = 0
    limit: int = 20
