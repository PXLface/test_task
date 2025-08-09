from rest_framework.views import APIView
from rest_framework.response import Response
from api.filters import DDSApiFilter
from core.apps.dds.services.dds import IDDSService
from core.project.containers import get_container
from api.serializers import CreateDDSSerializer, DDSSerializer
from rest_framework.request import Request
from api.handlers import handle_dds_exceptions
from api.validators.dds_validators import validate_dds_filters


class DDSListView(APIView):
    @handle_dds_exceptions
    def get(self, request: Request):
        container = get_container()
        service: IDDSService = container.resolve(IDDSService)

        filters_data, pagination = validate_dds_filters(request=request)

        domain_filters = DDSApiFilter.to_entity_filters(filters_data)
        dds_dto = service.get_dds_list(filters=domain_filters, pagination=pagination)

        serialized_data = [DDSSerializer.from_dto(dto=dto) for dto in dds_dto]
        return Response(serialized_data)


class DDSCreateView(APIView):
    def post(self, requset: Request):
        serializer = CreateDDSSerializer(requset.data)
        dto = serializer.to_dto
        created_entity = dds_service.created_dds(dto)
        
        return Response()
        