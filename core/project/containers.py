import punq

from core.apps.dds.repositories.base import IDDSRepository
from core.apps.dds.repositories.orm import ORMDDSRepository

def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    container.register(IDDSRepository, ORMDDSRepository)

    return container