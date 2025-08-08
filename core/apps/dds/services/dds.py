from abc import ABC, abstractmethod
from typing import Iterable

from django.db.models import QuerySet

from api.filters import PaginationIn
from core.apps.dds.entities.dds import DDS as DDSEntity
from core.apps.dds.filters.dds import DDSFilterSpecification, DDSFilters
from core.apps.dds.models.dds import DDS as DDSModel


class IDDSService(ABC):
    @abstractmethod
    def get_dds_list(
        self,
        filters: DDSFilters,
        pagination: PaginationIn,
    ) -> Iterable[DDSEntity]:
        ...


class ORMDDSService(IDDSService):
    def _get_filtered_queryset(self, filters:DDSFilters) -> QuerySet:
        query = DDSFilterSpecification(filters=filters)
        return DDSModel.objects.filter(query)

    def get_dds_list(
        self,
        filters:DDSFilters,
        pagination:PaginationIn
    ) -> Iterable[DDSEntity]:
        qs = self._get_filtered_queryset(filters=filters)[pagination.offset:pagination.offset + pagination.limit]

        return [item.to_entity() for item in qs]

    def get_dds_queryset(self, filters:DDSFilters) -> QuerySet:
        return self._get_filtered_queryset(filters=filters)
