from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from vendor.models import *
import os,pathlib,random
from django.core.paginator import Paginator
# Create your views here.
def vendor_index(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_index.html',{'vendor': vendor})
        
    return render(request,'vendor_index.html')

def vendor_errorpage(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_errorpage.html',{'vendor': vendor})
    return render(request,'vendor_errorpage.html')

def vendor_navbar(request):
     if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_navbar.html',{'vendor': vendor})

def vendor_wrongpassword(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_wrongpassword.html',{'vendor': vendor})
    return render(request,'vendor_wrongpassword.html')




def vendor_home(request):

   if request.method == 'GET':
    if 'email' in request.session:
        email = request.session['email']
        vendor = Vendor.objects.filter(email=email).first()
        hotel = Hotel.objects.filter(email=email)
        bus = Bus.objects.filter(email=email)
        train = Train.objects.filter(email=email)
        airline = Airline.objects.filter(email=email)


        airline_paginator = Paginator(airline,6)
        hotel_paginator = Paginator(hotel,6)
        bus_paginator = Paginator(bus,6)
        train_paginator = Paginator(train,6)

        page_number = request.GET.get('page')

        airlines = airline_paginator.get_page(page_number)
        hotels = hotel_paginator.get_page(page_number)
        buss = bus_paginator.get_page(page_number)
        trains = train_paginator.get_page(page_number)

        totalairlinepage = airlines.paginator.num_pages
        totalhotelpage = hotels.paginator.num_pages
        totalbuspage = buss.paginator.num_pages
        totaltrainpage = trains.paginator.num_pages

        context = {
            'vendor': vendor,
            'hotels': hotels,
            'buss':buss,
            'trains':trains,
            'airlines':airlines,

            'totalairlinepage':totalairlinepage,
            'totalhotelpage':totalhotelpage,
            'totalbuspage':totalbuspage,
            'totaltrainpage':totaltrainpage,

            'totalairlinepagelist':[n+1 for n in range(totalairlinepage)],
            'totalhotelpagelist':[n+1 for n in range(totalhotelpage)],
            'totalbuspagelist':[n+1 for n in range(totalbuspage)],
            'totaltrainpagelist':[n+1 for n in range(totaltrainpage)]

            }
        return render(request, 'vendor_home.html', context)
   else:
    return redirect(vendor_errorpage)



def vendor_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        vendor = Vendor.objects.filter(email=email,password=password).first()
        if vendor is not None:
            request.session['email']=request.POST['email']
            return redirect(vendor_home)
        else:
            return redirect(vendor_wrongpassword)

    return render(request,'vendor_login.html')

def vendor_register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        vendor_type = request.POST.get('vendor_type')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        gender = request.POST.get('gender')
        profile_pic = request.FILES.get('profile_pic')

        vendor = Vendor(
            name=name, 
            email=email,
            phone = 12345,
            vendor_type=vendor_type,
            address=address,
            password=password,
            gender=gender,
            profile_pic=profile_pic
            )
        
        if password == confirm_password:
            vendor.save()
            return redirect(vendor_login)
        else:
            return redirect(vendor_errorpage)
        
    return render(request,'vendor_regester.html')

def vendor_profile(request):
    if request.method == 'GET':
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_profile.html', {'vendor': vendor})
        else:
            return redirect(vendor_errorpage)
    return render(request,'vendor_profile.html')

def vendor_updateprofile(request):
    if request.method == 'GET':
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_updateprofile.html', {'vendor': vendor})
        else:
            return redirect(vendor_errorpage)

    if request.method == "POST":
        email = request.session['email']
        vendor = Vendor.objects.filter(email=email).first()

        name = request.POST.get('name')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        profile_pic = request.FILES.get('profile_pic')

        if 'password' in request.POST:
            password = request.POST.get('password')
            if password == vendor.password:
                vendor.name = name
                vendor.address = address
                vendor.gender = gender

                if profile_pic:
                    vendor.profile_pic = profile_pic

                vendor.save()
                return redirect(vendor_profile)
            else:
                return redirect(vendor_errorpage)
    else:
        return redirect(vendor_errorpage)
    return render(request,'vendor_updateprofile.html')

def vendor_logout(request):
    del request.session['email']
    return redirect(vendor_index)

def vendor_addhotel(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_addhotel.html',{'vendor': vendor})

    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        address = request.POST.get('address')
        room_number = request.POST.get('room_number')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        email = request.session['email']
        hotel_picture = request.FILES.get('hotel_picture')

        hotel = Hotel(
            name=name,
            code=code,
            address=address,
            room_number=room_number,
            price=price,
            status=status,
            description=description,
            hotel_picture=hotel_picture,
            email=email
        )
        hotel.save()
        return redirect(vendor_home)
    return  render(request, 'vendor_addhotel.html')

def vendor_chnagepassword(request):

    if request.method == 'GET':
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_changepassword.html', {'vendor': vendor})
        else:
            return redirect(vendor_errorpage)
        
    if request.method == 'POST':
        email = request.session['email']
        vendor = Vendor.objects.filter(email=email).first()
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if old_password == vendor.password:
            if new_password == confirm_new_password:
                vendor.password = new_password
                vendor.save()
                return redirect(vendor_profile)
            else:
                return redirect(vendor_wrongpassword)
        else:
            return redirect(vendor_errorpage)
        
    return render(request,'vendor_changepassword.html')

def vendor_deletehotel(request):
    if request.method == 'GET':
        code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            hotel = Hotel.objects.filter(email=email,code=code).first()
            hotel.delete()
            return redirect(vendor_home)
        else:
            return redirect(vendor_errorpage)


def vendor_edithotel(request):
    email = None
    pcode = None 
    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        code = request.GET.get('code')
        pcode = code
        hotel = get_object_or_404(Hotel, email=email, code=code)
        vendor = Vendor.objects.filter(email=email).first()
        context = {'vendor': vendor,'hotel': hotel}
        print(email,pcode,code)
        return render(request, 'vendor_edithotel.html', context)
    
    

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        room_number = request.POST.get('room_number')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        code = request.POST.get('code')
        hotel_picture = request.FILES.get('hotel_picture', None)

        if email is not None:
            vendor = Vendor.objects.filter(email=email).first()
            hotel = get_object_or_404(Hotel, email=email, code=code)
            print(email,pcode,code)

            if 'password' in request.POST:
                password = request.POST.get('password')
                if password == vendor.password:
                    hotel.name = name
                    hotel.address = address
                    hotel.room_number = room_number
                    hotel.price = price
                    hotel.status = status
                    hotel.description = description
                    if hotel_picture:
                        hotel.hotel_picture = hotel_picture
                    hotel.save()
                    return redirect(vendor_home)
                else:
                    return redirect(vendor_wrongpassword)
        else:
            return redirect(vendor_errorpage)

    return render(request, 'vendor_edithotel.html')


# bus data 

def vendor_addbus(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            bus_classes = BusClasses.objects.all()
            context = {
                'bus_classes': bus_classes,
                'vendor': vendor
            }
            return render(request,'vendor_addbus.html',context)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.session['email']
        bus_code = ''.join(random.choices('0123456789ASDFG', k=9))
        address = request.POST.get('address')
        bus_class = request.POST.get('bus_class')
        status = request.POST.get('status')
        description = request.POST.get('description')
        bus_date = request.POST.get('bus_date')

        bus_picture_1 = request.FILES.get('bus_picture_1')
        bus_picture_2 = request.FILES.get('bus_picture_2')
        bus_picture_3 = request.FILES.get('bus_picture_3')
        
        bus = Bus(
            name=name,
            email=email,
            bus_code=bus_code,
            address=address,
            bus_class=bus_class,
            status=status,
            description=description,
            bus_date = bus_date,

            bus_picture_1=bus_picture_1,
            bus_picture_2=bus_picture_2,
            bus_picture_3=bus_picture_3,
        )
        bus.save()
        return redirect(vendor_home)

    return  render(request, 'vendor_addbus.html')

def vendor_editbus(request):
    email = None
    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        bus_code = request.GET.get('code')
        print(bus_code,email)
        bus = Bus.objects.filter(email=email, bus_code=bus_code).first()
        vendor = Vendor.objects.filter(email=email).first()
        bus_classes = BusClasses.objects.all()
        context = {'bus': bus,'vendor': vendor,'bus_classes': bus_classes}
        return render(request, 'vendor_editbus.html', context)
    
    

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.session['email']
        bus_code = request.POST.get('bus_code')
        address = request.POST.get('address')
        bus_class = request.POST.get('bus_class')
        status = request.POST.get('status')
        description = request.POST.get('description')
        bus_date = request.POST.get('bus_date')

        bus_picture_1 = request.FILES.get('bus_picture_1')
        bus_picture_2 = request.FILES.get('bus_picture_2')
        bus_picture_3 = request.FILES.get('bus_picture_3')

        bus = Bus.objects.filter(email=email, bus_code=bus_code).first()
        vendor = Vendor.objects.filter(email=email).first()

        if bus and vendor:
            bus.name = name
            bus.email = email
            bus.bus_code = bus_code
            bus.address = address
            bus.bus_class = bus_class
            bus.status = status
            bus.description = description
            bus.bus_date = bus_date

            if bus_picture_1:
                bus.bus_picture_1 = bus_picture_1
            if bus_picture_2:
                bus.bus_picture_2 = bus_picture_2
            if bus_picture_3:
                bus.bus_picture_3 = bus_picture_3

            bus.save()
            return redirect(vendor_home)
        else:
            return redirect(vendor_errorpage)

    return render(request, 'vendor_edithotel.html')

def vendor_deletebus(request):

    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        bus_code = request.GET.get('code') 
        bus = Bus.objects.filter(email=email, bus_code=bus_code).first()
        print(bus_code,email)
        if bus is not None:
            roots = BusRoots.objects.filter(bus_code=bus_code)
            print(bus_code,email)
            if roots is not None:
                roots.delete()
            bus.delete()
            return redirect(vendor_home)
        else:
            print("bus is none")
    return redirect(vendor_home)



def vendor_busroots(request):
    email = None
    bus_code = None
    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        bus_code = request.GET.get('code')
        print("get area")
        print(bus_code,email)
        vendor = Vendor.objects.filter(email=email).first()
        bus = Bus.objects.filter(email=email,bus_code=bus_code).first()
        roots = BusRoots.objects.filter(bus_code=bus_code)
        bus_Terminals = Bus_Terminal.objects.all()
        context = {
            'bus': bus,
            'vendor': vendor,
            'bus_Terminals': bus_Terminals,
            'roots':roots
            }
        return render(request, 'vendor_busroots.html', context)

    if request.method == 'POST':
        root_code = ''.join(random.choices('0123456789', k=9))
        root_from = request.POST.get('root_from')
        root_to = request.POST.get('root_to')
        Distance = request.POST.get('Distance')
        price = request.POST.get('price')
        root_date = request.POST.get('root_date')
        bus_code = request.POST.get('bus_code')

        bus = Bus.objects.filter(email=email, bus_code=bus_code).first()
        root = BusRoots.objects.filter(root_code=root_code, bus_code=bus_code).first()
        bus_Terminals = Bus_Terminal.objects.all()

        if root is None:
            rootdata = BusRoots(
                root_code = root_code,
                root_from = root_from,
                root_to = root_to,
                Distance = Distance,
                price = price,
                root_date = root_date,
                bus_code = bus_code,
            )
            print("prepare for save")
            rootdata.save()
            vendor = Vendor.objects.filter(email=email).first()
            bus = Bus.objects.filter(email=email,bus_code=bus_code).first()
            roots = BusRoots.objects.filter(bus_code=bus_code)
            bus_Terminals = Bus_Terminal.objects.all()
            context = {'bus': bus,'vendor': vendor,'roots':roots,'bus_Terminals': bus_Terminals}
            return render(request, 'vendor_busroots.html', context)
        else:
            vendor = Vendor.objects.filter(email=email).first()
            bus = Bus.objects.filter(email=email,bus_code=bus_code).first()
            roots = BusRoots.objects.filter(bus_code=bus_code)
            bus_Terminals = Bus_Terminal.objects.all()
            context = {'bus': bus,'vendor': vendor,'roots':roots,'bus_Terminals': bus_Terminals}
            return render(request, 'vendor_busroots.html', context)
        
    return  render(request, 'vendor_busroots.html')




def vendor_deletebusroot(request):
    email = None
    if request.method == 'GET':
        bus_code = request.GET.get('code') 
        root_code = request.GET.get('r_code')
        
        if 'email' in request.session:
            email = request.session['email']
            print(root_code,bus_code)
            data = BusRoots.objects.filter(bus_code=bus_code, root_code=root_code).first()
            print(data)
            
            
            # Check if both the bus and root objects exist
            if data is not None:
                data.delete()

                vendor = Vendor.objects.filter(email=email).first()
                bus = Bus.objects.filter(email=email, bus_code=bus_code).first()
                roots = BusRoots.objects.filter(bus_code=bus_code)
                bus_Terminals = Bus_Terminal.objects.all()
                context = {'bus': bus,'vendor': vendor,'roots':roots,'bus_Terminals': bus_Terminals}
                return render(request, 'vendor_busroots.html', context)
            


def vendor_editbusroot(request):
    email = None
    bus_code = None
    root_code = None

    if request.method == 'GET':
        bus_code = request.GET.get('code') 
        root_code = request.GET.get('r_code')
        
    if 'email' in request.session:
        email = request.session['email']
   
    if request.method == 'POST':
        root_code = request.POST.get('root-code')
        root_from = request.POST.get('root_from')
        root_to = request.POST.get('root_to')
        Distance = request.POST.get('Distance')
        price = request.POST.get('price')
        root_date = request.POST.get('root_date')
        bus_code = request.POST.get('bus-code')
        
        
        bus = Bus.objects.filter(email=email, bus_code=bus_code).first()
        root = BusRoots.objects.filter(root_code=root_code, bus_code=bus_code).first()

        if bus and root:
            root.bus_code = bus_code
            root.root_code = root_code
            root.root_from = root_from
            root.root_to = root_to
            root.Distance = Distance
            root.price = price
            root.root_date = root_date

            root.save()

            vendor = Vendor.objects.filter(email=email).first()
            bus = Bus.objects.filter(email=email, bus_code=bus_code).first()
            roots = BusRoots.objects.filter(bus_code=bus_code)
            bus_Terminals = Bus_Terminal.objects.all()
            context = {'bus': bus,'vendor': vendor,'roots':roots,'bus_Terminals': bus_Terminals}
            return render(request,'vendor_busroots.html', context)
        else:
            return render(request,'vendor_errorpage.html')
            
        


# Airlines data 

def vendor_addairline(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            airline_classes = Airline_class.objects.all()
            airports = Airport.objects.all()
            context ={
                'airline_classes': airline_classes,
                'vendor': vendor,
                'airports': airports,
            }
            return render(request,'vendor_addairline.html',context)

    if request.method == "POST":
        name = request.POST.get('name')
        airline_code = ''.join(random.choices('0123456789', k=9))
        airline_from = request.POST.get('airline_from')
        airline_to = request.POST.get('airline_to')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        airline_date = request.POST.get('airline_date')
        airline_class = request.POST.get('airline_class')
        

        email = request.session['email']

        airline_picture_1 = request.FILES.get('airline_picture_1')
        airline_picture_2 = request.FILES.get('airline_picture_2')
        airline_picture_3 = request.FILES.get('airline_picture_3')

        airline = Airline(
            name=name,
            airline_code=airline_code,
            airline_from=airline_from,
            airline_to=airline_to,
            price=price,
            status=status,
            description=description,
            airline_date=airline_date,
            airline_class = airline_class,
            airline_picture_1=airline_picture_1,
            airline_picture_2=airline_picture_2,
            airline_picture_3=airline_picture_3,
            email=email
        )
        
        airline.save()

        return redirect(vendor_home)

    return  render(request, 'vendor_addairline.html')

def vendor_editairline(request):  
    email = None
    pcode = None 

    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        airline_code = request.GET.get('code')
        airline = get_object_or_404(Airline, email=email, airline_code=airline_code)
        vendor = Vendor.objects.filter(email=email).first()
        airline_classes = Airline_class.objects.all()
        airports = Airport.objects.all()
        context = {
            'airline':airline,
            'vendor':vendor,
            'airline_classes': airline_classes,
            'airports': airports
            }
        return render(request, 'vendor_editairline.html', context)
    
    

    if request.method == 'POST':
        name = request.POST.get('name')
        airline_code = request.POST.get('airline_code')
        airline_from = request.POST.get('airline_from')
        airline_to = request.POST.get('airline_to')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        airline_date = request.POST.get('airline_date')
        airline_class = request.POST.get('airline_class')
        

        email = request.session['email']

        airline_picture_1 = request.FILES.get('airline_picture_1')
        airline_picture_2 = request.FILES.get('airline_picture_2')
        airline_picture_3 = request.FILES.get('airline_picture_3')

        if email is not None:
            vendor = Vendor.objects.filter(email=email).first()
            airline = get_object_or_404(Airline, email=email, airline_code=airline_code)

            if airline is not None:
                airline.name = name
                airline.airline_code = airline_code
                airline.airline_from = airline_from
                airline.airline_to = airline_to
                airline.price = price
                airline.status = status
                airline.description = description
                airline.airline_date = airline_date
                airline.airline_class = airline_class

                if airline_picture_1:
                    airline.airline_picture_1 = airline_picture_1
                if airline_picture_2:
                    airline.airline_picture_2 = airline_picture_2
                if airline_picture_3:
                    airline.airline_picture_3 = airline_picture_3

                airline.save()
                return redirect(vendor_home)
            else:
                return redirect(vendor_wrongpassword)
        else:
            return redirect(vendor_errorpage)

    return render(request, 'vendor_editairline.html')

def vendor_deleteairline(request):
    if request.method == 'GET':
        airline_code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            airline = Airline.objects.filter(email=email,airline_code=airline_code).first()
            airline.delete()
            return redirect(vendor_home)
        else:
            return redirect(vendor_errorpage)
        

# Train data 

def vendor_addtrain(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_addtrain.html',{'vendor': vendor})

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.session['email']
        train_code = ''.join(random.choices('0123456789', k=9))
        status = request.POST.get('status')
        description = request.POST.get('description')
        train_date = request.POST.get('train_date')
        
        train_picture_1 = request.FILES.get('train_picture_1')
        train_picture_2 = request.FILES.get('train_picture_2')
        train_picture_3 = request.FILES.get('train_picture_3')

        train = Train(
            name=name,
            email=email,
            train_code=train_code,
            status=status,
            description=description,
            train_date =train_date,
            train_picture_1=train_picture_1,
            train_picture_2=train_picture_2,
            train_picture_3=train_picture_3
        )
        
        train.save()

        return redirect(vendor_home)

    return  render(request, 'vendor_addtrain.html')

def vendor_edittrain(request):
    email = None
    pcode = None 
    
    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        train_code = request.GET.get('code')
        pcode = train_code
        train = get_object_or_404(Train, email=email, train_code=train_code)
        vendor = Vendor.objects.filter(email=email).first()
        print(email,pcode,train_code)
        context = {'train':train,'vendor':vendor}
        return render(request, 'vendor_edittrain.html', context)
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        description = request.POST.get('description')
        train_code = request.POST.get('train_code')
        train_date = request.POST.get('train_date')
        train_picture_1 = request.FILES.get('train_picture_1', None)
        train_picture_2 = request.FILES.get('train_picture_2', None)
        train_picture_3 = request.FILES.get('train_picture_3', None)

        if email is not None:
            vendor = Vendor.objects.filter(email=email).first()
            train = get_object_or_404(Train, email=email, train_code=train_code)
            print(email,pcode,train_code)

            
            if train is not None:
                train.name = name
                train.status = status
                train.description = description
                train.train_date = train_date

                if train_picture_1:
                    train.train_picture_1 = train_picture_1
                if train_picture_2:
                    train.train_picture_2 = train_picture_2
                if train_picture_3:
                    train.train_picture_3 = train_picture_3
                train.save()
                return redirect(vendor_home)
            else:
                return redirect(vendor_wrongpassword)
           

    return render(request, 'vendor_edittrain.html')

def vendor_deletetrain(request):
    if request.method == 'GET':
        train_code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            train = Train.objects.filter(email=email,train_code=train_code).first()
            train.delete()
            return redirect(vendor_home)
        else:
            return redirect(vendor_errorpage)


def vendor_trainpanel(request):
    email = None
    train_code = None
    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        train_code = request.GET.get('code')
        print("get area")
        print(train_code,email)
        vendor = Vendor.objects.filter(email=email).first()
        train = Train.objects.filter(email=email,train_code=train_code).first()
        roots = TrainRoots.objects.filter(train_code=train_code)
        train_stations = Train_station.objects.all()
        train_classes = Train_Classes.objects.all()
        coachs = Train_CoachF.objects.filter(train_code=train_code)
        context = {
        'train': train,
        'vendor': vendor,
        'train_stations': train_stations,
        'roots':roots,
        'coachs':coachs,
        'train_classes': train_classes
        }
        return render(request, 'vendor_trainpanel.html', context)

    if request.method == 'POST':
        root_code = ''.join(random.choices('0123456789', k=9))
        root_from = request.POST.get('root_from')
        root_to = request.POST.get('root_to')
        Distance = request.POST.get('Distance')
        price = request.POST.get('price')
        root_date = request.POST.get('root_date')
        train_code = request.POST.get('train_code')
        root_status = request.POST.get('root_status') 

        train = Train.objects.filter(email=email, train_code=train_code).first()
        root = TrainRoots.objects.filter(root_code=root_code, train_code=train_code).first()
        train_stations = Train_station.objects.all()

        if root is None:
            rootdata = TrainRoots(
                root_code = root_code,
                root_from = root_from,
                root_to = root_to,
                Distance = Distance,
                price = price,
                root_date = root_date,
                train_code = train_code,
                root_status = root_status
            )
            print("prepare for save")
            rootdata.save()
            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)
        else:
            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)
        
    return  render(request, 'vendor_busroots.html')

def vendor_addtraincoach(request):
    email = None
    train_code = None
    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        train_code = request.GET.get('code')
            
    
    if request.method == 'POST' :
        train_code = request.POST.get('train_code')
        coach_name = request.POST.get('coach_name')
        coach_code = ''.join(random.choices('01234567f89', k=9))
        train_class = request.POST.get('train_class')
        coach_status = request.POST.get('coach_status')

        train = Train.objects.filter(email=email, train_code=train_code).first()
        coach = Train_CoachF.objects.filter(coach_code=coach_code, train_code=train_code).first()
        print(train_code, train_class, coach_name, coach_status, train_class, coach_code)
        if train is not None:
            coach_data = Train_CoachF(
                coach_code = coach_code,
                train_code = train_code,
                coach_name = coach_name,
                train_class = train_class,
                coach_status = coach_status
            )
            coach_data.save()
            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)
        else:
            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)


def vendor_traineditroot(request):
    email = None

    if request.method == 'GET':
        train_code = request.GET.get('code')
        
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)
   
    if request.method == 'POST':
        root_code = request.POST.get('root-code')
        root_from = request.POST.get('root_from')
        root_to = request.POST.get('root_to')
        Distance = request.POST.get('Distance')
        price = request.POST.get('price')
        root_date = request.POST.get('root_date')
        root_status = request.POST.get('root-status')
        train_code = request.POST.get('train-code')
        
        
       
        root = TrainRoots.objects.filter(root_code=root_code, train_code=train_code).first()

        if root:
            root.train_code = train_code
            root.root_code = root_code
            root.root_from = root_from
            root.root_to = root_to
            root.Distance = Distance
            root.price = price
            root.root_date = root_date
            root.root_status = root_status

            root.save()

            if 'email' in request.session:
                email = request.session['email']

            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)
            
        else:
            return render(request,'vendor_errorpage.html')

def vendor_edittraincoach(request):
    email = None
    train_code = None
    coach_code = None

    if request.method == 'GET':
        train_code = request.GET.get('code') 
        coach_code = request.GET.get('coach_code')
        
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code,coach_code=coach_code)
            print(coach_code,train_code,coachs)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)
   
    if request.method == 'POST' :
        
        coach_name = request.POST.get('coach_name')
        coach_code = request.POST.get('coach-code')
        train_class = request.POST.get('train_class')
        coach_status = request.POST.get('coach_status')
        train_code = request.POST.get('train_code')
        
        
        coach_data  = Train_CoachF.objects.filter(coach_code=coach_code, train_code=train_code).first()

        if coach_data:
            coach_data.train_code = train_code
            coach_data.coach_name = coach_name
            coach_data.coach_code = coach_code
            coach_data.train_class = train_class
            coach_data.coach_status = coach_status
            print(coach_code,train_code)
          

            coach_data.save()

            if 'email' in request.session:
                email = request.session['email']

            vendor = Vendor.objects.filter(email=email).first()
            train = Train.objects.filter(email=email,train_code=train_code).first()
            roots = TrainRoots.objects.filter(train_code=train_code)
            train_stations = Train_station.objects.all()
            train_classes = Train_Classes.objects.all()
            coachs = Train_CoachF.objects.filter(train_code=train_code)
            context = {
            'train': train,
            'vendor': vendor,
            'train_stations': train_stations,
            'roots':roots,
            'coachs':coachs,
            'train_classes': train_classes
            }
            return render(request, 'vendor_trainpanel.html', context)
            
         
def vendor_deletetraincoach(request):
    email = None
    if request.method == 'GET':
        train_code = request.GET.get('code') 
        coach_code = request.GET.get('coach_code')
        
        if 'email' in request.session:
            email = request.session['email']
            print(coach_code,train_code)
            data = Train_CoachF.objects.filter(train_code=train_code, coach_code=coach_code).first()
            print(data)
            
            
            # Check if both the bus and root objects exist
            if data is not None:
                data.delete()

                vendor = Vendor.objects.filter(email=email).first()
                train = Train.objects.filter(email=email,train_code=train_code).first()
                roots = TrainRoots.objects.filter(train_code=train_code)
                train_stations = Train_station.objects.all()
                train_classes = Train_Classes.objects.all()
                coachs = Train_CoachF.objects.filter(train_code=train_code)
                context = {
                'train': train,
                'vendor': vendor,
                'train_stations': train_stations,
                'roots':roots,
                'coachs':coachs,
                'train_classes': train_classes
                }
                return render(request, 'vendor_trainpanel.html', context)
    
def vendor_deletetrainroot(request):
    email = None
    if request.method == 'GET':
        train_code = request.GET.get('code') 
        root_code = request.GET.get('r_code')
        
        if 'email' in request.session:
            email = request.session['email']
            print(root_code,train_code)
            data = TrainRoots.objects.filter(train_code=train_code, root_code=root_code).first()
            print(data)
            
            
            # Check if both the bus and root objects exist
            if data is not None:
                data.delete()

                vendor = Vendor.objects.filter(email=email).first()
                train = Train.objects.filter(email=email,train_code=train_code).first()
                roots = TrainRoots.objects.filter(train_code=train_code)
                train_stations = Train_station.objects.all()
                train_classes = Train_Classes.objects.all()
                coachs = Train_CoachF.objects.filter(train_code=train_code)
                context = {
                'train': train,
                'vendor': vendor,
                'train_stations': train_stations,
                'roots':roots,
                'coachs':coachs,
                'train_classes': train_classes
                }
                return render(request, 'vendor_trainpanel.html', context)


def vendor_faqs(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_faqs.html',{'vendor': vendor})
    return render(request,'vendor_faqs.html')

def vendor_contact(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_contact.html',{'vendor': vendor})
    return render(request,'vendor_contact.html')
def vendor_howitworks(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_howitworks.html',{'vendor': vendor})
    return render(request,'vendor_howitworks.html')
def vendor_browseitems(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_browseitems.html',{'vendor': vendor})
    return render(request,'vendor_browseitems.html')

