# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import GithubUser

# Register your models here.


class GithubUserAdmin(admin.ModelAdmin):
    list_display = (
        'login',
        'admin_thumbnail',
    )
    model_fields = [f.name for f in GithubUser._meta.get_fields()]  # we can hardcode this as required.
    model_fields.extend(['admin_thumbnail'])
    model_fields.remove('active')
    readonly_fields = model_fields

    search_fields = ['login', 'created_at', 'get_todays_api_calls', 'get_last_weeks_api_calls',
                     'get_last_months_api_calls', 'get_todays_users', 'get_last_weeks_users', 'get_last_months_users']

admin.site.register(GithubUser, GithubUserAdmin)

