# Create your models here.
from multiprocessing.sharedctypes import Value
from pyexpat import model
from random import random
from statistics import mode
from django import conf
from django.db import models
import random 
from django.utils.crypto import get_random_string
# Create your models here.
conf_code = get_random_string(length=5)
class ground(models.Model):
    Grounds = models.CharField(max_length=40)
    FutsalName = models.CharField(max_length=30)
    gname = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.CharField(max_length=30)
    code = models.CharField(default=conf_code, max_length=5)
    def __str__(self):
        return self.Grounds


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    Booking_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    Grounds = models.CharField(max_length=30)
    FutsalName = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.CharField(max_length=30)
    status = models.CharField(choices=Booking_STATUSES, default=BOOKED, max_length=2)
    code = models.CharField(default=conf_code, max_length=5)
    

    def __str__(self):
        return self.email
        
