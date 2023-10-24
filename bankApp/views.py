from django.shortcuts import render
from .models import SendMoney
from rest_framework.generics import ListCreateAPIView
from .serializers import SendMoneySerializer
# Create your views here.

class SendMoneyCreateView(ListCreateAPIView):
    queryset = SendMoney.objects.all()
    serializer_class = SendMoneySerializer