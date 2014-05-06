from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#! REST urls
urlpatterns = patterns('',
    
    #! api                   
    url(r'^api/', include('apps.service._api._d2._urls._heroes._main')),
    
    #! doc
    url(r'^doc/', include('apps.service._urls._doc._d2._main')),
)
