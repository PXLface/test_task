from django.db.models import QuerySet

from api.filters import PaginationIn
from core.apps.dds.filters.dds import DDSFilterSpecification, DDSFilters
from core.apps.dds.models.dds import DDS as DDSModel
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
            status=entity.status,
            operation_type=entity.operation_type,
            category=entity.category,
            subcategory=entity.subcategory,
            amount=entity.amount,
            created_at=entity.created_at,
        )

    def _to_entity(self, model: DDSModel) -> DDSEntity:
        return DDSEntity(
            id=model.id,
            status=model.status.status_choice,
            operation_type=model.operation_type.operation_type_choice,
            category=model.category.category_choice,
            subcategory=model.subcategory.subcategory_choice,
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