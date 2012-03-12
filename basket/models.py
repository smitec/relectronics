from django.db import models
from models.component import *
from models.users import User

# Create your models here.

class Order(models.Model):
	owner = models.ForeignKey('User')


class lineItem(models.Model):
	order_id = models.ForeignKey('Order')
	item_id = models.ForeignKey('Component')
	quantity = models.IntegerField()