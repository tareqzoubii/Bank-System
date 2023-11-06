# Generated by Django 4.1 on 2023-11-06 07:06

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_account_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='account_number',
            field=models.BigIntegerField(default=accounts.models.generate_account_number, primary_key=True, serialize=False),
        ),
    ]
