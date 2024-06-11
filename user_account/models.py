from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.IntegerField(blank=True, null=True, help_text='Contact phone number')
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.png')
    address = models.CharField(max_length=250, default='Enter Address')
    postal_code = models.CharField(max_length=20,default='Enter Postal')
    city = models.CharField(max_length=100,default='Enter City')


