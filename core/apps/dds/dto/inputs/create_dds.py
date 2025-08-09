from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from core.apps.dds.entities.dds import DDS as DDSEntity
from core.apps.dds.models.dds import ChoiceStatus


@dataclass
class CreateDDSDTO:
    status: str
    operation_type: str
    category: str
    subcategory: str
    amount: Decimal
    comment: str
    created_at: date


    def to_entity(self) -> DDSEntity:
        return DDSEntity(
            id=None,
            status=self.status,
            operation_type=self.operation_type,
            category=self.category,
            subcategory=self.subcategory,
            amount=self.amount,
            comment=self.comment,
            created_at=self.created_at
        )
