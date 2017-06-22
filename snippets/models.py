from django.db import models

# Create your models here.

class Snippets(models.Model):

	title = models.CharField(max_length=128)
	language = models.CharField(max_length=64)
	snippet = models.CharField(max_length=512)
	description = models.CharField(max_length=256)