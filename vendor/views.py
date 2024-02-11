from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from vendor.models import *
import os,pathlib
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
        hotels = Hotel.objects.filter(email=email)
        buss = Bus.objects.filter(email=email)
        trains = Train.objects.filter(email=email)
        airlines = Airline.objects.filter(email=email)
        context = {'vendor': vendor, 'hotels': hotels,'buss':buss,'trains':trains,'airlines':airlines}
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
            return render(request,'vendor_addbus.html',{'vendor': vendor})

    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        address = request.POST.get('address')
        sit_number = request.POST.get('sit_number')
        bus_from = request.POST.get('bus_from')
        bus_to = request.POST.get('bus_to')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        email = request.session['email']
        bus_picture = request.FILES.get('bus_picture')

        bus = Bus(
            name=name,
            code=code,
            address=address,
            sit_number=sit_number,
            bus_from=bus_from,
            bus_to=bus_to,
            price=price,
            status=status,
            description=description,
            bus_picture=bus_picture,
            email=email
        )
        
        bus.save()

        return redirect(vendor_home)

    return  render(request, 'vendor_addbus.html')

def vendor_editbus(request):
    email = None
    pcode = None 
    if 'email' in request.session:
        email = request.session['email']

    if request.method == 'GET':
        code = request.GET.get('code')
        pcode = code
        bus = get_object_or_404(Bus, email=email, code=code)
        vendor = Vendor.objects.filter(email=email).first()
        context = {'bus': bus,'vendor': vendor}
        print(email,pcode,code)
        return render(request, 'vendor_editbus.html', context)
    
    

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        sit_number = request.POST.get('sit_number')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        code = request.POST.get('code')
        bus_picture = request.FILES.get('bus_picture', None)

        if email is not None:
            vendor = Vendor.objects.filter(email=email).first()
            bus = get_object_or_404(Bus, email=email, code=code)
            print(email,pcode,code)

            if 'password' in request.POST:
                password = request.POST.get('password')
                if password == vendor.password:
                    bus.name = name
                    bus.address = address
                    bus.sit_number = sit_number
                    bus.price = price
                    bus.status = status
                    bus.description = description
                    if bus_picture:
                        bus.bus_picture = bus_picture
                    bus.save()
                    return redirect(vendor_home)
                else:
                    return redirect(vendor_wrongpassword)

    return render(request, 'vendor_edithotel.html')

def vendor_deletebus(request):
    if request.method == 'GET':
        code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            bus = Bus.objects.filter(email=email,code=code).first()
            bus.delete()
            return redirect(vendor_home)
        


# Airlines data 

def vendor_addairline(request):
    if request.method == 'GET' :
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_addairline.html',{'vendor': vendor})

    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        sit_number = request.POST.get('sit_number')
        airline_from = request.POST.get('airline_from')
        airline_to = request.POST.get('airline_to')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        email = request.session['email']
        airline_picture = request.FILES.get('airline_picture')

        airline = Airline(
            name=name,
            code=code,
            sit_number=sit_number,
            airline_from=airline_from,
            airline_to=airline_to,
            price=price,
            status=status,
            description=description,
            airline_picture=airline_picture,
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
        code = request.GET.get('code')
        pcode = code
        airline = get_object_or_404(Airline, email=email, code=code)
        vendor = Vendor.objects.filter(email=email).first()
        print(email,pcode,code)
        context = {'airline':airline , 'vendor':vendor}
        return render(request, 'vendor_editairline.html', context)
    
    

    if request.method == 'POST':
        name = request.POST.get('name')
        sit_number = request.POST.get('sit_number')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        code = request.POST.get('code')
        airline_picture = request.FILES.get('airline_picture', None)

        if email is not None:
            vendor = Vendor.objects.filter(email=email).first()
            airline = get_object_or_404(Airline, email=email, code=code)
            print(email,pcode,code)

            if 'password' in request.POST:
                password = request.POST.get('password')
                if password == vendor.password:
                    airline.name = name
                    airline.sit_number = sit_number
                    airline.price = price
                    airline.status = status
                    airline.description = description
                    if airline_picture:
                        airline.airline_picture = airline_picture
                    airline.save()
                    return redirect(vendor_home)
                else:
                    return redirect(vendor_wrongpassword)
            else:
                return redirect(vendor_errorpage)

    return render(request, 'vendor_editairline.html')

def vendor_deleteairline(request):
    if request.method == 'GET':
        code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            airline = Airline.objects.filter(email=email,code=code).first()
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
        code = request.POST.get('code')
        sit_number = request.POST.get('sit_number')
        train_from = request.POST.get('train_from')
        train_to = request.POST.get('train_to')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        email = request.session['email']
        train_picture = request.FILES.get('train_picture')

        train = Train(
            name=name,
            code=code,
            sit_number=sit_number,
            train_from=train_from,
            train_to=train_to,
            price=price,
            status=status,
            description=description,
            train_picture=train_picture,
            email=email
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
        code = request.GET.get('code')
        pcode = code
        train = get_object_or_404(Train, email=email, code=code)
        vendor = Vendor.objects.filter(email=email).first()
        print(email,pcode,code)
        context = {'train':train,'vendor':vendor}
        return render(request, 'vendor_edittrain.html', context)
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        sit_number = request.POST.get('sit_number')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        code = request.POST.get('code')
        train_picture = request.FILES.get('train_picture', None)

        if email is not None:
            vendor = Vendor.objects.filter(email=email).first()
            train = get_object_or_404(Train, email=email, code=code)
            print(email,pcode,code)

            if 'password' in request.POST:
                password = request.POST.get('password')
                if password == vendor.password:
                    train.name = name
                    train.sit_number = sit_number
                    train.price = price
                    train.status = status
                    train.description = description
                    if train_picture:
                        train.train_picture = train_picture
                    train.save()
                    return redirect(vendor_home)
                else:
                    return redirect(vendor_wrongpassword)
            else:
                return redirect(vendor_errorpage)

    return render(request, 'vendor_edittrain.html')

def vendor_deletetrain(request):
    if request.method == 'GET':
        code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            train = Train.objects.filter(email=email,code=code).first()
            train.delete()
            return redirect(vendor_home)
        else:
            return redirect(vendor_errorpage)
        
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

