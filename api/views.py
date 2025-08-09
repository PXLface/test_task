from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import DDSApiFilter
from api.handlers import handle_dds_exceptions
from api.serializers import (
    CreateDDSSerializer,
    DDSSerializer,
)
from api.validators.dds_validators import validate_dds_filters
from core.apps.dds.services.dds import (
    ICreateDDS,
    IGETDDS,
)
from core.project.containers import get_container


class DDSListView(APIView):
    @handle_dds_exceptions
    def get(self, request: Request):
        container = get_container()
        service: IGETDDS = container.resolve(IGETDDS)

        filters_data, pagination = validate_dds_filters(request=request)

        domain_filters = DDSApiFilter.to_entity_filters(filters_data)
        dds_dto = service.get_dds_list(filters=domain_filters, pagination=pagination)

        serialized_data = [DDSSerializer.from_dto(dto=dto) for dto in dds_dto]
        return Response(serialized_data)


class DDSCreateView(APIView):
    def get(self, request: Request):
        return Response({
            "status": "Бизнес",
            "operation_type": "Пополнение",
            "category": "Инфраструктура",
            "subcategory": "Proxy",
            "amount": "2340.43",
            "comment": "3123123",
            "created_at": "2025-04-11",
        })

    def post(self, request: Request):
        container = get_container()
        service: ICreateDDS = container.resolve(ICreateDDS)

        validated_data = request.data

        serializer = CreateDDSSerializer(data=validated_data)
        serializer.is_valid(raise_exception=True)

        dto = serializer.to_dto()
        created_data = service.create_dds(dto)

        return Response(CreateDDSSerializer.from_dto(created_data))
