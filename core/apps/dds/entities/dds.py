from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class DDS:
    id: int
    status: str
    operation_type: str
    category: str
    subcategory: str
    amount: Decimal
    comment: str
    created_at: date
