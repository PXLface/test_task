from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from core.apps.dds.entities.dds import DDS as DDSEntity


@dataclass
class CreateDDSDTO:
    status: str
    operation_type: str
    category: str
    subcategory: str
    amount: Decimal
    comment: str
    created_at: date


    @classmethod
    def to_entity(cls) -> DDSEntity:
        return DDSEntity(
            status=cls.status,
            operation_type=cls.operation_type,
            category=cls.category,
            subcategory=cls.subcategory,
            amount=cls.amount,
            comment=cls.comment,
            created_at=cls.created_at
        )
