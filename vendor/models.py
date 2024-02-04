from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    vendor_type = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='vendor_profile_pic/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100, null=True)
    checkin_time = models.DateTimeField(null=True)
    checkout_time = models.DateTimeField(null=True)
    price = models.FloatField()
    status = models.BooleanField(default=False)
    picture =  models.ImageField(upload_to="hotel_image")
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
    