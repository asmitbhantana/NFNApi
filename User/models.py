from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from User.abstract import DateTimeEntity


class BaseUser(AbstractUser, DateTimeEntity):
    GENDER_CHOICE = {
        ("1", "Male"),
        ("2", "Female"),
        ("3", "Other")
    }
    USER_CHOICE = {
        ("1", "User"),
        ("2", "NFN Worker"),
        ("3", "NFN Leader"),
        ("4", "NFN Admin"),
    }
    email = models.EmailField(unique=True, blank=False, null=False)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    citizenship_number = models.CharField(max_length=100, unique=True, blank=False)
    current_address = models.CharField(max_length=100, blank=False)
    permanent_address = models.CharField(max_length=100, blank=False)
    fb_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    google_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    profile_pic = models.ImageField("profile-image", blank=True, null=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICE, default="1")
    total_contribution = models.FloatField(default=0)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

