# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.utils import timezone
from django.contrib import admin
from .models import GithubUser


# Register your models here.
def get_api_calls(time_period_days):
    time_delta = timezone.now() - timedelta(days=time_period_days)
    num_api_calls = GithubUser.objects.filter(api_call_at__gte=time_delta).values("api_call_at").distinct().count()
    return num_api_calls


def get_users_added(time_period_days):
    time_delta = timezone.now() - timedelta(days=time_period_days)
    num_users_added = GithubUser.objects.filter(created_at__gte=time_delta).count()
    return num_users_added


# Num API Calls
def get_todays_api_calls():
    return get_api_calls(1)


def get_last_weeks_api_calls():
    return get_api_calls(7)


def get_last_months_api_calls():
    return get_api_calls(30)  # assume 30 day month, can be made variable based on month


# Num Users
def get_todays_users():
    return get_users_added(1)


def get_last_weeks_users():
    return get_users_added(7)


def get_last_months_users():
    return get_users_added(30)  # assume 30 day month, can be made variable based on month


last_months_users = get_last_months_users()
last_weeks_users = get_last_weeks_users()
todays_users = get_todays_users()

last_months_api_calls = get_last_months_api_calls()
last_weeks_api_calls = get_last_weeks_api_calls()
todays_api_calls = get_todays_api_calls()


class GithubUserAdmin(admin.ModelAdmin):
    list_display = (
        'login',
        'admin_thumbnail',
        'get_api_calls_daily',
        'get_api_calls_weekly',
        'get_api_calls_monthly',
        'get_users_daily',
        'get_users_weekly',
        'get_users_monthly'
    )
    model_fields = [f.name for f in GithubUser._meta.get_fields()]  # we can hardcode this as required.
    model_fields.append('admin_thumbnail')
    model_fields.remove('active')
    readonly_fields = model_fields

    search_fields = ['login', 'created_at']

    # #TODO Problem: will make n number of db calls. One for each object(I think). VERY naive solution.
    # look for others.
    # Maybe get api calls by checking the request log file.
    #
    # Solved. single db hit when admin.py is loaded. and that variable loaded each time.

    # Num API Calls
    def get_api_calls_daily(self, obj):
        return todays_api_calls
    get_api_calls_daily.short_description = "Day's API calls"

    def get_api_calls_weekly(self, obj):
        return last_weeks_api_calls
    get_api_calls_weekly.short_description = "Week's API calls"

    def get_api_calls_monthly(self, obj):
        return last_months_api_calls
    get_api_calls_monthly.short_description = "Month's API calls"

    def get_users_daily(self, obj):
        return todays_users
    get_users_daily.short_description = "Day's Users added"

    def get_users_weekly(self, obj):
        return last_weeks_users
    get_users_weekly.short_description = "Week's Users added"

    def get_users_monthly(self, obj):
        return last_months_users
    get_users_monthly.short_description = "Month's Users added"

admin.site.register(GithubUser, GithubUserAdmin)
