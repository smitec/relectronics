from django.db import models
from component.models import *
from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):
	user_id = models.ForeignKey(User, related_name="user_id")
	item_id = models.ForeignKey('component.Component')
	quantity = models.IntegerField()
	create_time = models.DateTimeField()
	approver = models.ForeignKey(User, related_name="admin_id")
	approveal_time = models.DateTimeField()
	
	def approved(self):
		return this.approver != None
	