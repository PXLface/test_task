from rest_framework.views import APIView
from rest_framework.response import Response
from .filters import DDSApiFilter, PaginationIn
from core.apps.dds.filters.dds import DDSFilters as DDSFiltersEntity
from core.apps.dds.repositories.base import IDDSRepository
from core.project.containers import get_container
from rest_framework import status
from api.serializers import DDSSerializer
import logging

logger = logging.getLogger(__name__)

class DDSListView(APIView):
    def get(self, request):
        try:
            container = get_container()
            service: IDDSRepository = container.resolve(IDDSRepository)

            api_filter = DDSApiFilter(data=request.query_params)
            if not api_filter.is_valid():
                return Response(
                    {"error": "Invalid filters", "details": api_filter.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )

            try:
                pagination = PaginationIn(
                    offset=int(request.query_params.get('offset', 0)),
                    limit=int(request.query_params.get('limit', 20))
                )
            except ValueError as e:
                return Response(
                    {"error": "Invalid pagination parameters", "details": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )

            domain_filters = DDSFiltersEntity(
                status=api_filter.validated_data.get('status'),
                operation_type=api_filter.validated_data.get('operation_type'),
                category=api_filter.validated_data.get('category'),
                subcategory=api_filter.validated_data.get('subcategory'),
                date_from=api_filter.validated_data.get('date_from'),
                date_to=api_filter.validated_data.get('date_to'),
            )

            dds_entities = service.get_dds_list(
                filters=domain_filters,
                pagination=pagination
            )
            
            serialized_data = [
                DDSSerializer.from_entity(entity)
                for entity in dds_entities
            ]
            
            return Response(serialized_data)
            
        except Exception as e:
            logger.error(f"DDS API Error: {str(e)}", exc_info=True)
            return Response(
                {"error": "Server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )