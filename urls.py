from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'service.views.home', name='home'),
    # url(r'^service/', include('service.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

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

)