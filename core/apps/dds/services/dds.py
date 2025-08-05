from abc import ABC, abstractmethod
from typing import Iterable

from django.db.models import Q

class IDDSService(ABC):
    @abstractmethod
    def get_dds_list():
        ...
