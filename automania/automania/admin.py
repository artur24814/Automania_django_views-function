from django.contrib import admin

from .models import Car, Order, Messeges, ReadedMesseges

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Messeges)
admin.site.register(ReadedMesseges)
