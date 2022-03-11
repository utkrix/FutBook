from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('findground', views.findground, name="findground"),
    path('bookings', views.bookings, name="bookings"),
    path('signup/', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),

]
