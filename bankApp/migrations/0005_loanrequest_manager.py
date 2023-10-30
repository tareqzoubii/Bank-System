# Generated by Django 4.2.6 on 2023-10-30 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankApp', '0004_loanrequest_acceptedloan'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_loans', to=settings.AUTH_USER_MODEL),
        ),
    ]