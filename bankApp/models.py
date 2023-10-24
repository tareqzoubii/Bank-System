from django.db import models

# Create your models here.

class SendMoney(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    tha_amount = models.IntegerField()