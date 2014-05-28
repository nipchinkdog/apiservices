from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._comm._modules._comments import _List

urlpatterns = patterns('',
    url(r'^showById/(?P<id>[0-9]+)/$', _List.CommentsList.as_view(), name='comments_list'),
)
urlpatterns = format_suffix_patterns(urlpatterns)