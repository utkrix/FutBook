from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, ground, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return render(request, 'myapp/signin.html')


@login_required(login_url='signin')
def findground(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('Futsalname')
        date_r = request.POST.get('date')
        ground_list = ground.objects.filter(FutsalName=source_r, date=date_r)
        if ground_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context["error"] = "Sorry no grounds availiable/all booked already!"
            return render(request, 'myapp/findground.html', context)
    else:
        return render(request, 'myapp/findground.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('Futsalname')
        seats_r = 1
        Ground = ground.objects.get(id=id_r)
        if Ground:
            if Ground.rem > int(seats_r):
                name_r = Ground.Grounds
                source_r = Ground.FutsalName
                price_r = Ground.price
                date_r = Ground.date
                time_r = Ground.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = Ground.rem - seats_r
                time_r = Ground.time
                ground.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, Grounds=name_r,
                                           FutsalName=source_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'myapp/bookings.html', locals())
            else:
                context["error"] = "Sorry, that time slot is already booked!"
                return render(request, 'myapp/findground.html', context)

    else:
        return render(request, 'myapp/findground.html')



def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'myapp/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)
