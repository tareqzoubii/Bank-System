# Generated by Django 4.2.6 on 2023-10-31 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankApp', '0007_remove_loanrequest_date_requested_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('loan_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bankApp.loanrequest')),
            ],
        ),
    ]
