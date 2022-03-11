from django.contrib import admin
from .models import ground, User, Book

# Register your models here.

admin.site.register(ground)
admin.site.register(User)
admin.site.register(Book)


