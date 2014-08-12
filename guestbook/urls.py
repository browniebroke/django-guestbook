# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from views import post_entry, EntryListView, api_list_entries

urlpatterns = patterns('',
    url(r'^$', EntryListView.as_view() , name='guestbook_page_last'),
    url(r'^page(?P<page>[0-9]+)/$', EntryListView.as_view(), name='guestbook_page'),
    url(r'^post/', post_entry, name='guestbook_post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/list/', api_list_entries, name='api_guestbook_list')
)
