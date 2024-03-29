# import datetime
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, FormView, DeleteView
from .models import Apartment, Booking, ApartmentPrice, Guest
from .forms import AddNewBooking, BookingForm
from .book_func import check_if_available


def index(request):
    """ A view to return the homepage """

    return render(request, 'holidayapp/index.html')


def apartments(request):
    """ A page to view apartments """
    apartmentss = Apartment.objects.all()

    template = 'holidayapp/apartments.html'
    context = {
        'apartments': apartmentss,
    }
    return render(request, template, context)


class BookingListView(ListView):
    """ A view to see all booked events """
    model = Booking
    template_name = "booking_list.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return redirect('succesfully_booked.html')
        return render(request, template_name)


class ApartmentDetailView(View):
    """ A view that guides to booking and apartment """
    def get(self, request, *args, **kwargs):
        apartment_name = self.kwargs.get('apartment_name', None)
        apartment_url = get_object_or_404(Apartment, pk=apartment_name)
        form = BookingForm(request.GET)
        apartment_list = Apartment.objects.filter(apartment_name=apartment_name)

        if apartment_list:
            apartments = apartment_list[0]
            apartment_name = dict(apartments.APARTMENTS).get(apartments.apartment_name, None)
            context = {
                'apartment_name': apartment_name,
                'apartment_url': apartment_url,
                'form': form,
            }
            return render(request, 'holidayapp/detail_view.html', context)
        else:
            return HttpResponse('Category does not existsss')

    def post(self, request, *args, **kwargs):
        apartment_name = self.kwargs.get('apartment_name', None)
        apartment_list = Apartment.objects.filter(apartment_name=apartment_name)
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

        available_aparts = []
        for apartment in apartment_list:
            # if check_if_available(apartment, data['check_in'], data['check_out']):
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
            messages.add_message(request, messages.SUCCESS, 'Thank you, your booking is requested!')
            # return redirect('succesfully_booked.html')
            # return reverse_lazy('booking_list')

            return redirect('home')
            # return render(request, 'holidayapp/apartments.html')
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')


def ApartmentListView(request):
    """ See the list of apartments """
    apartment = Apartment.objects.all()[1]
    apartment_names = dict(apartment.APARTMENTS)
    apartment_values = apartment_names.keys()
    apart_list = []

    for apartment_name in apartment_names:
        apartment = apartment_names.get(apartment_name)
        apartment_url = reverse_lazy('ApartmentList', kwargs={
                           'apartment_name': apartment_name, })

        apart_list.append((apartment, apartment_url))
    context = {
        "apartment_list": apart_list,
    }
    return render(request, 'holidayapp/detail_view.html', context)


class BookingView(FormView):
    """ A view to see bookings """
    form_class = BookingForm
    template_name = 'holidayapp/booking_page.html'

    def form_valid(self, form):
        data = form.cleaned_data
        apartment_list = Apartment.objects.filter(apartment_name=data['apartment_name'])
        available_aparts = []
        for apartment in apartment_list:
            # if check_if_available(apartment, data['check_in'], data['check_out']):
            #     available_aparts.append(apartment)

            if len(available_aparts) > 0:
                apartment = available_aparts[0]
                booking = Booking.objects.create(
                    user=self.request.user,
                    apartment=apartment,
                    check_in=data['check_in'],
                    check_out=data['check_out']
                )
                booking.save()
                return reverse_lazy('booking_list')
                # return HttpResponse(booking)
            else:
                return HttpResponse('This apartment is already booked, please try another one')
        return HttpResponse('The apartment is booked')


class CancelBookingView(DeleteView):
    """ A view to cancel bookings """
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('booking_list')
