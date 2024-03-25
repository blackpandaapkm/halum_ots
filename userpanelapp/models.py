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


class Bus_Ticket(models.Model):
    name = models.CharField(max_length=100)
    bus_ticket_code = models.CharField(max_length=100)
    bus_class = models.CharField(max_length=100)
    bus_from = models.CharField(max_length=100)
    bus_to = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=100)
    bus_date = models.DateTimeField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    payment_status = models.CharField(max_length=10,null=True)
    payment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.bus_ticket_code
    
class Airline_Ticket(models.Model):
    name = models.CharField(max_length=100)
    airline_ticket_code = models.CharField(max_length=100)
    airline_class = models.CharField(max_length=100)
    airline_from = models.CharField(max_length=100)
    airline_to = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=100)
    airline_date = models.DateTimeField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthday = models.DateTimeField()
    nid_number = models.CharField(max_length = 50)
    payment_status = models.CharField(max_length=10,null=True)
    payment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.airline_ticket_code



class Train_Ticket(models.Model):
    name = models.CharField(max_length=100)
    train_ticket_code = models.CharField(max_length=100)
    train_class = models.CharField(max_length=100)
    train_from = models.CharField(max_length=100)
    train_to = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=100)
    train_date = models.DateTimeField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    nid_number = models.CharField(max_length = 50)
    payment_status = models.CharField(max_length=10,null=True)
    payment_date = models.DateTimeField(null=True)
    coach = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.train_ticket_code
    



    
