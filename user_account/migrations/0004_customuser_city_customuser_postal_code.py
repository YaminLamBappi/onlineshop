# Generated by Django 5.0.6 on 2024-06-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_customuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='postal_code',
            field=models.CharField(default='NA', max_length=20),
        ),
    ]
