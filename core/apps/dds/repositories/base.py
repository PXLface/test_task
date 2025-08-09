from abc import ABC, abstractmethod
from dataclasses import dataclass
from django.db.models import QuerySet
from api.filters import PaginationIn
from core.apps.dds.entities.dds import DDS as DDSEntity
from core.apps.dds.filters.dds import DDSFilters


@dataclass
class IDDSRepository(ABC):
    @abstractmethod
    def get_dds_list(
        self,
        filters: DDSFilters,
        pagination: PaginationIn,
    ) -> list:
        ...

    @abstractmethod
    def get_dds_queryset(self, filters:DDSFilters) -> QuerySet:
        ...

    @abstractmethod
    def save(self, entity: DDSEntity) -> DDSEntity:
        ...

    @abstractmethod
    def delete(self, id: int) -> None:
        ...