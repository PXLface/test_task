from typing import Optional, Type
from django.db.models import QuerySet, Model

from api.filters import PaginationIn
from core.apps.dds.filters.dds import DDSFilterSpecification, DDSFilters
from core.apps.dds.models.dds import DDS as DDSModel, ChoiceStatus, ChoiceCategory, ChoiceOperationType, ChoiceSubcategory
from core.apps.dds.repositories.base import IDDSRepository
from core.apps.dds.entities.dds import DDS as DDSEntity

class ORMDDSRepository(IDDSRepository):
    def _get_filtered_queryset(self, filters:DDSFilters) -> QuerySet:
        spec = DDSFilterSpecification()
        query = spec(filters)
        return DDSModel.objects.filter(query)
    
    def _from_entity(self, entity: DDSEntity) -> DDSModel:
        """Convert Domain Entity to Database Model"""
        return DDSModel(
            id=entity.id,
            status=ChoiceStatus.objects.get(choice_value=entity.status),
            operation_type=ChoiceOperationType.objects.get(choice_value=entity.operation_type),
            category=ChoiceCategory.objects.get(choice_value=entity.category),
            subcategory=ChoiceSubcategory.objects.get(choice_value=entity.subcategory),
            amount=entity.amount,
            comment=entity.comment,
            created_at=entity.created_at,
        )

    def _to_entity(self, model: DDSModel) -> DDSEntity:
        return DDSEntity(
            id=model.id,
            status=model.status.choice_value,
            operation_type=model.operation_type.choice_value,
            category=model.category.choice_value,
            subcategory=model.subcategory.choice_value,
            amount=model.amount,
            comment=model.comment,
            created_at=model.created_at,
        )

    def get_dds_list(
        self,
        filters:DDSFilters,
        pagination:PaginationIn
    ) -> list:
        qs = self._get_filtered_queryset(filters=filters)[pagination.offset:pagination.offset + pagination.limit]

        return [self._to_entity(model=item) for item in qs]

    def get_dds_queryset(self, filters:DDSFilters) -> QuerySet:
        return self._get_filtered_queryset(filters=filters)

    def save(self, entity: DDSEntity) -> DDSEntity:
        model = self._from_entity(entity=entity)
        model.save()
        return entity
    
    def delete(self, id):
        ...
