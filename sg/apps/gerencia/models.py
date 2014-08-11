from django.db import models
from apps.ubicacion.models import Sede

class Gerencia(models.Model):
	gerencia_responsable = models.CharField(max_length=50)

	def __unicode__(self):
		return self.gerencia_responsable

class Plataforma(models.Model):
	plataforma = models.CharField(max_length=50)

	def __unicode__(self):
		return self.plataforma