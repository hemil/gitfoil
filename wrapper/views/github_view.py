import json
import logging
from django.http import HttpResponse
from rest_framework.decorators import api_view


logger = logging.getLogger("gitfoil")


@api_view(['GET'])
def user_handler(request):
    try:
        name = request.GET.get("name")                                  # name
        name_in = request.GET.get("name_in")                            # possible values: email, login, fullname, None
        repo_number = request.GET.get("repo_number")                    # a number or range
        repo_sign = request.GET.get("repo_sign")                        # possible values: <=, <, >, >=, =, None
        location = request.GET.get("location")                          # physical location
        language = request.GET.get("language")                          # programming language
        followers = request.GET.get("followers")                        # number of followers or range
        followers_sign = request.GET.get("followers_sign")              # possible values: <=, <, >, >=, =, None
        created_date = request.GET.get("created_date")                  # date of creation or range
        created_date_sign = request.GET.get("created_date_sign")        # possible values: <=, <, >, >=, =, None

        return HttpResponse("GET Wrath of Khan is on.", status=200)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(json.dumps({
            'status': 0,
            'message': "Exception: {e}".format(e=e),
            'error_code': 500,
            'data': None
        }), content_type="application/json", status=500)
