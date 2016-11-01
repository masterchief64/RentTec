from django.db import models

class Propietario(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	telefono = models.CharField(max_length=15)
	whatsapp = models.CharField(max_length=15)
	direccion = models.CharField(max_length=255)
	email = models.CharField(max_length=150)
	password = models.CharField(max_length=64)

	def __unicode__(self):
		return self.nombre