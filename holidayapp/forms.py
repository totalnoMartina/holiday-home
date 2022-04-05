from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from .models import Apartment, Guest

class AvailabilityForm(forms.Form):
    """ A form to check if apartment is available """

    check_in = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    apartment_name = forms.ModelChoiceField(
        queryset=Apartment.objects.all())
    #  widget=forms.Select(attrs={"class": "mdb-select md-form"})

class GuestForm(forms.ModelForm):
    """ a model for the guest """
    class Meta:
        model = Guest
        fields = '__all__'