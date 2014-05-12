from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! View
from apps.service._modules._doc._d2 import _Doc_Home
from apps.service._modules._doc._d2 import _Doc_Css
from apps.service._modules._doc._d2 import _Doc_Download

urlpatterns = patterns('',
    url(r'^$', _Doc_Home.DocHome.as_view(), name='doc_d2_home_api'),
    url(r'^index/$', _Doc_Home.DocHome.as_view(), name='doc_d2_home_api'),
    url(r'^api/$', _Doc_Home.DocHome.as_view(), name='doc_d2_home_api'),
    url(r'^css/$', _Doc_Css.DocCss.as_view(), name='doc_d2_home_css'),
    url(r'^dl/$', _Doc_Download.DocDownload.as_view(), name='doc_d2_download_css'),
)