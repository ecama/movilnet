from django.db import models

class Usuario(models.Model):
	usuario = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)

	def __unicode__(self):
		return self.usuario