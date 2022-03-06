from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
 #   return HttpResponse("Home@proj")

def futsals(request):
        return render(request, 'futsals.html')

def prevBookings(request):
    return render(request, 'previousbookings.html')

def authentication(request):
    return render(request, 'authentications.html')