from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Bus_Ticket)
admin.site.register(Airline_Ticket)
admin.site.register(Train_Ticket)
