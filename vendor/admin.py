from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Hotel)
admin.site.register(Bus)
admin.site.register(Airline)
admin.site.register(Train)
admin.site.register(BusRoots)