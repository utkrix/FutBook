import imp
from multiprocessing import context, reduction
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import OrderForm, CreateUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Registered Successfully for " + user )
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)


def index(request):
    return render(request, 'index.html')

def futsals(request):
        return render(request, 'futsals.html')

def prevBookings(request):
    return render(request, 'previousbookings.html')
