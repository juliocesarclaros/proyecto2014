from django.conf.urls import patterns, include, url
from django.contrib import admin
from juego.apps.comienso.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'juego.apps.comienso.views.home', name='home'),
    url(r'^home$', 'juego.apps.comienso.views.home1', name='home1'),

    #url(r'^$', 'proyecto_juego.apps.inicio.views.registro', name='registro'),
    #url(r'^$', 'proyecto_juego.apps.inicio.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^registro/$','proyecto_juego.apps.inicio.views.registro_usuarios', name='registro_usuarios'),
    url(r'^registrar/$','juego.apps.comienso.views.registrou', name='registrou'),
    url(r'^ingresar/$','juego.apps.comienso.views.ingresar', name='ingresar'),
    url(r'^perfil/$',perfil),
    
)

#http://localhost:8000/