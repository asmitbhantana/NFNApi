from rest_framework.serializers import ModelSerializer

from Transactions.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["amount", "confirm_id", "transaction_type", "heat"]

