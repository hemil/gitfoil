import json
import logging
from django.http import HttpResponse
from rest_framework.decorators import api_view


logger = logging.getLogger("gitfoil")


@api_view(['GET'])
def user_handler(request):
    try:
        return HttpResponse("GET Wrath of Khan is on.", status=200)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(json.dumps({
            'status': 0,
            'message': "Exception: {e}".format(e=e),
            'error_code': 500,
            'data': None
        }), content_type="application/json", status=500)
