from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from vendor.models import *
from userpanelapp.models import *
from django.core.paginator import Paginator
from django import template
register = template.Library()

@register.filter


# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    buss = Bus.objects.all()
    trains = Train.objects.all()
    airlines = Airline.objects.all()
    roots = BusRoots.objects.all()
    airports = Airport.objects.all()
    citys = City.objects.all()
    bus_Terminals = Bus_Terminal.objects.all()
    airline_classes = Airline_class.objects.all()
    busClasses = BusClasses.objects.all()
    train_Classes = Train_Classes.objects.all()
    train_stations = Train_station.objects.all()


    context = {
        'hotels': hotels,
        'buss':buss,
        'trains':trains,
        'airlines':airlines,
        'roots':roots,
        'airports':airports,
        'citys':citys,
        'bus_Terminals':bus_Terminals,
        'busClasses':busClasses,
        'train_Classes':train_Classes,
        'train_stations':train_stations,
        'airline_classes':airline_classes
        }
        
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            context = {
            'hotels': hotels,
            'buss':buss,
            'trains':trains,
            'airlines':airlines,
            'roots':roots,
            'airports':airports,
            'citys':citys,
            'bus_Terminals':bus_Terminals,
            'busClasses':busClasses,
            'train_Classes':train_Classes,
            'train_stations':train_stations,
            'airline_classes':airline_classes
            }
            return render(request, 'index.html', context)
    return render(request,'index.html',context)
        
    

def browseitems(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'browseitems.html', {'user': user})
    return render(request,'browseitems.html')

def howitworks(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'howitworks.html', {'user': user})

    return render(request,'howitworks.html')

def updateprofile(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'updateprofile.html', {'user': user})
    
    if request.method == 'POST':
        usermail = request.session['usermail']
        user = Person.objects.filter(usermail=usermail).first()
        username = request.POST.get('username')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        user_picture = request.FILES.get('user_picture')

        
        if password == user.password:
            
            user.username=username
            user.address = address
            user.birthday=birthday
            user.gender=gender

            if user_picture:
                user.user_picture = user_picture

            user.save()
            return redirect(profile)
        
    
    return render(request,'updateprofile.html')

def logout(request):
    del request.session['usermail']
    return redirect(index)

def faqs(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'faqs.html', {'user': user})
    return render(request,'faqs.html')
def contact(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'contact.html', {'user': user})
    return render(request,'contact.html')

def changepassword(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'changepassword.html', {'user': user})
    
    if request.method == 'POST':
        pasword = request.POST.get('old_password')
        newpassword = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_new_password')

        usermail = request.session['usermail']
        user = Person.objects.filter(usermail=usermail).first()
        if pasword == user.password:
            if newpassword == confirm_password:
                user.password = newpassword
                user.save()
                return redirect(profile)
            else:
                return redirect(wrongpassword)
        else:
            return redirect(wrongpassword)


    return render(request,'changepassword.html')

def wrongpassword(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'wrongpassword.html', {'user': user})
    return render(request,'wrongpassword.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        usermail = request.POST.get('usermail')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_picture = request.FILES.get('user_picture')


        person = Person(
            username=username, 
            usermail=usermail,
            address = address,
            birthday=birthday,
            gender=gender,
            password=password,
            user_picture=user_picture
            )
        
        if password == confirm_password:
            person.save()
            return redirect(login)
        
    return render(request,'regester.html')
def login(request):
    if request.method == 'POST':
        usermail = request.POST.get('usermail')
        password = request.POST.get('password')
        user = Person.objects.filter(usermail=usermail,password=password).first()
        if user is not None:
            request.session['usermail']=request.POST['usermail']
            return redirect(home)
        else:
            return redirect(wrongpassword)
        
    return render(request,'login.html')

def home(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'home.html', {'user': user})
        

def profile(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'profile.html', {'user': user})
    
def searchresult(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request, 'searchresult.html', {'user': user})
    
    if request.method == 'POST':
        type = request.POST.get('type')

        airline_from = request.POST.get('airline_from')
        airline_to = request.POST.get('airline_to')
        airline_date = request.POST.get('airline_date')
        airline_class = request.POST.get('airline_class')

        bus_from = request.POST.get('bus_from')
        bus_to = request.POST.get('bus_to')
        bus_date = request.POST.get('bus_date')
        bus_class = request.POST.get('bus_class')

        train_from = request.POST.get('train_from')
        train_to = request.POST.get('train_to')
        train_date = request.POST.get('train_date')
        train_class = request.POST.get('train_class')

        persons = request.POST.get('persons')



        if type == 'hotels':
            hotels = Hotel.objects.filter(name__icontains=sit_type)
            return render(request,'searchresult.html', {'hotels': hotels})
        elif type == 'Bus':
            bus = Bus.objects.filter(bus_code__in=BusRoots.objects.filter(root_from=bus_from, root_to=bus_to).values_list('bus_code', flat=True) , bus_class=bus_class )
            print(bus_from,bus_to,bus_class)
            print(bus)
            type = 'Bus'
            bus_paginator = Paginator(bus,6)
            page_number = request.GET.get('page')
            buss = bus_paginator.get_page(page_number)
            totalbuspage = buss.paginator.num_pages

            context = {
                'buss': buss,
                'type': type,
                'totalbuspage':totalbuspage,
                'totalbuspagelist':[n+1 for n in range(totalbuspage)]
                }
            
            return render(request,'searchresult.html', context)
        elif type == 'Train':
            train = Train.objects.filter(train_code__in=TrainRoots.objects.filter(root_from=train_from, root_to=train_to).values_list('train_code', flat=True) , train_class=train_class )
         
            type = 'Train'
            train_paginator = Paginator(train,6)
            page_number = request.GET.get('page')
            trains = train_paginator.get_page(page_number)
            totaltrainpage = trains.paginator.num_pages

            context = {
                'trains': trains,
                'type': type,
                'totaltrainpage':totaltrainpage,
                'totalbuspagelist':[n+1 for n in range(totaltrainpage)]
                }
            
            return render(request,'searchresult.html', context)
        elif type == 'Airline':
            airline = Airline.objects.filter(airline_from=airline_from,airline_to=airline_to,airline_class=airline_class)
            type = 'Airline'

            airline_paginator = Paginator(airline,6)
            page_number = request.GET.get('page')
            airlines = airline_paginator.get_page(page_number)
            totalairlinepage = airlines.paginator.num_pages

          

            context = {
                'airlines': airlines,
                'type': type,
                'persons': persons,
                'totalairlinepage':totalairlinepage,
                'totalairlinepagelist':[n+1 for n in range(totalairlinepage)]
                }
            return render(request,'searchresult.html', context)

def range_filter(n):
    return ["%d" % i for i in range(1,n+1)]

def selectticket(request):
    if request.method == 'GET':

        type = request.GET.get('type')
        persons = request.GET.get('person')
        airline_code = request.GET.get('code')
        print(type, persons, airline_code)



        if type == 'hotels':
            hotels = Hotel.objects.filter(name__icontains=sit_type)
            return render(request,'searchresult.html', {'hotels': hotels})
        elif type == 'Bus':
            bus = Bus.objects.filter(bus_code__in=BusRoots.objects.filter(root_from=bus_from, root_to=bus_to).values_list('bus_code', flat=True) , bus_class=bus_class )
            print(bus_from,bus_to,bus_class)
            print(bus)
            type = 'Bus'
            bus_paginator = Paginator(bus,6)
            page_number = request.GET.get('page')
            buss = bus_paginator.get_page(page_number)
            totalbuspage = buss.paginator.num_pages

            context = {
                'buss': buss,
                'type': type,
                'totalbuspage':totalbuspage,
                'totalbuspagelist':[n+1 for n in range(totalbuspage)]
                }
            
            return render(request,'searchresult.html', context)
        elif type == 'Train':
            train = Train.objects.filter(train_code__in=TrainRoots.objects.filter(root_from=train_from, root_to=train_to).values_list('train_code', flat=True) , train_class=train_class )
        
            type = 'Train'
            train_paginator = Paginator(train,6)
            page_number = request.GET.get('page')
            trains = train_paginator.get_page(page_number)
            totaltrainpage = trains.paginator.num_pages

            context = {
                'trains': trains,
                'type': type,
                'totaltrainpage':totaltrainpage,
                'totalbuspagelist':[n+1 for n in range(totaltrainpage)]
                }
            
            return render(request,'searchresult.html', context)
        elif type == 'Airline':
            airline = Airline.objects.filter(airline_code=airline_code).first()
            airline_class = airline.airline_class
            type = 'Airline'

            # airline_paginator = Paginator(airline,6)
            # page_number = request.GET.get('page')
            # airlines = airline_paginator.get_page(page_number)
            # totalairlinepage = airlines.paginator.num_pages

            airline_class_obj = Airline_class.objects.filter(airline_class=airline_class).first()
            total_sits_n = airline_class_obj.total_sit
            total_sits = range_filter(total_sits_n)
            print(total_sits)
            print(type, persons, airline_code)

            context = {
                'airline': airline,
                'type': type,
                'persons': persons,
                'total_sits': total_sits,
                }
            return render(request,'selectticket.html', context)
    return render(request,'selectticket.html')


def addinfodata(request):
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            return render(request,'addinfodata.html', {'user': user})
    return render(request,'addinfodata.html')