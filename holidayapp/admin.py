from django.contrib import admin
from .models import Apartment, Booking, Guest


admin.site.register(Apartment)
admin.site.register(Booking)
admin.site.register(Guest)
