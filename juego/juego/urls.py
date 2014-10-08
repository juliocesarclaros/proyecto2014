from django.conf.urls import patterns, include, url
from django.contrib import admin
from juego.apps.comienso.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'juego.apps.comienso.views.home', name='home'),
    #url(r'^$', 'proyecto_juego.apps.inicio.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/$','juego.apps.comienso.views.registro_usuarios', name='registro_usuarios'),
)
#http://localhost:8000/