from django.db import models


class DateTimeEntity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, auto_created=True)
    date_updated = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True