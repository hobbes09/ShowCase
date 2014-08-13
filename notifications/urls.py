# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('notifications.views',
    url(r'^$', 'all', name='all'),
    url(r'^/unread$', 'unread', name='unread'),
    url(r'^/mark-all-as-read$', 'mark_all_as_read', name='mark_all_as_read'),
    url(r'^/mark-as-read/(?P<pk>[0-9]+)$', 'mark_as_read', name='mark_as_read'),
    url(r'^/mark-as-unread/(?P<pk>[0-9]+)$', 'mark_as_unread', name='mark_as_unread'),
    url(r'^/check$', 'check_for_notification', name='check_for_notification'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
