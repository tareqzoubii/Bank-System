# Generated by Django 4.2.6 on 2023-10-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Manager', 'Manager')], default='Customer', max_length=8),
        ),
    ]