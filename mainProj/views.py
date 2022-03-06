from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    return HttpResponse("Home@proj")

def about(request):
    return HttpResponse("About@proj")

def prevBookings(requests):
    return HttpResponse("Previous_Bookings@proj")
