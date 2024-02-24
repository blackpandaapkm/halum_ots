from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from vendor.models import *
from userpanelapp.models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    buss = Bus.objects.all()
    trains = Train.objects.all()
    airlines = Airline.objects.all()
    roots = BusRoots.objects.all()
    context = {'hotels': hotels,'buss':buss,'trains':trains,'airlines':airlines,'roots':roots}
        
    if request.method == 'GET':
        if 'usermail' in request.session:
            usermail = request.session['usermail']
            user = Person.objects.filter(usermail=usermail).first()
            context = {'user': user, 'hotels': hotels,'buss':buss,'trains':trains,'airlines':airlines,'roots':roots}
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
        sit_type = request.POST.get('sit_type')
        airline_from = request.POST.get('airline_from')
        airline_to = request.POST.get('airline_to')
        airline_date = request.POST.get('airline_date')
        persons = request.POST.get('persons')
        type = request.POST.get('type')

        if type == 'hotels':
            hotels = Hotel.objects.filter(name__icontains=sit_type)
            return render(request,'searchresult.html', {'hotels': hotels})
        elif type == 'buss':
            buss = Bus.objects.filter(name__icontains=sit_type)
            return render(request,'searchresult.html', {'buss': buss})
        elif type == 'trains':
            trains = Train.objects.filter(name__icontains=sit_type)
            return render(request,'searchresult.html', {'trains': trains})
        elif type == 'Airline':
            airline = Airline.objects.filter(airline_from=airline_from,airline_to=airline_to)
            type = 'Airline'

            airline_paginator = Paginator(airline,6)
            page_number = request.GET.get('page')
            airlines = airline_paginator.get_page(page_number)
            totalairlinepage = airlines.paginator.num_pages

            context = {
                'airlines': airlines,
                'type': type,
                'totalairlinepage':totalairlinepage,
                'totalairlinepagelist':[n+1 for n in range(totalairlinepage)]
                }
            return render(request,'searchresult.html', context)
