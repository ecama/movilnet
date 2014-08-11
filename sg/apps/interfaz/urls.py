from django.conf.urls import patterns, include, url
from .views import RegistrarInterfaz

urlpatterns = patterns('',

    #REGISTRO DE EQUIPO
    url(r'^registrar/inter$' , RegistrarInterfaz.as_view() , name="registrar_interfaz"),

    )