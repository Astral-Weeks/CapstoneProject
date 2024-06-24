from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    BookingDate = models.DateField()

    def __str__(self):
        return self.Name
    
    def get_booking(self):
        return f'{self.Name} : {str(self.No_of_guests)} : {str(self.BookingDate)}'


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    Inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

    def get_item(self):
        return f'Title: {self.Title}  Price: {str(self.Price)}  Inventory: {self.Inventory}'
