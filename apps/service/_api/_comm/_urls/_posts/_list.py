from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._comm._modules._posts import _List
from apps.service._api._comm._modules._posts import _Limit

urlpatterns = patterns('',
    url(r'^all/$', _List.PostsList.as_view(), name='posts_all_list'),
    url(r'^showByLimit/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/$', _Limit.PostsLimit.as_view(), name='posts_limit_list'),
)
urlpatterns = format_suffix_patterns(urlpatterns)