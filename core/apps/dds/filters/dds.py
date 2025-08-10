from dataclasses import dataclass
from datetime import date

from django.db.models import Q


@dataclass(frozen=True)
class DDSFilters:
    """Фильтр для ДДС

    Не имеет поля id и created_at.

    Для фильтрации диапазоном дат по полю created_at используются
    date_from и date_to.

    Для получения записей за один день приходится указывать диапазон где:
    date_from = date_to.
    """
    status: str | None = None
    operation_type: str | None = None
    category: str | None = None
    subcategory: str | None = None
    date_from: date | None = None
    date_to: date | None = None

    @property
    def has_date(self) -> bool:
        """Показывает указан ли какой-либо диапазон дат"""
        return self.date_from is not None or self.date_to is not None


class DDSFilterSpecification:
    """Последовательно применяет все фильтры.

    Querysets are lazy.
    """
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
