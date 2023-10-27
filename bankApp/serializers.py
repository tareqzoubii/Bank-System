from rest_framework import serializers
from .models import SendMoney
from accounts.models import CustomUser
from rest_framework import status

class SendMoneySerializer(serializers.Serializer):
    receiver_account_number = serializers.IntegerField()
    the_amount = serializers.IntegerField()

    def create(self, validated_data):
        sender = self.context['request'].user
        receiver_account_number = validated_data['receiver_account_number']
        the_amount = validated_data['the_amount']

        try:
            receiver = CustomUser.objects.get(account_number=receiver_account_number)
        except CustomUser.DoesNotExist:
            return {'message': 'Receiver not found'}, status.HTTP_404_NOT_FOUND

        if sender.account_ammount >= the_amount > 0:
            sender.account_ammount -= the_amount
            sender.save()
            receiver.account_ammount += the_amount
            receiver.save()

            SendMoney.objects.create(sender=sender, receiver=receiver, the_amount=the_amount)

            return Response({'message': 'Money sent successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Insufficient balance or invalid amount'}, status=status.HTTP_400_BAD_REQUEST)
