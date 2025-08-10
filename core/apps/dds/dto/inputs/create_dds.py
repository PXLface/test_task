from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from core.apps.dds.entities.dds import DDS as DDSEntity


@dataclass
class CreateDDSDTO:
    """DTO для создания новой записи ДДС"""
    id: int | None # noqa
    status: str
    operation_type: str
    category: str
    subcategory: str
    amount: Decimal
    comment: str
    created_at: date

    def to_entity(self) -> DDSEntity:
        """Преобразует DTO в Domain Entity ДДС"""
        return DDSEntity(
            id=None,
            status=self.status,
            operation_type=self.operation_type,
            category=self.category,
            subcategory=self.subcategory,
            amount=self.amount,
            comment=self.comment,
            created_at=self.created_at,
        )
