from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
from apps.service._comm._modules._comments._Comments_Add import *

urlpatterns = patterns('',
    url(r'^do/comments/$', CommentsAdd.as_view(), name='comm_comments_add'),
)