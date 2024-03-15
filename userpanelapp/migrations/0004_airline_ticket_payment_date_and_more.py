# Generated by Django 5.0.1 on 2024-03-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanelapp', '0003_airline_ticket_bus_ticket_train_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline_ticket',
            name='payment_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='airline_ticket',
            name='payment_status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bus_ticket',
            name='payment_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='bus_ticket',
            name='payment_status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='train_ticket',
            name='payment_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='train_ticket',
            name='payment_status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
