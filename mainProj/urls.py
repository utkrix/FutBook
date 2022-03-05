import imp
from django.contrib import admin
from django.urls import path, include
from mainProj import views
urlpatterns = [
    path('', views.index, name="home") 
]