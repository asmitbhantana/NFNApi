from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from Transactions.models import Transaction
from Transactions.serializers import TransactionSerializer
from User.models import BaseUser


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = None

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'A':  # admin
            queryset = Transaction.objects.all()
        elif user.user_type == 'L':  # leader
            queryset = Transaction.objects.all()
        else:
            print("hello world",self.action)
            queryset = Transaction.objects.filter(user=self.request.user)

        # queryset = Transaction.objects.all()
        return queryset.order_by('-date_created')

    def perform_create(self, serializer):
        print(f"On perform create is the serializers {serializer}")
        serializer.save(user=self.request.user)
