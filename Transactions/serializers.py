from rest_framework.serializers import ModelSerializer

from Transactions.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["amount", "confirm_id", "transaction_type",
                  "heat", "user", "pk"]

        extra_kwargs = {
            'user': {'read_only': True},
            'pk': {'read_only': True}
        }
