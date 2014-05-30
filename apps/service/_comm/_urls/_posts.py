from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
from apps.service._comm._modules._posts._Posts_Add import *
from apps.service._comm._modules._posts._Posts_List import *

urlpatterns = patterns('',
    url(r'^$', PostsList.as_view(), name='comm_posts_list'),
    url(r'^do/posts/$', PostsAdd.as_view(), name='comm_posts_add'),
)