import random
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

ROLES = (
    ('Customer','Customer'),
    ('Manager','Manager'),    
)

def generate_account_number():
    return random.randint(10**11, 10**12 - 1)
#     while True:
#         new_account_number = random.randint(111111111111, 999999999999)
#         if not CustomUser.objects.filter(account_number=new_account_number).exists():
#             return new_account_number


class CustomUser(AbstractUser):
    # account_number = models.BigIntegerField(unique=True, default=generate_account_number, editable=False)
    id_number = models.CharField(max_length=10)  # Adjust the max_length as needed
    phone_number = models.CharField(max_length=10)
    account_ammount = models.IntegerField(default=0.00)
    role = models.CharField(max_length=8, choices=ROLES, default='Customer')
    account_number = models.BigIntegerField(default = generate_account_number, primary_key=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)