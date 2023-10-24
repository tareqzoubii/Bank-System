from rest_framework import serializers
from .models import SendMoney

class SendMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMoney
        fields = '__all__'