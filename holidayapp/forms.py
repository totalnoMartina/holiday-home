from django import forms
from django.conf import settings
from datetime import datetime
from django.core.exceptions import ValidationError
from .models import Apartment, Guest

class AvailabilityForm(forms.Form):
    """ A form to check if apartment is available """

    check_in = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", ], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", ], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    apartment_name = forms.ModelChoiceField(
        queryset=Apartment.objects.all())

    def checking_hours(self, start, end):
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