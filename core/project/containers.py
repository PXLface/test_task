from functools import lru_cache

import punq

from core.apps.quotes.application.services import (
    BaseContentService,
    ORMContentService,
)


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    container.register(BaseContentService, ORMContentService)

    return container
