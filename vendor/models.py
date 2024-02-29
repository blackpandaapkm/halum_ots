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
    bus_code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    bus_class = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=100)
    bus_date = models.DateTimeField(null=True)
    bus_picture_1 =  models.ImageField(upload_to='bus_pictures/',max_length=200,null=True, blank=True)
    bus_picture_2 =  models.ImageField(upload_to='bus_pictures/',max_length=200,null=True, blank=True)
    bus_picture_3 =  models.ImageField(upload_to='bus_pictures/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.bus_code
    
class BusRoots(models.Model):
    root_code = models.CharField(max_length=100)
    root_from = models.CharField(max_length=100,null=True)
    root_to = models.CharField(max_length=100,null=True)
    Distance = models.FloatField(null=True)
    price = models.FloatField(null=True)
    bus_code = models.CharField(max_length=100,null=True)
    root_date = models.DateTimeField(null=True)
    root_status = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.root_code

class BusClasses(models.Model):
    bus_code = models.CharField(max_length = 100)
    total_seat = models.IntegerField(null=True)
    bus_class = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.bus_class

class Airline(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    airline_code = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=100,null=True)
    airline_from = models.CharField(max_length=100,null=True)
    airline_to = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    status = models.BooleanField(null=True)
    description = models.TextField(max_length=100)
    airline_class = models.CharField(max_length=100,null=True)
    airline_date = models.DateTimeField(null=True)
    airline_picture_1 =  models.ImageField(upload_to='airline_pictures/',max_length=200,null=True, blank=True)
    airline_picture_2 =  models.ImageField(upload_to='airline_pictures/',max_length=200,null=True, blank=True)
    airline_picture_3 =  models.ImageField(upload_to='airline_pictures/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.airline_code
    
class Airline_class(models.Model):
    airline_code = models.CharField(max_length = 100,null=True)
    airline_class = models.CharField(max_length=100, null=True)
    total_sit = models.IntegerField(null=True)

    def __str__(self):
        return self.airline_class
    

class Train(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True)
    train_code = models.CharField(max_length=100,null=True)
    status = models.BooleanField(null=True)
    train_class = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=100)
    train_date = models.DateTimeField(null=True)
    train_picture_1 =  models.ImageField(upload_to='train_pictures/',max_length=200,null=True, blank=True)
    train_picture_2 =  models.ImageField(upload_to='train_pictures/',max_length=200,null=True, blank=True)
    train_picture_3 =  models.ImageField(upload_to='train_pictures/',max_length=200,null=True, blank=True)

    def __str__(self):
        return self.train_code
    

class TrainRoots(models.Model):
    root_code = models.CharField(max_length=100)
    root_from = models.CharField(max_length=100,null=True)
    root_to = models.CharField(max_length=100,null=True)
    Distance = models.FloatField(null=True)
    price = models.FloatField(null=True)
    train_code = models.CharField(max_length=100,null=True)
    root_date = models.DateTimeField(null=True)
    root_status = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.root_code

class Train_Classes(models.Model):
    total_seat = models.IntegerField(null=True)
    train_class = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.train_class
    
class Train_Coach(models.Model):
    coach_name = models.CharField(max_length=100, null=True)
    train_class = models.CharField(max_length=100, null=True)
    train_code = models.CharField(max_length=100, null=True)
    coach_status = models.CharField(max_length=100, null=True)
    coach_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.coach_name

class Train_CoachF(models.Model):
    coach_name = models.CharField(max_length=100, null=True)
    train_class = models.CharField(max_length=100, null=True)
    train_code = models.CharField(max_length=100, null=True)
    coach_status = models.CharField(max_length=100, null=True)
    coach_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.coach_name

class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Airport(models.Model):
    airport = models.CharField(max_length=100)

    def __str__(self):
        return self.airport
    
class Bus_Terminal(models.Model):
    bus_terminal = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_terminal

class Train_station(models.Model):
    train_station = models.CharField(max_length=100)

    def __str__(self):
        return self.train_station