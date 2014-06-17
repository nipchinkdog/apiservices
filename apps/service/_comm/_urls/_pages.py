from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
from apps.service._comm._modules._pages._Pages import *

urlpatterns = patterns('',
    url(r'^about/$', PagesAbout.as_view(), name='comm_about_pages'),
)