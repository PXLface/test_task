from abc import ABC
from dataclasses import dataclass
from typing import Iterable

from core.apps.dds.dto.inputs.create_dds import CreateDDSDTO
from core.apps.dds.dto.outputs.get_dds import DDSResponseDTO
from core.apps.dds.filters.dds import DDSFilters
from core.apps.dds.repositories.base import IDDSRepository
from core.apps.dds.validators.domain import DDSDomainValidator


@dataclass
class IGETDDS(ABC):
    @staticmethod
    def get_dds_list(self, filters: DDSFilters, pagination):
        ...


@dataclass
class ICreateDDS(ABC):
    """Интерфейс для операций создания записей ДДС."""
    @staticmethod
    def create_dds(self, dto: CreateDDSDTO) -> CreateDDSDTO:
        """Создаёт новую запись ДДС.

        Возвращает созданный DTO с зарегестрированным ID в базе данных
        """
        ...


class GetDDSService(IGETDDS):
    """Сервис для получения данных ДДС."""

    def __init__(self, repository: IDDSRepository):
        self._repository = repository

    def get_dds_list(self, filters: DDSFilters, pagination) -> Iterable[DDSResponseDTO]:
        """Реализация получения списка ДДС.

        Получает данные из репозитория и преобразует их в DTO.
        """
        entity = self._repository.get_dds_list(filters=filters, pagination=pagination)
        return [DDSResponseDTO.from_entity(entity=items) for items in entity]


class CreateDDSSErvice(ICreateDDS):
    """Сервис для создания записей ДДС"""

    def __init__(self, repository: IDDSRepository):
        self._repository = repository

    def create_dds(self, dto: CreateDDSDTO) -> CreateDDSDTO:
        """Реализация создания записи ДДС.

        Преобразует DTO в сущность, сохраняет с возвращением обновленного DTO
        """
        entity = dto.to_entity()

        DDSDomainValidator.validate_positive_amount(amount=entity.amount)

        self._repository.save(entity=entity)
        dto.id = entity.id
        return dto
