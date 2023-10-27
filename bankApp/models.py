from django.db import models
from accounts.models import CustomUser

class SendMoney(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_transactions', on_delete=models.CASCADE)
    the_amount = models.PositiveIntegerField()  # Ensure the amount is non-negative
