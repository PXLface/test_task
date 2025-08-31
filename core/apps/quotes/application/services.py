from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.apps.quotes.application.exceptions import ContentNotFound
from core.apps.quotes.domain.entities.content import Content
from core.apps.quotes.infrastructure.filters import ContentFilters
from core.apps.quotes.infrastructure.models.content import ContentModel


class BaseContentService(ABC):
    @abstractmethod
    def get_content_list(
        self,
        filters: ContentFilters,
        pagination: PaginationIn,
    ) -> Iterable[Content]:
        ...

    @abstractmethod
    def get_content_count(self, filters: ContentFilters) -> int:
        ...

    @abstractmethod
    def get_by_id(self, content_id: int) -> int:
        ...

    @abstractmethod
    def get_all_content(self) -> Iterable[Content]:
        ...


class ORMContentService(BaseContentService):
    def _build_content_query(self, filters: ContentFilters) -> Q:
        query = Q()

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search,
            )

        return query

    def get_content_list(
        self,
        filters: ContentFilters,
        pagination: PaginationIn,
    ) -> Iterable[Content]:
        query = self._build_content_query(filters=filters)
        qs = ContentModel.objects.filter(query)[
            pagination.offset:pagination.offset + pagination.limit
        ]

        return [content.to_entity() for content in qs]

    def get_content_count(self, filters: ContentFilters) -> int:
        query = self._build_content_query(filters=filters)

        return ContentModel.objects.filter(query).count()

    def get_by_id(self, content_id):
        try:
            content_dto = ContentModel.objects.get(pk=content_id)
        except ContentModel.DoesNotExist:
            raise ContentNotFound()

        return content_dto.to_entity()

    def get_all_content(self) -> Iterable[Content]:
        query = self._build_content_query[ContentFilters()]
        queryset = ContentModel.objects.filter(query)

        for content in queryset:
            yield content.to_entity()
