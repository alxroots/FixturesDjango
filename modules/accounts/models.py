from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
	usuario = models.ForeignKey(
		User, blank=True, null=True, on_delete=models.CASCADE
	)
	age = models.IntegerField(blank=True, null=True)


	def __str__(self):
		return str(self.usuario)