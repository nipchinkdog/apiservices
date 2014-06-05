from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
urlpatterns = patterns('apps.service._angular.modules._Search',
    url(r'^search/$','Search', name='ng_Search'),
)