from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking_page/', views.BookingView.as_view(), name='bookings'),
    path('apartment/<apartment_name>', views.ApartmentDetailView.as_view(), name='ApartmentDetailView'),
    path('checkout/', views.CheckoutView.as_view(), name='CheckoutView'),

]
