from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import (
    DDSApiFilter,
    PaginationIn,
)
from api.handlers import handle_dds_exceptions
from api.serializers import (
    CreateDDSSerializer,
    DDSSerializer,
)
from api.validators.dds_validators import DDSInputValidator
from core.apps.dds.services.dds import (
    ICreateDDS,
    IGETDDS,
)
from core.project.containers import get_container


class DDSListView(APIView):
    """APIView получает записи ДДС с фильтрацией и пагинацией.

    Сейчас исправно применяет фильтры и пагинацию, НО
    по пути http://127.0.0.1:8000/api/v1/dds нет полей для ввода фильтров и пагинации
    """
    # !TODO Изменить APIView для удобного ввода фильтров и пагинации
    @handle_dds_exceptions
    def get(self, request: Request):
        container = get_container()
        service: IGETDDS = container.resolve(IGETDDS)

        filter_serializer = DDSApiFilter(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        DDSInputValidator.validate_amount(value=request.query_params.get('amount'))
        DDSInputValidator.validate_dates(request=request)

        pagination = PaginationIn(
            offset=int(request.query_params.get('offset', 0)),
            limit=min(int(request.query_params.get('limit', 20)), 100),
        )

        domain_filters = filter_serializer.to_entity_filters()
        dds_dto = service.get_dds_list(filters=domain_filters, pagination=pagination)

        serialized_data = [DDSSerializer.from_dto(dto=dto) for dto in dds_dto]
        return Response(serialized_data)


class DDSCreateView(APIView):
    """APIView для создание новых записей ДДС."""
    def get(self, request: Request):
        """Выдает один и тот же пример ДДС для создания"""
        # !TODO Вывести вывод примера ввода в отдельный сервис
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
        """Создаёт запись в БД из полученных данных ДДС.

        Возвращает запись ДДС из БД с полученным id.

        Raises:
            400 BadRequest: невалидные данные.
            500 Server Error: проблема с сохранением.
        """
        container = get_container()
        service: ICreateDDS = container.resolve(ICreateDDS)

        validated_data = request.data

        DDSInputValidator.validate_amount(value=validated_data.get("amount"))

        serializer = CreateDDSSerializer(data=validated_data)
        serializer.is_valid(raise_exception=True)

        dto = serializer.to_dto()
        created_data = service.create_dds(dto)

        return Response(CreateDDSSerializer.from_dto(created_data))
