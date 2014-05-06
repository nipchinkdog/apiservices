from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

#! REST
from rest_framework.urlpatterns import format_suffix_patterns

#! View
from apps.service._api._d2._modules._heroes import _Detail_Class
from apps.service._api._d2._modules._heroes import _Detail_Faction
from apps.service._api._d2._modules._heroes import _Detail_Hero
from apps.service._api._d2._modules._heroes import _Detail_Any

urlpatterns = patterns('',
    url(r'^findByHero/(?P<name>[a-zA-Z0-9_]+)/$', _Detail_Hero.HeroesDetail.as_view(), name='heroes_detail_hero'),
    url(r'^findByClass/(?P<clss>[a-zA-Z0-9_]+)/$', _Detail_Class.HeroesDetail.as_view(), name='heroes_detail_class'),
    url(r'^findByFaction/(?P<faction>[a-zA-Z0-9_]+)/$', _Detail_Faction.HeroesDetail.as_view(), name='heroes_detail_faction'),
    url(r'^findByAny/(?P<faction>[a-zA-Z0-9_]+)/(?P<clss>[a-zA-Z0-9_]+)/$', _Detail_Any.HeroesDetail.as_view(), name='heroes_detail_any'),
    #url(r'^role/(?P<role>[a-zA-Z0-9_]+)/$', _Detail_Hero.HeroesDetail.as_view(), name='heroes_detail_role'),
)
urlpatterns = format_suffix_patterns(urlpatterns)