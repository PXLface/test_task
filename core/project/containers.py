import punq

from core.apps.dds.repositories.base import IDDSRepository
from core.apps.dds.repositories.orm import ORMDDSRepository
from core.apps.dds.services.dds import IGETDDS, GetDDSService, ICreateDDS, CreateDDSSErvice


def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    container.register(IDDSRepository, ORMDDSRepository)
    container.register(IGETDDS, GetDDSService)
    container.register(ICreateDDS, CreateDDSSErvice)

    return container