# Generated by Django 5.0.1 on 2024-02-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('vendor_type', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(upload_to='vendor_profile_pic/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
