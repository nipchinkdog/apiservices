from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'votes/', include('apps.service._api._comm._urls._votes._post')),
)
