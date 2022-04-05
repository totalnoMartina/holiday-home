from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking_page/', views.BookingView.as_view(), name='bookings'),
    path('booking_list/', views.BookingListView.as_view(), name='booking_list'),
    path('apartment/<apartment_name>', views.ApartmentDetailView.as_view(), name='ApartmentDetailView'),

]
