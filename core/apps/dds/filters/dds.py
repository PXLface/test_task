from dataclasses import dataclass
from datetime import date

from django.db.models import Q


@dataclass(frozen=True)
class DDSFilters:
    status: str | None = None
    operation_type: str | None = None
    category: str | None = None
    subcategory: str | None = None
    date_from: date | None = None
    date_to: date | None = None

    @property
    def has_status(self) -> bool:
        return self.status is not None

    @property
    def has_operation_type(self) -> bool:
        return self.operation_type is not None

    @property
    def has_category(self) -> bool:
        return self.category is not None

    @property
    def has_subcategory(self) -> bool:
        return self.subcategory is not None

    @property
    def has_date(self) -> bool:
        return self.date_from is not None or self.date_to is not None


class DDSFilterSpecification:
    def __call__(self, filters: DDSFilters) -> Q:
        query = Q()

        if filters.status:
            query &= Q(status=filters.status)

        if filters.operation_type:
            query &= Q(operation_type=filters.operation_type)

        if filters.category:
            query &= Q(category=filters.category)

        if filters.subcategory:
            query &= Q(subcategory=filters.subcategory)

        if filters.has_date:
            if filters.date_from and filters.date_to:
                query &= Q(created_at__range=[filters.date_from, filters.date_to])
            else:
                if filters.date_from:
                    query &= Q(created_at__gte=filters.date_from)
                if filters.date_to:
                    query &= Q(created_at__lte=filters.date_to)

        return query
