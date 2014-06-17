from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
urlpatterns = patterns('apps.service._angular.modules._About',
    url(r'^about/$','About', name='ng_About'),
)