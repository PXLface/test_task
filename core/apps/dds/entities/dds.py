from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class DDS:
    """Сущность ДДС (Движения денежных средств), представляющая базовую модель данных.

    Поля operation_type, category, subcategory, amount обязательны.

    Имеются связанные поля:
    operation_type -> category -> subcategory
    """
    id: int # noqa
    status: str
    operation_type: str
    category: str
    subcategory: str
    amount: Decimal
    comment: str
    created_at: date
