# Generated by Django 5.0.1 on 2024-02-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0018_bus_terminal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train_station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_station', models.CharField(max_length=100)),
            ],
        ),
    ]
