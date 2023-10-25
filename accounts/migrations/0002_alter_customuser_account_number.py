# Generated by Django 4.2.6 on 2023-10-25 13:17

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_number',
            field=models.BigIntegerField(default=accounts.models.generate_account_number, unique=True),
        ),
    ]
