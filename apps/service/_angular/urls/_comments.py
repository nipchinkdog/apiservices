from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
urlpatterns = patterns('apps.service._angular.modules._Comments',
    url(r'^comments/$','Comments', name='ng_Comments'),
)