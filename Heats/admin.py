from django.contrib import admin

# Register your models here.
from Heats.models import Heat, UserHeat

admin.site.register([Heat, UserHeat])