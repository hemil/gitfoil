import json
import requests

from django.conf import settings
from django.http import HttpResponse


def get_response(data, status_code=200, message="", status=1, content_type="application/json"):
    return HttpResponse(json.dumps({
        "status": status,
        "message": message,
        "data": data
    }), content_type=content_type, status=status_code)


def get_github_data(get_params):
    """
        fetches the data from github
    Args:
        get_params: dictionary of get parameters.

    Returns:
        response
    """
    url = settings.GITHUB_USER_SEARCH_URL
    github_response = requests.get(url, get_params)
    return github_response
