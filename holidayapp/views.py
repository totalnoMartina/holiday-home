# import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core import serializers
from .models import Apartment, Booking, ApartmentPrice, Guest
from django.views.generic import View, ListView, FormView
from .forms import AvailabilityForm, GuestForm, AddNewBooking
# from .book_func import check_if_available


def index(request):
    """ A view to return the homepage """

    return render(request, 'holidayapp/index.html')


def apartments(request):
    """ A page to view apartments """
    apartments = Apartment.objects.all()

    template = 'holidayapp/apartments.html'
    context = {
        'apartments': apartments,
    }
    return render(request, template, context)


class ApartmentListView(ListView):
    model = Apartment


class BookingList(ListView):
    model = Booking


class ApartmentDetailView(View):
    def get(self, request, *args, **kwargs):
        apartment_name = self.kwargs.get('apartment_name', None)
        form = AvailabilityForm()
        apartment_list = Apartment.objects.filter(category=category)

        if len(apartment_list) > 0:
            apartment = apartment_list[0]
            apartment_name = dict(apartment.APARTMENTS).get(apartment.apartment_name, None)
            context = {
                'apartment_name': apartment_name,
                'form': form,
            }
            # return render(request, 'ap_detail_view.html', context)
            return JsonResponse(serializers.serialize('json', Apartment), safe=False)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        apartment_name = self.kwargs.get('apartment_name', None)
        apartment_list = Apartment.objects.filter(apartment_name=apartment_name)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_aparts = []
        for apartment in apartment_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_aparts.append(apartment)

        if len(available_aparts) > 0:
            apartment = available_aparts[0]
            booking = Booking.objects.create(
                user=self.request.user,
                apartment=apartment,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')



#####

def find_total_price(check_in, check_out, price):
    """ Get total price """
    days = check_out-check_in
    apartment_name = ApartmentPrice.objects.get(apartment_name=apartment_name)
    total = days.days * apartment_name.price
    return total


def add_booking(request):

    form = AddNewBooking()
    if request.method == 'POST':
        form = AddNewBooking(request.POST, request.FILES)
        if form.is_valid():
            booking = Booking.objects.create(
                user=request.user,
                apartment=apartment,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        form.save()
        messages.success(request, 'Booking Added Successfully')
        return redirect('bookings')

    context = {'form': form}
    return render(request, 'holidayapp/booking_page.html', context)


class BookingListView(ListView):
    """ A model to show bookings already booked """
    model = Booking
    template_name = "holidayapp/booking_page.html"

    def get_queryset(self, *args, **kwargs):

        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class CheckoutView(View):
    """ A checking ojut view """
    def get(self, request, *args, **kwargs):
        guest_form = GuestForm()
        context = {
            "guest_form": guest_form,
        }
        return render(request, 'holidayapp/checkout.html', context)

    def post(self, request, *args, **kwargs):

        guest = Guest.objects.create(
            name=guest_name,
            email=guest_email
        )
        person.save()
        context = {
            'guest': guest,
        }
