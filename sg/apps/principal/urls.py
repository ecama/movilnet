from django.conf.urls import patterns, include, url
from .views import Principal

urlpatterns = patterns('',

 #   url(r'^inicio/$' ,'apps.principal.views.Principal'),

    url(r'^registro/$' ,'apps.principal.views.Registro'),

	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login', name='logout'),

	url(r'^inicio/$' , Principal.as_view() , name="lista_de_equipos"),

)