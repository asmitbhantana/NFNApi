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
    citizenship_number = models.CharField(max_length=100, unique=True)
    current_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    fb_id = models.CharField(max_length=100, unique=True)
    google_id = models.CharField(max_length=100, unique=True)
    profile_pic = models.ImageField("profile-image")
    user_type = models.CharField(max_length=1, choices=USER_CHOICE)
    total_contribution = models.FloatField(default=0)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

