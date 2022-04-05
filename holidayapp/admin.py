from django.contrib import admin
from .models import Apartment, Booking, Guest, ApartmentPrice


admin.site.register(Apartment)
admin.site.register(Booking)
admin.site.register(Guest)
admin.site.register(ApartmentPrice)
