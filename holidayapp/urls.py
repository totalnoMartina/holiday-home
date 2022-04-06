from django.urls import path
from . import views


APP_NAME = 'holidayapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('apartments/', views.apartments, name='apartments'),
    path('booking_page/', views.BookingView.as_view(), name='bookings'),
    path('booking_list/', views.BookingListView.as_view(), name='booking_list'),
    path('app_list_view/', views.ApartmentListView, name='ApartmentList'),
    path('apartment/<apartment_name>', views.ApartmentDetailView.as_view(), name='ApartmentDetailView'),
    path('booking/cancel/<pk>', views.CancelBookingView.as_view(), name='CancelBookingView'),

]
