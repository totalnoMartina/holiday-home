from django.shortcuts import render
from .models import Apartment


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

