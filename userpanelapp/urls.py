from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns=[   
    path('',index,name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('browseitems/', browseitems, name='browseitems'),
    path('howitworks/', howitworks, name='howitworks'),
    path('faqs/', faqs, name='faqs'),
    path('contact/', contact, name='contact'),
    path('updateprofile/', updateprofile, name='updateprofile'),
    path('logout/', logout, name='logout'),
    path('changepassword/', changepassword, name='changepassword'),
    path('wrongpassword/', wrongpassword, name='wrongpassword'),
    path('searchresult/', searchresult, name='searchresult'),
    path('selectticket/', selectticket, name='selectticket'),
    path('addinfodata/', addinfodata, name='addinfodata'),
    path('payment/', payment, name='payment'),
    path('addticketdata/', addticketdata, name='addticketdata'),
    path('transation/', transation, name='transation'),


    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)