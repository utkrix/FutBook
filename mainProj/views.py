import imp
from multiprocessing import context, reduction
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import OrderForm, CreateUserForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def futsals(request):
        return render(request, 'futsals.html')

def prevBookings(request):
    return render(request, 'previousbookings.html')


def login(request):
    return render(request,'login.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Registered Successfully for" + user )
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)


