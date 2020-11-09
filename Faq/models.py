from django.db import models
from User.models import BaseUser


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=100, unique=True, null=False, blank=False)
    answer = models.TextField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    question_user = models.ForeignKey(BaseUser, on_delete=models.SET_NULL, null=True)
