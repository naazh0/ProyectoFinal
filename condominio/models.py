# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.


class Condominio(models.Model):
	name = models.CharField(max_length=144)
	direccion = models.CharField(max_length=144)

	def __str__(self):
		return self.name

class AdminCondominio(models.Model):
	name = models.CharField(max_length=144)
	rut = models.CharField(max_length=15)
	correo = models.CharField(max_length=144)
	condominio = models.ForeignKey(Condominio)

	def __str__(self):
		return self.name

class Copropietario(models.Model):
	name = models.CharField(max_length=144)
	rut = models.CharField(max_length=144)
	documento = models.FileField(upload_to="docs", null=True, blank=True)
	condominio = models.ForeignKey(Condominio)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
