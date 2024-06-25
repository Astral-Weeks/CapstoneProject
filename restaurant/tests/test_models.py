from django.test import TestCase
from restaurant.models import Booking
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

# ///////////////////////////////////////////////////////////////
# Tests on the User API

class UserTest(TestCase):
    def test_create_user(self):
        item = User.objects.create(username="Mindy", email="mindy@mindymail.com", password="mindylittlelemon")
        self.assertEqual(item.username, 'Mindy')
        self.assertEqual(item.email, 'mindy@mindymail.com')
        self.assertEqual(item.password, 'mindylittlelemon')


# ///////////////////////////////////////////////////////////////
# Tests on the Booking API

class BookingTest(TestCase):
    def test_booking(self):
        # creating user
        User.objects.create(username="Joanna234", email="jo234@jmail.com", password="joannalittlelemon")
        user = User.objects.get(username='Joanna234')
        # creating booking with simulated authentication
        booking = Booking.objects.create(username=user, Name="Joanna", No_of_guests="3", BookingDate="2024-09-02")
        force_authenticate(booking, user=user)
        bookingstr = booking.get_booking()
        # expected result
        self.assertEqual(bookingstr, 'Joanna : 3 : 2024-09-02')

class BookingTest2(TestCase):
    def test_booking(self):
        # creating user
        User.objects.create(username="Amir22", email="amir@awesomemail.com", password="amirlittlelemon")
        amir = User.objects.get(username='Amir22')
        # creating booking with simulated authentication
        booking = Booking.objects.create(username=amir, Name="Amir", No_of_guests="2", BookingDate="2024-10-03")
        force_authenticate(booking, user=amir)
        bookingstr = booking.get_booking()
        # expected result
        self.assertEqual(bookingstr, 'Amir : 2 : 2024-10-03')

    def test_delete_booking(self):
        booking = Booking.objects.filter(Name="Amir", No_of_guests="2", BookingDate="2024-10-03")
        booking.delete()
        self.assertEqual(Booking.objects.count(), 0)