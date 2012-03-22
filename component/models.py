from django.db import models

# Create your models here.

class Component(models.Model):
	shortName = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
	partNum = models.CharField(max_length=50)
	stock = models.IntegerField()
	points = models.IntegerField()
	sup_id = models.ForeignKey('Supplier')
	
	def __unicode__(self):
		return self.shortName

class Supplier(models.Model):
	name = models.CharField(max_length=200)
	site = models.CharField(max_length=200)	
	
	def __unicode__(self):
		return self.name