from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from vendor.models import *
import os,pathlib
# Create your views here.
def vendor_index(request):
    return render(request,'vendor_index.html')

def vendor_home(request):

   if request.method == 'GET':
    if 'email' in request.session:
        email = request.session['email']
        vendor = Vendor.objects.filter(email=email).first()
        hotels = Hotel.objects.filter(email=email)
        context = {'vendor': vendor, 'hotels': hotels}
        return render(request, 'vendor_home.html', context)


def vendor_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        vendor = Vendor.objects.filter(email=email,password=password)
        if vendor is not None:
            request.session['email']=request.POST['email']
            return redirect(vendor_home)
        else:
            return HttpResponse("Couldn't login")

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
        
    return render(request,'vendor_regester.html')

def vendor_profile(request):
    if request.method == 'GET':
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_profile.html', {'vendor': vendor})
    return render(request,'vendor_profile.html')

# def vendor_updateprofile(request):

#     if request.method == 'GET':
#         if 'email' in request.session:
#             email = request.session['email']
#             vendor = Vendor.objects.filter(email=email).first()
#             return render(request,'vendor_updateprofile.html', {'vendor': vendor})
    
#     vendor = Vendor.objects.filter(email=email).first()

#     if  request.method == "POST":
#         name = request.POST.get('name')
#         address = request.POST.get('address')
#         password = request.POST.get('password')
#         gender = request.POST.get('gender')
#         profile_pic = request.FILES.get('profile_pic')
        
#         if password == vendor.password:
#             vendor.name = name
#             vendor.address = address
#             vendor.gender = gender
#             vendor.profile_pic = profile_pic
#             vendor.save()
#             # update the session data with new data
#             return redirect(vendor_profile)

#     return render(request,'vendor_updateprofile.html')

def vendor_updateprofile(request):
    if request.method == 'GET':
        if 'email' in request.session:
            email = request.session['email']
            vendor = Vendor.objects.filter(email=email).first()
            return render(request,'vendor_updateprofile.html', {'vendor': vendor})

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
                return redirect(vendor_home)
            else:
                return HttpResponse("wrong password")
       

    return render(request,'vendor_updateprofile.html')

def vendor_logout(request):
    del request.session['email']
    return redirect(vendor_login)

def vendor_addhotel(request):

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
                return HttpResponse("Password doesn't match")
        else:
            return HttpResponse("Old password doesn't match")
        
        
    return render(request,'vendor_changepassword.html')

def vendor_deletehotel(request):
    if request.method == 'GET':
        code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            hotel = Hotel.objects.filter(email=email,code=code).first()
            hotel.delete()
            return redirect(vendor_home)


# def vendor_edithotel(request,code):
#     if request.method == 'GET':
#         if 'email' in request.session:
#             email = request.session['email']
#             hotel = Hotel.objects.filter(email=email,code=code).first()
#             return render(request,'vendor_edithotel.html', {'hotel': hotel})
        
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         address = request.POST.get('address')
#         room_number = request.POST.get('room_number')
#         price = request.POST.get('price')
#         status = request.POST.get('status')
#         description = request.POST.get('description')
#         email = request.session['email']
#         hotel_picture = request.FILES.get('hotel_picture')

#         hotel = Hotel.objects.filter(email=email,code=code).first()
#         vendor = Vendor.objects.filter(email=email).first()

#         if 'password' in request.POST:
#             password = request.POST.get('password')
#             if password == vendor.password:
#                 hotel.name = name
#                 hotel.address = address
#                 hotel.room_number = room_number
#                 hotel.price = price
#                 hotel.status = status
#                 hotel.description = description


#                 if hotel_picture:
#                     hotel.hotel_picture = hotel_picture
#                 hotel.save()
#                 return redirect(vendor_home)
#             else:
#                 return HttpResponse("wrong password")
#     return render(request,'vendor_edithotel.html')

def vendor_edithotel(request):
    if request.method == 'GET':
        code = request.GET.get('code') 
        if 'email' in request.session:
            email = request.session['email']
            hotel = get_object_or_404(Hotel, email=email, code=code)
            print(code,email)
            return render(request, 'vendor_edithotel.html', {'hotel': hotel})

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        room_number = request.POST.get('room_number')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')
        email = request.session['email']
        hotel_picture = request.FILES.get('hotel_picture', None)

        hotel = Hotel.objects.filter(email=email, code=code).first()
        vendor = Vendor.objects.filter(email=email).first()

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
                return HttpResponse("wrong password")


