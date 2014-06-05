from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._comm._modules._posts import _Limit
from apps.service._api._comm._modules._posts import _Search

urlpatterns = patterns('',
    url(r'^showByLimit/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/fetch$', _Limit.PostsLimit.as_view(), name='posts_limit_list'),
    url(r'^showBySearch/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/(?P<word>[a-zA-Z_]+)/search', _Search.PostsSearch.as_view(), name='posts_search_list'),
)
urlpatterns = format_suffix_patterns(urlpatterns)