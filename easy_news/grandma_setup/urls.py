# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'easy_news.grandma_setup.views.index', name='easy_news_index'),
)
