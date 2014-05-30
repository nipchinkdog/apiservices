from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'comments/', include('apps.service._api._comm._urls._comments._list')),
    url(r'comments/', include('apps.service._api._comm._urls._comments._post')),
)
