from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import datetime
import json
from django.urls import reverse, reverse_lazy
from .models import Apartment, Booking, Guest, ApartmentPrice
from django.views.generic import View, ListView
from .forms import AvailabilityForm, GuestForm
from .book_func import check_if_available


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

def find_total_price(check_in, check_out, price):
    """ Get total price """
    days = check_out-check_in
    apartment_name = ApartmentPrice.objects.get(apartment_name=apartment_name)
    total = days.days * apartment_name.price
    return total


class ApartmentsListView(ListView):
    """  A view to see all apartments """
    model = Apartment


class BookingView(View):
    """ A function to ask for bookings from user side """
    def get(self, request, *args, **kwargs):
        if "check_in" in request.session:
            s = request.session
            form_data = {
                "check_in": s['check_in'], "check_out": s['check_out'], "apartment_name": s['apartment_name']}
            form = AvailabilityForm(request.POST or None, initial=form_data)
        else:
            form = AvailabilityForm()
        return render(request, 'holidayapp/booking_page.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request.session['check_in'] = data['check_in'].strftime(
                    "%Y-%m-%dT%H:%M")
            request.session['check_out'] = data['check_out'].strftime(
                    "%Y-%m-%dT%H:%M")
            request.session['apartment_name'] = data['apartment_name']
            return redirect('/')
        return HttpResponse('form not valid', form.errors)


class BookingListView(ListView):
    """ A model to show bookings already booked """
    model = Booking
    template_name = "holidayapp/booking_page_view.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class ApartmentsBooked(View):
    """ A view to see apartments """
    def get(self, request, *args, **kwargs):
        print(self.request.user)
        apartment_name = self.kwargs.get('apartment_name', None)
        form = AvailabilityForm()
        app_list = Apartment.objects.filter(apartment_name=apartment_name)

        if len(app_list) > 0:
            apartment = app_list[0]
            apartment_name = dict(apartment.APARTMENTS).get(apartment.apartment_name, None)
            context = {
                'apartment_name': apartment_name,
                'form': form,
            }
            return render(request, 'booking_page.html', context)
        else:
            return HttpResponse('Apartment name does not exist')

    def post(self, request, *args, **kwargs):
        apartment_name = self.kwargs.get('apartment_name', None)
        app_list = Apartment.objects.filter(apartment_name=apartment_name)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
        avail_apartments = []

        for apartment in avail_apartments:
            if check_if_available(apartment, data['check_in'], data['check_out']):
                avail_apartments.append(apartment)

        if len(avail_apartments) > 0:
            apartment = avail_apartments[0]

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
