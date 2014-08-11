from django.db import models
from apps.ubicacion.models import Sala, Sede, Sala, Fila, Rack
from apps.gerencia.models import Gerencia, Plataforma



class Equipo(models.Model):
  host_name = models.CharField(max_length=50)
  status = models.BooleanField() 
  funcion = models.TextField(max_length=200)
  fuentes = models.IntegerField() 
  fuentes_conectadas = models.IntegerField() 
  serial = models.CharField(max_length=50) 
  modelo = models.CharField(max_length=50) 
  sede = models.ForeignKey('ubicacion.Sede')
  sala = models.ForeignKey('ubicacion.Sala')
  fila = models.ForeignKey('ubicacion.Fila')
  rack = models.ForeignKey('ubicacion.Rack')
  gerencia_responsable = models.ForeignKey(Gerencia)
  plataforma = models.ForeignKey(Plataforma)
  def __unicode__(self):
  	  return self.host_name


