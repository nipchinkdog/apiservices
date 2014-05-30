from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._comm._modules._comments import _Post

urlpatterns = patterns('',
    url(r'^writeComments/$', _Post.CommentsPost.as_view(), name='comments_post'),
)
urlpatterns = format_suffix_patterns(urlpatterns)