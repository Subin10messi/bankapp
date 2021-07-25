import django_filters
from .models import Transactions


class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = Transactions
        fields = ["Date", "Amount", "from_account_number", "to_account_number"]
