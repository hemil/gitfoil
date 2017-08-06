from django.conf.urls import url

from .views import base_view, github_view

urlpatterns = [
    url(r'^v1/ping/?$', base_view.ping, name='ping'),
    url(r'^v1/github-users/?$', github_view.user_handler, name='github_users'),
]
