import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from mainProj import views
urlpatterns = [
    path('', views.index, name="home"),
    path('futsals', views.futsals, name="futsals"), 
    path('previousbookings', views.prevBookings, name="PreviousBookings"),
    path('authentication', views.authentication, name="authentication")

]