from django.urls import path
from .views import *


urlpatterns=[   
    path('vendor_index/',vendor_index,name='vendor_home'),
    path('vendor_home/',vendor_home,name='vendor_home'),
    path('vendor_login/',vendor_login,name='vendor_login'),
    path('vendor_register/',vendor_register,name='vendor_register'),
    path('vendor_profile/',vendor_profile,name='vendor_profile'),
    path('vendor_updateprofile/',vendor_updateprofile,name='vendor_updateprofile'),
    path('vendor_addhotel/',vendor_addhotel,name='vendor_addhotel'),
    path('vendor_logout/',vendor_logout,name='vendor_logout'),
    path('vendor_chnagepassword/',vendor_chnagepassword,name='vendor_chnagepassword'),

]