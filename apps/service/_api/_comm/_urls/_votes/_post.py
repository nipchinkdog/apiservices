from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._comm._modules._votes import _Post

urlpatterns = patterns('',  
    url(r'^writeVotes/(?P<postsid>[0-9]+)/$', _Post.VotesPost.as_view(), name='votes_post'),
)
urlpatterns = format_suffix_patterns(urlpatterns)