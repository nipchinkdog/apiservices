from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'tpl/', include('apps.service._angular.urls._posts')),
    url(r'tpl/', include('apps.service._angular.urls._comments')),
)