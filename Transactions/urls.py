from django.urls import path

from Transactions.views import TransactionsViewSet

app_name = "transaction"

urlpatterns = [
    path('all/', TransactionsViewSet.as_view({'get': 'list'}), name="all"),

]
