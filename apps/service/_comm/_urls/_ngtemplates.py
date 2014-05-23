from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
urlpatterns = patterns('apps.service._comm._modules._test',
    url(r'^test.html$','testview', name='ng_testview'),
)