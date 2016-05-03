from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Payment(models.Model):
	receiver = models.CharField(max_length=100)
	amount = models.FloatField()
	comment = models.CharField(max_length=100)

	def __str__(self):
		return self.receiver