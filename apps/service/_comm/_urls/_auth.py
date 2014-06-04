from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
from apps.service._comm._modules._auth._Logout import *

urlpatterns = patterns('',
    url(r'^do/logout/$', Logout.as_view(), name='comm_logout'),
)