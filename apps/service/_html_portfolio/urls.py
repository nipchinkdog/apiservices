# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
from apps.service._html_portfolio import view

urlpatterns = patterns('',
    url(r'^$', view._Html_Portfolio.as_view(), name='html_portfolio'),
)