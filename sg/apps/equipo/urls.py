from django.conf.urls import patterns, include, url
from .views import BuscarView, RegistrarEquipo

urlpatterns = patterns('',

    #REGISTRO DE EQUIPO
    url(r'^registrar/equipo$' , RegistrarEquipo.as_view() , name="registrar_equipo"),
    url(r'^buscar/$' , BuscarView.as_view() , name="buscar"),
    url(r'^equipos/$' ,'apps.equipo.views.lista_equipos', name="lista_equipos"),
    url(r'^equipos/(?P<id_equipo>\d+)$' ,'apps.equipo.views.detalle_equipo'),
)