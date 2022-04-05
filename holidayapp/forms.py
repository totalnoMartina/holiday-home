from datetime import datetime
from django import forms
from django.core import serializers
# from django.conf import settings
from django.core.exceptions import ValidationError
from .models import Apartment, Booking, Guest


class AddNewBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingForm(forms.Form):
    """ A form to check if apartment is available """

    apartment_name = forms.ModelChoiceField(
        queryset=Apartment.objects.all())
    check_in = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", ])

   


    def checking_hours(self, start, end):
        """ For the times to check in and out """
        check_in = self.cleaned_data.get('check_in')
        check_out = self.cleaned_data.get('check_out')
        # This ensures that check_in and check_out are between start and end of your working hours.
        if not(check_in < start and check_out < end):
            raise ValidationError(
                "Not available, please enter value within working hours")
        else:
            return self.cleaned_data


class GuestForm(forms.ModelForm):
    """ a model for the guest """
    class Meta:
        model = Guest
        fields = '__all__'
