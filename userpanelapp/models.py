from django.db import models
from vendor.models import *

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=20)
    usermail = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    birthday = models.DateTimeField()
    gender = models.CharField(max_length=10)
    join_date = models.DateTimeField(auto_now_add=True)
    user_picture =  models.ImageField(upload_to='user_picture/',max_length=200,null=True, blank=True)

def __str__(self):
    return self.usermail