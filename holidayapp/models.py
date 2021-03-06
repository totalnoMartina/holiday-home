from django.db import models
from django.contrib.auth.models import User


class Apartment(models.Model):
    """ A model for apartment """
    APARTMENTS = (('Tony', 'Tony Apartment for max4 people'),
                ('Matea', 'Matea apartment for max4 people'),
                ('Martina', 'Martina apartment for max6 people'))
    apartment_name = models.CharField(choices=APARTMENTS, max_length=10, primary_key=True)
    beds_nr = models.IntegerField()
    guest_nr = models.IntegerField()
    description = models.TextField(name='description', null=True)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    image7 = models.ImageField(blank=True)
    image8 = models.ImageField(blank=True)

    def __str__(self):
        """ Showing apartment class model created """
        return f' {self.apartment_name} with {self.beds_nr} beds.'


class ApartmentPrice(models.Model):
    """ Getting the price of the apartment """
    APARTMENTS_PRICES = (('Tony', '80.00'),
                ('Matea', '80.00'),
                ('Martina', '120.00'))
    apartment_name = models.CharField(choices=APARTMENTS_PRICES, max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f'{self.apartment_name} has a price of {self.price}'


class Booking(models.Model):
    """ A model for details of the booking """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'A {self.user} has booked {self.apartment} from {self.check_in} until {self.check_out}'


class Guest(models.Model):
    """ About the guest """
    name = models.CharField(max_length=100)
    email = models.EmailField()
