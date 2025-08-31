from ninja import Router

from core.api.v1.content.handlers import router as content_router


router = Router(tags=['v1'])

router.add_router('content/', content_router)
