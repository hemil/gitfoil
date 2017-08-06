import json
import logging
from django.http import HttpResponse
from rest_framework.decorators import api_view

from modules.utilities import get_github_data, get_response


@api_view(['GET'])
def user_handler(request):
    try:
        name = request.GET.get("name")  # name
        name_in = request.GET.get("name_in")  # possible values: email, login, fullname, None
        repo_number = request.GET.get("repo_number")  # a number or range
        repo_sign = request.GET.get("repo_sign")  # possible values: <=, <, >, >=, =, None
        location = request.GET.get("location")  # physical location
        language = request.GET.get("language")  # programming language
        followers = request.GET.get("followers")  # number of followers or range
        followers_sign = request.GET.get("followers_sign")  # possible values: <=, <, >, >=, =, None
        created_date = request.GET.get("created_date")  # date of creation or range
        created_date_sign = request.GET.get("created_date_sign")  # possible values: <=, <, >, >=, =, None
        sort = request.GET.get("sort")
        order = request.GET.get("order")

        github_data, response_headers = get_github_data(name, name_in, repo_number, repo_sign, location, language,
                                                        followers, followers_sign, created_date, created_date_sign,
                                                        sort, order)
        return get_response(github_data, headers=response_headers)
    except Exception as e:
        import traceback
        traceback.print_exc()
        # logging.error(e)
        return get_response(None, message="Exception: {e}".format(e=e), status_code=500)
