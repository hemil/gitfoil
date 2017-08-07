import json
import requests

from django.conf import settings
from django.http import HttpResponse
from rest_framework.exceptions import ParseError


def get_response(data, status_code=200, message="", status=1, content_type="application/json", headers={}):
    response = HttpResponse(json.dumps({
        "status": status,
        "message": message,
        "data": data,
        "link": headers.get("Link"),
    }), content_type=content_type, status=status_code)
    return response


def is_sign_valid(sign_string):
    if sign_string in [">", "<", "=", ">=", "<="]:
        return True
    return False


def create_q(name, name_in, repo_number, repo_sign, location, language, followers, followers_sign,
             created_date, created_date_sign):
    # All begin with leading space
    q = "{name}".format(name=name)
    if name_in and name_in in ["email", "fullname", "login"]:
        q += " in:{name_in}".format(name_in=name_in)

    if location:
        q += " location:{location}".format(location=location)

    if language:
        q += " language:{language}".format(language=language)

    if repo_number and repo_number.isdigit():
        q += " repos:"
        if is_sign_valid(repo_sign):
            # add >,<,= and their combinations
            q += "{repo_sign}".format(repo_sign=repo_sign)
        q += "{repo_number}".format(repo_number=repo_number)

    if followers and followers.isdigit():
        q += " followers:"
        if is_sign_valid(followers_sign):
            # add >,<,= and their combinations
            q += "{followers_sign}".format(followers_sign=followers_sign)
        q += "{followers}".format(followers=followers)

    if created_date:
        q += " created:"
        if is_sign_valid(created_date_sign):
            # add >,<,= and their combinations
            q += "{created_date_sign}".format(created_date_sign=created_date_sign)
        q += "{created_date}".format(created_date=created_date)
    
    return q


def create_query_param(name, name_in, repo_number, repo_sign, location, language, followers, followers_sign,
                       created_date, created_date_sign, sort, order, page):
    q = create_q(name, name_in, repo_number, repo_sign, location, language, followers, followers_sign,
                 created_date, created_date_sign)
    params = {
        "q": q
    }
    if sort and order:
        params["sort"] = sort
        params["order"] = order
    if page:
        params["page"] = page
    return params


def get_github_data(name, name_in, repo_number, repo_sign, location, language, followers, followers_sign,
                    created_date, created_date_sign, sort, order, page):
    url = settings.GITHUB_USER_SEARCH_URL
    get_params = create_query_param(name, name_in, repo_number, repo_sign, location, language, followers,
                                    followers_sign, created_date, created_date_sign, sort, order, page)
    headers = {
        "Accept": "application/vnd.github.v3.raw+json"
    }
    github_response = requests.get(url, get_params, headers=headers)
    if github_response.status_code == 200:
        return github_response.json(), github_response.headers
    raise ParseError
