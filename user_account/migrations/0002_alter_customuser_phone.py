# Generated by Django 5.0.6 on 2024-06-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(blank=True, help_text='Contact phone number', null=True),
        ),
    ]
