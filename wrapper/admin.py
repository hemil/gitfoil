# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.utils import timezone
from django.contrib import admin
from .models import GithubUser

# Register your models here.


class GithubUserAdmin(admin.ModelAdmin):
    list_display = (
        'login',
        'admin_thumbnail',
        'get_todays_api_calls',
        'get_last_weeks_api_calls',
        'get_last_months_api_calls',
        'get_todays_users',
        'get_last_weeks_users',
        'get_last_months_users'
    )
    model_fields = [f.name for f in GithubUser._meta.get_fields()]  # we can hardcode this as required.
    model_fields.extend(['admin_thumbnail', 'get_todays_api_calls', 'get_last_weeks_api_calls',
                         'get_last_months_api_calls', 'get_todays_users', 'get_last_weeks_users',
                         'get_last_months_users'])
    model_fields.remove('active')
    readonly_fields = model_fields

    search_fields = ['login', 'created_at']

    # Problem: will make n number of db calls. One for each object(I think). VERY naive solution.
    # look for others.
    # Maybe get api calls by checking the request log file.

    def get_api_calls(self, time_period_days):
        time_delta = timezone.now() - timedelta(days=time_period_days)
        num_api_calls = GithubUser.objects.filter(api_call_at__gte=time_delta).count()
        return num_api_calls

    def get_users_added(self, time_period_days):
        time_delta = timezone.now() - timedelta(days=time_period_days)
        num_users_added = GithubUser.objects.filter(created_at__gte=time_delta).count()
        return num_users_added

    # Num API Calls
    def get_todays_api_calls(self, obj):
        return u'<p>{num}</p>'.format(num=self.get_api_calls(1))
    get_todays_api_calls.short_description = "Day's API calls"
    get_todays_api_calls.allow_tags = True

    def get_last_weeks_api_calls(self, obj):
        return u'<p>{num}</p>'.format(num=self.get_api_calls(7))
    get_last_weeks_api_calls.short_description = "Week's API calls"
    get_last_weeks_api_calls.allow_tags = True

    def get_last_months_api_calls(self, obj):
        return u'<p>{num}</p>'.format(num=self.get_api_calls(30))   # assume 30 day month, can be made variable based on month
    get_last_months_api_calls.short_description = "Month's API calls"
    get_last_months_api_calls.allow_tags = True

    # Num Users
    def get_todays_users(self, obj):
        return u'<p>{num}</p>'.format(num=self.get_users_added(1))
    get_todays_users.short_description = "Day's Users added"
    get_todays_users.allow_tags = True

    def get_last_weeks_users(self, obj):
        return u'<p>{num}</p>'.format(num=self.get_users_added(7))
    get_last_weeks_users.short_description = "Week's Users added"
    get_last_weeks_users.allow_tags = True

    def get_last_months_users(self, obj):
        return u'<p>{num}</p>'.format(num=self.get_users_added(30))   # assume 30 day month, can be made variable based on month
    get_last_months_users.short_description = "Month's Users added"
    get_last_months_users.allow_tags = True

admin.site.register(GithubUser, GithubUserAdmin)
