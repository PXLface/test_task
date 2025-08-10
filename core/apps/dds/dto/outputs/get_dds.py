from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from core.apps.dds.entities.dds import DDS as DDSEntity


@dataclass
class DDSResponseDTO:
    """DTO для выдачи ДДС в GET запросе"""
    id: int # noqa
    status: str
    operation_type: str
    category: str
    subcategory: str
    amount: Decimal
    comment: str
    created_at: date

    @classmethod
    def from_entity(cls, entity: DDSEntity):
        """Конвертирует Domain Entity в DTO"""
        return cls(
            id=entity.id,
            status=entity.status,
            operation_type=entity.operation_type,
            category=entity.category,
            subcategory=entity.subcategory,
            amount=entity.amount,
            comment=entity.comment,
            created_at=entity.created_at,
        )
