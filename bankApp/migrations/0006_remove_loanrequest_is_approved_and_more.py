# Generated by Django 4.2.6 on 2023-10-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankApp', '0005_loanrequest_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanrequest',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='manager',
        ),
        migrations.AddField(
            model_name='acceptedloan',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
