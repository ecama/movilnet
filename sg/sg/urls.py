from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
      {'document_root':settings.MEDIA_ROOT, } ),

    #INICIO
    url(r'^', include('apps.inicio.urls')),

    #PAGINA PRINCIPAL
    url(r'^principal/', include('apps.principal.urls')),

    #EQUIPO
    url(r'^equipo/' , include('apps.equipo.urls')),

    #UBICACION
    url(r'^ubicacion/' , include('apps.ubicacion.urls')),

    #INTERFAZ
    url(r'^interfaz/' , include('apps.interfaz.urls')),

    #GERENCIA
#    url(r'^gerencia/' , include('apps.gerencia.urls')),
    
)