from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns=[   
    path('vendor_index/',vendor_index,name='vendor_index'),
    path('vendor_home/',vendor_home,name='vendor_home'),
    path('vendor_login/',vendor_login,name='vendor_login'),
    path('vendor_register/',vendor_register,name='vendor_register'),
    path('vendor_profile/',vendor_profile,name='vendor_profile'),
    path('vendor_updateprofile/',vendor_updateprofile,name='vendor_updateprofile'),
    path('vendor_addhotel/',vendor_addhotel,name='vendor_addhotel'),
    path('vendor_logout/',vendor_logout,name='vendor_logout'),
    path('vendor_chnagepassword/',vendor_chnagepassword,name='vendor_chnagepassword'),
    path('vendor_edithotel/',vendor_edithotel,name='vendor_edithotel'),
    path('vendor_deletehotel/',vendor_deletehotel,name='vendor_deletehotel'),
    path('vendor_addbus/',vendor_addbus,name='vendor_addbus'),
    path('vendor_editbus/',vendor_editbus,name='vendor_editbus'),
    path('vendor_deletebus/',vendor_deletebus,name='vendor_deletebus'),
    path('vendor_addairline/',vendor_addairline,name='vendor_addairline'),
    path('vendor_editairline/',vendor_editairline,name='vendor_editairline'),
    path('vendor_deleteairline/',vendor_deleteairline,name='vendor_deleteairline'),
    path('vendor_addtrain/',vendor_addtrain,name='vendor_addtrain'),
    path('vendor_edittrain/',vendor_edittrain,name='vendor_edittrain'),
    path('vendor_deletetrain/',vendor_deletetrain,name='vendor_deletetrain'),
    path('vendor_errorpage/',vendor_errorpage,name='vendor_errorpage'),
    path('vendor_wrongpassword/',vendor_wrongpassword,name='vendor_wrongpassword'),
    path('vendor_browseitems/',vendor_browseitems,name='vendor_browseitems'),
    path('vendor_howitworks/',vendor_howitworks,name='vendor_howitworks'),
    path('vendor_contact/',vendor_contact,name='vendor_contact'),
    path('vendor_faqs/',vendor_faqs,name='vendor_faqs'),
    path('vendor_busroots/',vendor_busroots,name='vendor_busroots'),
    path('vendor_deletebusroot/',vendor_deletebusroot,name='vendor_deletebusroot'),
    path('vendor_editbusroot/',vendor_editbusroot,name='vendor_editbusroot'),
    path('vendor_trainpanel/',vendor_trainpanel,name='vendor_trainpanel'),
    path('vendor_traineditroot/',vendor_traineditroot,name='vendor_traineditroot'),
    path('vendor_deletetrainroot/',vendor_deletetrainroot,name='vendor_deletetrainroot'),
    path('vendor_addtraincoach/',vendor_addtraincoach,name='vendor_addtraincoach'),
    path('vendor_deletetraincoach/',vendor_deletetraincoach,name='vendor_deletetraincoach'),
    path('vendor_edittraincoach/',vendor_edittraincoach,name='vendor_edittraincoach'),



    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 