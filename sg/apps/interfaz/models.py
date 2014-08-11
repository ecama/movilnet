from django.db import models
from apps.equipo.models import Equipo

class Interfaz(models.Model):
	equipo = models.ForeignKey(Equipo)
	interfaz = models.CharField(max_length=50)
	ip = models.IPAddressField()
	mascara = models.IPAddressField()
	gateway = models.IPAddressField()

	def __unicode__(self):
		return self.interfaz
