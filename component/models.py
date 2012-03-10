from django.db import models

# Create your models here.

class Component(models.Model):
	desc = models.CharField(max_length=200)
	partNum = models.CharField(max_length=50)
	stock = models.IntegerField()
	sup_id = models.ForeignKey('Supplier')
	
	def __unicode__(self):
		return self.desc

class Supplier(models.Model):
	name = models.CharField(max_length=200)
	site = models.CharField(max_length=200)	
	
	def __unicode__(self):
		return self.name