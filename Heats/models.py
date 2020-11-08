from django.db import models

# Create your models here.
from User.models import BaseUser


class Heat(models.Model):
    banner_image = models.ImageField('heats/banner')
    topic = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=100, blank=False, null=False)


class UserHeat(models.Model):
    heat = models.ForeignKey(Heat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(BaseUser, on_delete=models.SET_NULL, null=True)
    is_approved = models.BooleanField(default=False, null=False, blank=False)
