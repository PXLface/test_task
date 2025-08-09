from abc import ABC
from dataclasses import dataclass
from typing import Iterable
from core.apps.dds.dto.inputs.create_dds import CreateDDSDTO
from core.apps.dds.dto.outputs.get_dds import DDSResponseDTO
from core.apps.dds.entities.dds import DDS as DDSEntity
from core.apps.dds.filters.dds import DDSFilters
from core.apps.dds.repositories.base import IDDSRepository


@dataclass
class IGETDDS(ABC):
    @staticmethod
    def get_dds_list(self, filters: DDSFilters, pagination):
        ...
    

@dataclass
class ICreateDDS(ABC):
    @staticmethod
    def create_dds(self, dto: CreateDDSDTO):
        ...


class GetDDSService(IGETDDS):
    def __init__(self, repository: IDDSRepository):
        self._repository = repository

    def get_dds_list(self, filters: DDSFilters, pagination) -> Iterable[DDSResponseDTO]:
        entity = self._repository.get_dds_list(filters=filters, pagination=pagination)
        return [DDSResponseDTO.from_entity(entity=items) for items in entity]




class CreateDDSSErvice(ICreateDDS):
    def __init__(self, repository: IDDSRepository):
        self._repository = repository

    def create_dds(self, dto: CreateDDSDTO) -> DDSEntity:
        entity = dto.to_entity()


        return self._repository.save(entity=entity)
