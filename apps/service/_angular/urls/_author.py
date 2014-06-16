from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
urlpatterns = patterns('apps.service._angular.modules._Author',
    url(r'^author/$','Author', name='ng_Auhtor'),
)