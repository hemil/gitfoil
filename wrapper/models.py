# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.db import models


# Create your models here.
class GithubUser(models.Model):
    github_id = models.IntegerField(blank=False, null=False)
    login = models.CharField(blank=True, null=True, max_length=100)
    avatar_url = models.TextField(blank=True, null=True)  # don't know max length
    gravatar_id = models.TextField(blank=True, null=True)  # don't know max length
    url = models.TextField(blank=True, null=True)  # don't know max length
    html_url = models.TextField(blank=True, null=True)  # don't know max length
    followers_url = models.TextField(blank=True, null=True)  # don't know max length
    following_url = models.TextField(blank=True, null=True)  # don't know max length
    gists_url = models.TextField(blank=True, null=True)  # don't know max length
    starred_url = models.TextField(blank=True, null=True)  # don't know max length
    subscriptions_url = models.TextField(blank=True, null=True)  # don't know max length
    organizations_url = models.TextField(blank=True, null=True)  # don't know max length
    repos_url = models.TextField(blank=True, null=True)  # don't know max length
    events_url = models.TextField(blank=True, null=True)  # don't know max length
    received_events_url = models.TextField(blank=True, null=True)  # don't know max length
    type = models.CharField(blank=True, null=True, max_length=20)
    site_admin = models.BooleanField(blank=True, default=False)
    score = models.FloatField(blank=True, null=False)
    api_call_at = models.DateTimeField(blank=True, null=True)

    # Trackers
    active = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True, auto_now_add=False)

    def admin_thumbnail(self):
        return u'<img src="{url}" style="max-height: 100px; max-width: 100px;"/>'.format(url=self.avatar_url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    def get_api_calls(self, time_period_days):
        time_delta = datetime.utcnow() - timedelta(days=time_period_days)
        num_api_calls = self.model._default_manager.filter(api_call_at__gte=time_delta).count()
        return num_api_calls

    def get_users_added(self, time_period_days):
        time_delta = datetime.utcnow() - timedelta(days=time_period_days)
        num_users_added = self.model._default_manager.filter(created_at__gte=time_delta).count()
        return num_users_added

    # Num API Calls
    def get_todays_api_calls(self):
        return u'<p>{num}</p>'.format(num=self.get_api_calls(1))
    get_todays_api_calls.short_description = "Day's API calls"
    get_todays_api_calls.allow_tags = True

    def get_last_weeks_api_calls(self):
        return u'<p>{num}</p>'.format(num=self.get_api_calls(7))
    get_last_weeks_api_calls.short_description = "Week's API calls"
    get_last_weeks_api_calls.allow_tags = True

    def get_last_months_api_calls(self):
        return u'<p>{num}</p>'.format(num=self.get_api_calls(30))   # assume 30 day month, can be made variable based on month
    get_last_months_api_calls.short_description = "Month's API calls"
    get_last_months_api_calls.allow_tags = True

    # Num Users
    def get_todays_users(self):
        return u'<p>{num}</p>'.format(num=self.get_users_added(1))
    get_todays_users.short_description = "Day's Users added"
    get_todays_users.allow_tags = True

    def get_last_weeks_users(self):
        return u'<p>{num}</p>'.format(num=self.get_users_added(7))
    get_last_weeks_users.short_description = "Week's Users added"
    get_last_weeks_users.allow_tags = True

    def get_last_months_users(self):
        return u'<p>{num}</p>'.format(num=self.get_users_added(30))   # assume 30 day month, can be made variable based on month
    get_last_months_users.short_description = "Month's Users added"
    get_last_months_users.allow_tags = True

    class Meta:
        app_label = 'wrapper'
        db_table = 'github_user'

    def __unicode__(self):
        return self.login
