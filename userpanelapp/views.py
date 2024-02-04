from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html')
def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        password = request.POST.get('password')
        comfirmpassword = request.POST.get('comfirmpassword')
        if password == comfirmpassword:
            user = User.objects.create_user(username,useremail,password)
            user.save()
            return redirect(login)
        
    return render(request,'reg.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            request.session['username']=request.POST['username']
            return redirect(home)
        else:
            return HttpResponse("Couldn't login")


    return render(request,'login.html')

def home(request):
    if request.method == 'GET':
        if 'username' in request.session:
            username = request.session['username']
            user = User.objects.filter(username=username).first()
            return render(request, 'home.html', {'username': user})

def profile(request):
    if 'username' in request.session:
            username = request.session['username']
            user = User.objects.filter(username=username).first()
            return render(request, 'profile.html', {'username': user})
    