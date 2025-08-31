from django.http import HttpRequest

from ninja import (
    Query,
    Router,
)

from core.api.filters import (
    PaginationIn,
    PaginationOut,
)
from core.api.schemas import (
    ApiResponse,
    ListPaginatedResponse,
)
from core.api.v1.content.filters import ContentFilters
from core.api.v1.content.schemas import ContentSchema
from core.apps.quotes.application.services import BaseContentService
from core.apps.quotes.infrastructure.filters import ContentFilters as ContentFiltersEntity
from core.project.containers import get_container


router = Router(tags=['Content'])


@router.get('', response=ApiResponse[ListPaginatedResponse[ContentSchema]])
def get_content_list(
    request: HttpRequest,
    filters: Query[ContentFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[ContentSchema]]:
    get_container()
    container = get_container()
    service: BaseContentService = container.resolve(BaseContentService)

    content_list = service.get_content_list(
        filters=ContentFiltersEntity(search=filters.search),
        pagination=pagination_in,
    )
    content_count = service.get_content_count(filters=filters)
    items = [ContentSchema.from_entity(obj) for obj in content_list]
    pagination_out = PaginationOut(
        offset=0,
        limit=content_count,
        total=content_count,
    )
    return ApiResponse(data=ListPaginatedResponse(item=items, pagination=pagination_out))
