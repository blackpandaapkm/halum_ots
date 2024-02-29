# Generated by Django 5.0.1 on 2024-02-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0020_train_coach_remove_train_classes_train_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train_coach',
            old_name='choch_name',
            new_name='coach_name',
        ),
        migrations.AddField(
            model_name='train_coach',
            name='coach_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='train_coach',
            name='coach_status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
