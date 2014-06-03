from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#! REST urls
urlpatterns = patterns('',
    
    #! angular templates
    url(r'^angular/', include('apps.service._angular.urls._main')),
    
    #! api                   
    url(r'^api/', include('apps.service._api._d2._urls._heroes._main')),
    url(r'^api/comm/', include('apps.service._api._comm._urls._posts._main')),
    url(r'^api/comm/', include('apps.service._api._comm._urls._comments._main')),
    url(r'^api/comm/', include('apps.service._api._comm._urls._votes._main')),
    
    #! doc
    url(r'^doc/', include('apps.service._urls._doc._d2._main')),

    #! comm
    url(r'^comm/', include('apps.service._comm._urls._main')),
    
    #! social auth
    url(r'auth', include('social_auth.urls')),
    
)
