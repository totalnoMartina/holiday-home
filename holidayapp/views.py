from django.shortcuts import render, HttpResponse
from .models import Apartment, Booking, Guest, ApartmentPrice
from django.views.generic import View
from .forms import AvailabilityForm, GuestForm


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
            request.session['amount'] = find_total_room_charge(
                    data['check_in'], data['check_out'], data['apartment_name'])
            return redirect('holidayapp:CheckoutView')
        return HttpResponse('form not valid', form.errors)


class CheckoutView(View):

    def get(self, request, *args, **kwargs):
        guest_form = GuestForm()
        context = {
            "guest_form": guest_form,

        }
        return render(request, 'checkout.html', context)
