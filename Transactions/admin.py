from django.contrib import admin

# Register your models here.
from Transactions.models import Transaction

admin.site.register(Transaction)