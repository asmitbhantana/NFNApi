from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from Transactions.models import Transaction
from Transactions.serializers import TransactionSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = None

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        # queryset = Transaction.objects.all()
        return queryset.order_by('-date_created')

    def perform_create(self, serializer):
        print(f"On perform create is the serailizers {serializer}")
        serializer.save(user=self.request.user)
