from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'', include('apps.service._comm._urls._posts')),
    url(r'', include('apps.service._comm._urls._comments')),
    url(r'', include('apps.service._comm._urls._auth')),
    url(r'', include('apps.service._comm._urls._pages')),
)
