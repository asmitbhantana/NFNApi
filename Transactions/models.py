from django.db import models

# Create your models here.
from Heats.models import Heat
from User.models import BaseUser
import datetime

class Transaction(models.Model):
    TRANSACTION_TYPE = {
        ("MB", "Membership Payment"),
        ("EC", "Earning Commission"),
    }

    date_created = models.DateTimeField(blank=False, auto_now_add=True)

    amount = models.FloatField(blank=False, null=False)
    confirm_id = models.CharField(max_length=100, blank=False, null=False)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE, blank=False, null=False)
    user = models.ForeignKey(BaseUser, on_delete=models.SET_NULL, null=True)
    heat = models.ForeignKey(Heat, on_delete=models.SET_NULL, null=True, blank=True)
