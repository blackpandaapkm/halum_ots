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
    profile_pic = models.ImageField(upload_to='vendor_profile_pic/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100, null=True)
    checkin_time = models.DateTimeField(null=True)
    checkout_time = models.DateTimeField(null=True)
    price = models.FloatField(null=True)
    status = models.BooleanField(null=True)
    description = models.TextField(max_length=100)
    hotel_picture =  models.ImageField(upload_to='hotel_pictures/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Bus(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    sit_number = models.CharField(max_length=100, null=True)
    bus_from = models.CharField(max_length=100,null=True)
    bus_to = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    status = models.BooleanField(null=True)
    description = models.TextField(max_length=100)
    bus_picture =  models.ImageField(upload_to='bus_pictures/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name
    

class Airline(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    sit_number = models.CharField(max_length=100, null=True)
    airline_from = models.CharField(max_length=100,null=True)
    airline_to = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    status = models.BooleanField(null=True)
    description = models.TextField(max_length=100)
    airline_picture =  models.ImageField(upload_to='airline_pictures/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name
    

class Train(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    sit_number = models.CharField(max_length=100, null=True)
    train_from = models.CharField(max_length=100,null=True)
    train_to = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    status = models.BooleanField(null=True)
    description = models.TextField(max_length=100)
    train_picture =  models.ImageField(upload_to='train_pictures/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name