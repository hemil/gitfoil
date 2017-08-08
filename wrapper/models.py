# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

    class Meta:
        app_label = 'wrapper'
        db_table = 'github_user'

    def __unicode__(self):
        return self.login
