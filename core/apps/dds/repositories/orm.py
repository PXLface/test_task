from django.db.models import QuerySet

from api.filters import PaginationIn
from core.apps.dds.entities.dds import DDS as DDSEntity
from core.apps.dds.filters.dds import (
    DDSFilters,
    DDSFilterSpecification,
)
from core.apps.dds.models.dds import (
    ChoiceCategory,
    ChoiceOperationType,
    ChoiceStatus,
    ChoiceSubcategory,
    DDS as DDSModel,
)
from core.apps.dds.repositories.base import IDDSRepository
from core.apps.dds.validators.infrastructure import RepositoryValidator


class ORMDDSRepository(IDDSRepository):
    """Репозиторий для обработки операций ДДС."""

    def _get_filtered_queryset(self, filters: DDSFilters) -> QuerySet:
        """Применение фильтров к запросу БД.

        Возвращает отфильтрованный QuerySet с записями ДДС.
        """
        spec = DDSFilterSpecification()
        query = spec(filters)
        return DDSModel.objects.filter(query)

    def _from_entity(self, entity: DDSEntity) -> DDSModel:
        """Конвертирует Entity в Django модель.

        В связи с наличием ForeignKey полей имеет подзапросы.
        """
        # !TODO Реализовать кэширование для получения Choices полей
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
        """Конвертирует Django модель в Entity."""
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
        filters: DDSFilters,
        pagination: PaginationIn,
    ) -> list:
        """Выдаёт список ДДС с примененными фильтрами и параметрами пагинации."""
        qs = self._get_filtered_queryset(filters=filters)[pagination.offset:pagination.offset + pagination.limit]

        return [self._to_entity(model=item) for item in qs]

    def get_dds_queryset(self, filters: DDSFilters) -> QuerySet:
        """Выдает отфильтрованный QuerySet с записями ДДС."""
        return self._get_filtered_queryset(filters=filters)

    def save(self, entity: DDSEntity) -> DDSEntity:
        """Сохраняет данные из Entity в базу данных.

        Возвращает Entity с полученным id
        """

        instance = self._from_entity(entity=entity)

        RepositoryValidator.validate_relation(instance=instance)
        RepositoryValidator.check_duplicate_opertaion(instance=instance)

        instance.save()
        entity.id = instance.id
        return entity

    def delete(self, id): # noqa
        # !TODO Удаление не реализовано в API
        ...
