from django.db import models
from component.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import *
from django.dispatch import receiver

# Create your models here.

class Transaction(models.Model):
	user_id = models.ForeignKey(User, related_name="user_id")
	item_id = models.ForeignKey('component.Component')
	quantity = models.IntegerField()
	create_time = models.DateTimeField()
	approver = models.ForeignKey(User, related_name="admin_id", null=True, blank=True)
	approval_time = models.DateTimeField(null=True, blank=True)
	approved = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.user_id.__unicode__() + ": " + str(self.quantity) + " x " + self.item_id.__unicode__()

		
#save profile on create
@receiver(post_save, sender=Transaction)
def update_if_approved(sender, instance, created, **kwargs):
	if instance.approved and instance.approval_time == None:
		instance.item_id.change_stock(instance.quantity)
		instance.approval_time = datetime.now()
		instance.save()
		instance.item_id.save()
	