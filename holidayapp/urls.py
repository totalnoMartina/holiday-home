from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking_page/', views.BookingView.as_view(), name='bookings'),
]
