from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'd2/', include('apps.service._urls._doc._d2._urls')),
)
