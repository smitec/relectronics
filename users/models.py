from django.db import models

# Create your models here.

class User(moel.models):
	points = models.IntegerField()
	username = models.CharField(max_length=200)