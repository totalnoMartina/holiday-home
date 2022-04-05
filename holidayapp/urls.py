from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apartments/', views.apartments_view, name='apartments'),
    path('booking_page/', views.BookingView.as_view(), name='bookings'),
]
