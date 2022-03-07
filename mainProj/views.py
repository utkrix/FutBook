from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
 #   return HttpResponse("Home@proj")

def futsals(request):
        return render(request, 'futsals.html')

def prevBookings(request):
    return render(request, 'previousbookings.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
        return render (request=request, template_name="main/register.html", context={"register_form":form})