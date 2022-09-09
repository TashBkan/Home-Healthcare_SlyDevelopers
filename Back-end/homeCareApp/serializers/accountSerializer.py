from homeCareApp.models.account import Account
from rest_framework import serializer

class AccountSerializer(serializer, ModelSerializer):
    class Meta:
        model = Account
        field = ['balance', 'lastChangeDate', 'isActive']