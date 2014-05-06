from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._d2._modules._heroes import _List


urlpatterns = patterns('',
    url(r'^all/$', _List.HeroesList.as_view(), name='heroes_list'),
)
urlpatterns = format_suffix_patterns(urlpatterns)