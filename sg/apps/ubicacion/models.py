from django.db import models

class Sede(models.Model):
	sede = models.CharField(max_length=50)

	def __unicode__(self):
  		return self.sede

class Sala(models.Model):
	sede = models.ForeignKey(Sede)
	sala = models.CharField(max_length=50)

	def __unicode__(self):
		return self.sala


class Fila(models.Model):
	sala = models.ForeignKey(Sala)
	fila = models.CharField(max_length=50)

	def __unicode__(self):
		return self.fila

class UPS(models.Model):
    ups = models.CharField(max_length=50)
    sala = models.ForeignKey(Sala)

    def __unicode__(self):
        return self.ups

class Rack(models.Model):
    ups = models.ManyToManyField(UPS)
    fila = models.ForeignKey('Fila')
    rack = models.CharField(max_length=50)

    def __unicode__(self):
        return self.rack







