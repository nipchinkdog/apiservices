from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._comm._modules._posts import _Limit
from apps.service._api._comm._modules._posts import _Search
from apps.service._api._comm._modules._posts import _Challenge
from apps.service._api._comm._modules._posts import _Id
from apps.service._api._comm._modules._posts import _Author

urlpatterns = patterns('',
    url(r'^showById/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/(?P<id>[0-9]+)/posts', _Id.PostsId.as_view(), name='posts_id_list'),
    url(r'^showByAuthor/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/(?P<author>[0-9]+)/author', _Author.PostsAuthor.as_view(), name='posts_author_list'),
    url(r'^showByLimit/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/fetch$', _Limit.PostsLimit.as_view(), name='posts_limit_list'),
    url(r'^showBySearch/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/(?P<word>[a-zA-Z_]+)/search', _Search.PostsSearch.as_view(), name='posts_search_list'),
    url(r'^showByChallenge/(?P<page>[0-9]+)/(?P<limit>[0-9]+)/(?P<id>[0-9]+)/challenge', _Challenge.PostsChallenge.as_view(), name='posts_challenge_list'),
)
urlpatterns = format_suffix_patterns(urlpatterns)