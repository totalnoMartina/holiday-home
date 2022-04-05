from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking_page/', views.BookingView.as_view(), name='bookings'),
    path('apartments_booked/', views.ApartmentsBooked.as_view(), name='apartments_booked'),
    path('checkout/', views.CheckoutView.as_view(), name='CheckoutView'),

]
