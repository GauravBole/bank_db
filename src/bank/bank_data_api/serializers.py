from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField
from rest_framework.generics import ListAPIView

from .models import Bank, Branch

class BankSerializer(ModelSerializer):

    class Meta:
        model = Bank
        fields = "__all__"


class BankBranchSerilizer(ModelSerializer):
    bank = SerializerMethodField()
    allow_null = True
    many = True
    class Meta:
        model = Branch
        fields = "__all__"

    def get_bank(self, obj):
        return obj.bank.bank_name



