from rest_framework.generics import CreateAPIView
from .models import SendMoney
from .serializers import SendMoneySerializer
from rest_framework.permissions import IsAuthenticated

class SendMoneyView(CreateAPIView):
    queryset = SendMoney.objects.all()
    serializer_class = SendMoneySerializer
    permission_classes = [IsAuthenticated]
