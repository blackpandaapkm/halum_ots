from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from vendor.models import *
from userpanelapp.models import *
from django.core.paginator import Paginator
from django import template
from django.http import JsonResponse
import os,pathlib,random
from django.urls import reverse
from django.utils import timezone
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
            roots = BusRoots.objects.filter(root_from=bus_from, root_to=bus_to).values_list('root_code', flat=True)
            print(roots)
            type = 'Bus'
            bus_paginator = Paginator(bus,6)
            page_number = request.GET.get('page')
            buss = bus_paginator.get_page(page_number)
            totalbuspage = buss.paginator.num_pages

            context = {
                'buss': buss,
                'type': type,
                'persons': persons,
                'totalbuspage':totalbuspage,
                'totalbuspagelist':[n+1 for n in range(totalbuspage)],
                'bus_from': bus_from,
                'bus_to': bus_to,
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
        bus_code = request.GET.get('code')
        bus_from = request.GET.get('bus_from')
        bus_to = request.GET.get('bus_to')
        print(type, persons, airline_code)
        print(bus_code)

        if type == 'hotels':
            hotels = Hotel.objects.filter(name__icontains=sit_type)
            return render(request,'searchresult.html', {'hotels': hotels})
        elif type == 'Bus':
            bus = Bus.objects.filter(bus_code = bus_code).first()
            # This will print the queryset as a comma-separated string
            print("hello hello")
            # print(bus_root)
            bus_class = bus.bus_class
            type = 'Bus'
            root = BusRoots.objects.filter(root_from=bus_from, root_to=bus_to, bus_code = bus_code).first()
            print(root)
            bus_class_obj = BusClasses.objects.filter(bus_class=bus_class).first()
            total_sits_n = bus_class_obj.total_seat
            total_sits = range_filter(total_sits_n)
            print(total_sits)
            print(type, persons, bus_code)
            print("jamela")
           
           

            context = {
                'bus': bus,
                'type': type,
                'persons': persons,
                'total_sits': total_sits,
                'root' : root
                }
            
            return render(request,'selectticket.html', context)
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
            print("jamela")

            context = {
                'airline': airline,
                'type': type,
                'persons': persons,
                'total_sits': total_sits,
                }
            return render(request,'selectticket.html', context)
    if request.method == 'POST':
        selected_sits = request.POST.get('selected_sits')
        airline_code = request.POST.get('airline_code')
        persons = request.POST.get('persons')
        print("selectticket")
        print(selected_sits,airline_code,persons)
        # Redirect to addinfodata view with necessary data as URL parameters
        # return redirect(reverse('addinfodata') + f'?selected_sits={",".join(selected_sits)}&airline_code={airline_code}&persons={persons}')
    return render(request,'selectticket.html')


def addinfodata(request):
    type = request.GET.get('type')
    selected_sits = request.GET.get('selected_sits')
    airline_code = request.GET.get('airline_code')
    bus_code = request.GET.get('bus_code')
    person = int(request.GET.get('persons'))
    persons = range_filter(person)
    root = request.GET.get('root')
    
    # Process your data and render the template with the necessary context
    print("addinfodata")
    print(selected_sits, airline_code, persons,bus_code)
    
    int_array = []
    selected_sits_list = selected_sits.split(',')
    print(selected_sits_list)

    # # Convert selected_sits to integers
    # int_array = [int(sit) for sit in selected_sits_list]

    ticket_code = "None"
    passenger_name = "None"
    email = "None"
    phone = "None"
    address = "None"
    gender = "None"
    birthday = "None"
    nid_number = "None"

    ticket_data = {}

    if type == 'hotels':
        pass
    elif type == 'Bus':
        for person, selected_sits in zip(persons, selected_sits_list):
            ticket_data[person] = {
                    'passenger_email': email,
                    'passenger_phone': phone,
                    'passenger_address': address,
                    'passenger_gender': gender,
                    'passenger_birthday': birthday,
                    'passenger_nid_number': nid_number,


                    'bus_code': bus_code,
                    'person': person,
                    'ticket_code': ticket_code,
                    'passenger_name': passenger_name,
                    'selected_sits': selected_sits
                }

        # Print the airline_data dictionary
        print(ticket_data)

        context = {
            'ticket_data': ticket_data,
            'bus_code': bus_code,
            'type': type,
            'root': root,
        }
        if(context==context):
            print("addinfodata ok to go bus")
            return render(request, 'addinfodata.html', context)
    elif type == 'Train':
        pass
    elif type == 'Airline':
        # Iterate over the ticket_codes and persons lists simultaneously using zip()
        for person, selected_sits in zip(persons, selected_sits_list):
            # Create a new dictionary for each ticket_code
            ticket_data[person] = {
                'passenger_email': email,
                'passenger_phone': phone,
                'passenger_address': address,
                'passenger_gender': gender,
                'passenger_birthday': birthday,
                'passenger_nid_number': nid_number,


                'airline_code': airline_code,
                'person': person,
                'ticket_code': ticket_code,
                'passenger_name': passenger_name,
                'selected_sits': selected_sits
            }

        # Print the airline_data dictionary
        print(ticket_data)

        context = {
            'ticket_data': ticket_data,
            'airline_code': airline_code,
            'type': type
        }
        if(context==context):
            print("addinfodata ok to go ")
            return render(request, 'addinfodata.html', context)
    return render(request, 'addinfodata.html', context)







def addticketdata(request):

    if request.method == 'POST':
        airline_code = request.POST.get('airline_code')
        seat_number = request.POST.get('seat-number')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        nid_number = request.POST.get('nid_number')
        ticket_data = request.POST.get('ticket_data')
        ticket_data = eval(ticket_data)

        type = request.POST.get('type')
        bus_code = request.POST.get('bus_code')
        root = request.POST.get('root')

        print("addairlineticketdata")
        print(airline_code, seat_number, name, email, phone, address, gender, birthday, nid_number)
        print(type)
        print(bus_code)
        print(root)


        # ticket_codes = []

        # for i in range(person):
        #     random_code = ''.join(random.choices('0123456789', k=4))
        #     ticket_code = f"{airline_code}{random_code}{int_array[i]}"
        #     ticket_codes.append(ticket_code)

        # print(ticket_codes)
        person = 0
        if type == 'Airline':
            random_code = ''.join(random.choices('0123456789', k=4))
            ticket_code = f"{airline_code}{random_code}{seat_number}"


            for ticket in ticket_data.values():
                if ticket['selected_sits'] == seat_number:
                    person = ticket['person']



            ticket_data[person] = {
                'passenger_email': email,
                'passenger_phone': phone,
                'passenger_address': address,
                'passenger_gender': gender,
                'passenger_birthday': birthday,
                'passenger_nid_number': nid_number,


                'airline_code': airline_code,
                'person': person,
                'ticket_code': ticket_code,
                'passenger_name': name,
                'selected_sits': seat_number
            }

            context = {
                'ticket_data': ticket_data,
                'airline_code': airline_code,
                'type': type,
                'root': root
            }
            if(context==context):
                print("addinfodata ok to go ")
                return render(request, 'addinfodata.html', context)
        elif type == 'Train':
            pass
        elif type == 'Bus':
            random_code = ''.join(random.choices('0123456789', k=4))
            ticket_code = f"{bus_code}{random_code}{seat_number}"


            for ticket in ticket_data.values():
                if ticket['selected_sits'] == seat_number:
                    person = ticket['person']



            ticket_data[person] = {
                'passenger_email': email,
                'passenger_phone': phone,
                'passenger_address': address,
                'passenger_gender': gender,
                'passenger_birthday': birthday,
                'passenger_nid_number': nid_number,


                'bus_code': bus_code,
                'person': person,
                'ticket_code': ticket_code,
                'passenger_name': name,
                'selected_sits': seat_number
            }

            context = {
                'ticket_data': ticket_data,
                'bus_code': bus_code,
                'type': type,
                'root':root
            }
            if(context==context):
                print("addinfodata ok to go ")
                return render(request, 'addinfodata.html', context)
        elif type == 'Hotels':
            pass
    



        




def payment(request):
    if request.method == 'GET':
        ticket_data = request.GET.get('ticket_data')
        ticket_data = eval(ticket_data)
        type = request.GET.get('type')
        root = request.GET.get('root')

        if type == 'Airline':
            # Extract the airline_code for each ticket
            for ticket in ticket_data.values():
                airline_code = ticket['airline_code']
                person = ticket['person']
                
            
            # Print the ticket_data dictionary
            times = int(person)
            print(ticket_data)
            print("payment")
            print(airline_code)
            airline = Airline.objects.filter(airline_code=airline_code).first()
            price = airline.price
            print(price)
            print(times)
            total_price = price * times
            print(total_price)

            otp_verfication = "False"
            payment_status = "None"

            context = {
                'ticket_data': ticket_data,
                'total_price': total_price,
                'price': price,
                'otp_verfication' : otp_verfication,
                'payment_status' : payment_status,
                'type':type,
            }

            return render(request, 'payment.html', context)
        elif type == 'Train':
            pass
        elif type == 'Bus':
            for ticket in ticket_data.values():
                bus_code = ticket['bus_code']
                person = ticket['person']
                
            
            # Print the ticket_data dictionary
            times = int(person)
            print(ticket_data)
            print("payment")
            print(root)
            root_data = BusRoots.objects.filter(root_code=root).first()
            price = root_data.price
            print(price)
            print(times)
            total_price = price * times
            print(total_price)

            otp_verfication = "False"
            payment_status = "None"

            context = {
                'ticket_data': ticket_data,
                'total_price': total_price,
                'price': price,
                'otp_verfication' : otp_verfication,
                'payment_status' : payment_status,
                'type':type,
                'root':root
            }

            return render(request, 'payment.html', context)
        elif type == 'Hotels':
            pass
    

def transation(request):
    if request.method == 'POST':
        otpphone = request.POST.get('otpphone')
        airline_code = request.POST.get('airline_code')
        paytype = request.POST.get('paytype')
        transation_id = request.POST.get('transation_id')
        total_price = request.POST.get('total_price')
        price = request.POST.get('price')
        ticket_data = request.POST.get('ticket_data')
        ticket_data = eval(ticket_data)

        type = request.POST.get('type')
        root = request.POST.get('root')
        

        otp_code =  ''.join(random.choices('0123456789', k=4))
        otp_verfication = "True"

        payment_status = "success"
        payment_date = timezone.now().date()

        print(otp_code)

        if type == 'Airline':

            for person, data in ticket_data.items():
                email = data['passenger_email']
                phone = data['passenger_phone']
                address = data['passenger_address']
                gender = data['passenger_gender']
                birthday = data['passenger_birthday']
                nid_number = data['passenger_nid_number']

                airline_code = data['airline_code']
                person = data['person']
                ticket_code = data['ticket_code']
                passenger_name = data['passenger_name']
                selected_sits = data['selected_sits']

                airline = Airline.objects.filter(airline_code=airline_code).first()



                
                print(email, phone, address, gender, birthday, nid_number, airline_code, person, ticket_code, passenger_name, selected_sits)
                passenger = Airline_Ticket.objects.create(
                    name=passenger_name,
                    airline_ticket_code=ticket_code,
                    airline_class = airline.airline_class,
                    airline_from = airline.airline_from,
                    airline_to = airline.airline_to,
                    phone=phone, 
                    email=email, 
                    seat_number=selected_sits,
                    airline_date = airline.airline_date,
                    address=address, 
                    gender=gender, 
                    birthday=birthday, 
                    nid_number=nid_number,
                    payment_status = payment_status,
                    payment_date = payment_date
                    )
                passenger.save()


                context = {
                    'ticket_data': ticket_data,
                    'total_price': total_price,
                    'price': price,
                    'otp_verfication' : otp_verfication,
                    'payment_status' : payment_status,
                    'type':type,
                }

            return render(request, 'payment.html', context)
        elif type == 'Bus':
            root = BusRoots.objects.filter(root_code = root).first()
            for person, data in ticket_data.items():
                email = data['passenger_email']
                phone = data['passenger_phone']
                address = data['passenger_address']
                gender = data['passenger_gender']
                birthday = data['passenger_birthday']
                nid_number = data['passenger_nid_number']

                bus_code = data['bus_code']
                person = data['person']
                ticket_code = data['ticket_code']
                passenger_name = data['passenger_name']
                selected_sits = data['selected_sits']

                bus = Bus.objects.filter(bus_code=bus_code).first()
                



                
                print(email, phone, address, gender, birthday, nid_number, bus_code, person, ticket_code, passenger_name, selected_sits)
                passenger = Bus_Ticket.objects.create(
                    name=passenger_name,
                    bus_ticket_code=ticket_code,
                    bus_class = bus.bus_class,
                    bus_from = root.root_from,
                    bus_to = root.root_to,
                    phone=phone, 
                    email=email, 
                    seat_number=selected_sits,
                    bus_date = root.root_date,
                    address=address, 
                    gender=gender,
                    payment_status = payment_status,
                    payment_date = payment_date
                    )
                passenger.save()


                context = {
                    'ticket_data': ticket_data,
                    'total_price': total_price,
                    'price': price,
                    'otp_verfication' : otp_verfication,
                    'payment_status' : payment_status,
                    'type':type,
                    'root':root
                }
                print("ok to  create")
                print(root)
                print(type)

            return render(request, 'payment.html', context)
        # elif type == 'Hotels':
            pass
        elif type == 'Train':
            pass


