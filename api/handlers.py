from functools import wraps
from rest_framework.response import Response
from core.apps.dds.exceptions.dds import DDSDomainError
import logging
from rest_framework import status

logger = logging.getLogger(__name__)

def handle_dds_exceptions(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)

        except DDSDomainError as e:
            return Response(
                {"error": e.message, "details": e.details},
                status=e.http_status_code
            )

        except Exception as e:
            logger.exception(f"Unexpected error: {str(e)}")
            return Response(
                {
                    "error": "Internal server error",
                    "details": str(e),
                    "type": e.__class__.__name__
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return wrapper