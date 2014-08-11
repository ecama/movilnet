from django.conf.urls import patterns, include, url
from .views import RegistrarSede, ReportarSala, RegistrarSala, ReportarSede

urlpatterns = patterns('',

    #REGISTRO DE SEDE
    url(r'^registrar/sede$' , RegistrarSede.as_view() , name="registrar_sede"),

    #REGISTRO DE SALA
    url(r'^registrar/sala$' , RegistrarSala.as_view() , name="registrar_sala"),

    #REPORTAR SALAS    
    url(r'^reportar/salas$' , ReportarSala.as_view() , name="reportar_sala"),

    #REPORTAR SEDES
    url(r'^reportar/sedes$' , ReportarSede.as_view() , name="reportar_sede"),

    #SALAS DEPENDIENDO LA SEDE
    url(r'^reportar/sedes/(?P<id_sede>\d+)$' ,'apps.ubicacion.views.lista_de_salas_por_sede'),

    #LISTA DE EQUIPOS POR SALA SELECCIONADA
    url(r'^reportar/salas/(?P<id_sala>\d+)$' ,'apps.ubicacion.views.lista_de_equipos_por_sala'),

    #LISTA DE EQUIPOS POR FILA SELECCIONADA
    url(r'^reportar/filas/(?P<id_fila>\d+)$' ,'apps.ubicacion.views.lista_de_equipos_por_fila'),

    #LISTADO DE SALAS
    url(r'^listado/salas$' ,'apps.ubicacion.views.listado_de_salas'),

    )