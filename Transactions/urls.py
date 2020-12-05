from django.urls import path

from Transactions.views import TransactionsViewSet

app_name = "transaction"

urlpatterns = [
    path('list/', TransactionsViewSet.as_view({'get': 'list', 'post': 'create'}), name="all"),
]
