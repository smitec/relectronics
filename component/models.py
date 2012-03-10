from django.db import models

# Create your models here.

class Component(models.Model):
	desc = models.CharField(max_length=200)
	stock = models.IntegerField()
	sup_id = models.ForeignKey('Supplier')

class Supplier(models.Model):
	name = models.CharField(max_length=200)
	site = models.CharField(max_length=200)	