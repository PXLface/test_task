from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Dict,
    Tuple,
)

from rest_framework import status
from rest_framework.request import Request

from api.filters import (
    DDSApiFilter,
    PaginationIn,
)
from core.apps.dds.exceptions.dds import (
    DDSDomainError,
    InvalidPaginationError,
)


def validate_dds_filters(request: Request) -> Tuple[dict, PaginationIn]:
    validator = DDSApiValidator()
    filters = validator.validate_filters(request=request)
    pagination = validator.validate_pagination(request=request)

    return filters, pagination


class IDDSApiValidator(ABC):
    @abstractmethod
    def validate_filters(self, request: Request) -> Dict[str, Any]:
        ...

    @abstractmethod
    def validate_pagination(self, request: Request) -> PaginationIn:
        ...


class DDSApiValidator(IDDSApiValidator):
    def validate_filters(self, request: Request) -> Dict[str, Any]:
        api_filter = DDSApiFilter(data=request.query_params)
        if not api_filter.is_valid():
            raise DDSDomainError(
                message="Invalid filters",
                details=api_filter.errors,
                http_status_code=status.HTTP_400_BAD_REQUEST,
            )
        return api_filter.validated_data

    def validate_pagination(self, request: Request) -> PaginationIn:
        try:
            return PaginationIn(
                offset=int(request.query_params.get('offset', 0)),
                limit=int(request.query_params.get('limit', 20)),
            )
        except ValueError as e:
            raise InvalidPaginationError(details={"error": str(e)})
