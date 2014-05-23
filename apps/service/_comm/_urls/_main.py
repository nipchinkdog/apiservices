from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'posts/', include('apps.service._comm._urls._posts')),
    url(r'comments/', include('apps.service._comm._urls._comments')),
    url(r'ng_templates/', include('apps.service._comm._urls._ngtemplates')),
)
