from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from vendor.models import *
from userpanelapp.models import *


# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    return render(request,'index.html',{'hotels': hotels})
        
    

def browseitems(request):
    return render(request,'browseitems.html')

def howitworks(request):
    return render(request,'howitworks.html')

def updateprofile(request):
    return render(request,'updateprofile.html')

def logout(request):
    del request.session['usermail']
    return redirect(index)

def faqs(request):
    return render(request,'faqs.html')
def contact(request):
    return render(request,'contact.html')

def wrongpassword(request):
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
    if 'username' in request.session:
            username = request.session['username']
            user = User.objects.filter(username=username).first()
            return render(request, 'profile.html', {'username': user})
    