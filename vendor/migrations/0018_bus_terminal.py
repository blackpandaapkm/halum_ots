# Generated by Django 5.0.1 on 2024-02-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0017_train_train_picture_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus_Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_terminal', models.CharField(max_length=100)),
            ],
        ),
    ]