# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from .views import PortadaListView

urlpatterns = patterns('',
    url(r'^portadas/$', PortadaListView.as_view(),
        name='portafolio_albumes'),    
)