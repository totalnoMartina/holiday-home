import datetime
from holidayapp.models import Booking, Apartment


def check_if_available(apartment, check_in, check_out):
    """ Checking if the apartment is already booked """
    vacant_list = []
    booked_list = Booking.objects.filter(apartment=apartment)
    for booking in booked_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            vacant_list.append(True)
        else:
            vacant_list.append(False)
    return all(vacant_list)
