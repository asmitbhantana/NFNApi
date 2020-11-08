from django.db import models

# Create your models here.
from Heats.models import Heat


class Guideline(models.Model):
    pdf = models.FileField('guideline/', blank=False, null=False)
    order = models.IntegerField(blank=False, null=False, default=0)
    heat = models.ForeignKey(Heat, on_delete=models.CASCADE, blank=False, null=False)