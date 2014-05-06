from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'h/', include('apps.service._api._d2._urls._heroes._list')),
    url(r'h/', include('apps.service._api._d2._urls._heroes._detail')),
)
