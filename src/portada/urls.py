# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from .views import PortadaListView,ProbarSudo, ResumirWebPage

urlpatterns = patterns('',
    url(r'^$', PortadaListView.as_view(),
        name='portafolio_albumes'),
    url(r'sudo/$', ProbarSudo.as_view(),
        name='probar_sudo'),
    url(r'resumen/$', ResumirWebPage.as_view(),
        name='probar_resumen'),
)
