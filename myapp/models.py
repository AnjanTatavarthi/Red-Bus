import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone


class BusInfo(models.Model):
    bus_name=models.CharField(max_length=128)
    type=models.CharField(max_length=128)
    arriving_time=models.TimeField(choices=(

        (datetime.datetime.strptime('1:00 am', "%I:%M %p").time(), '1:00 am'),
        (datetime.datetime.strptime('2:00 am', "%I:%M %p").time(), '2:00 am'),
        (datetime.datetime.strptime('3:00 am', "%I:%M %p").time(), '3:00 am'),
        (datetime.datetime.strptime('4:00 am', "%I:%M %p").time(), '4:00 am'),
        (datetime.datetime.strptime('5:00 am', "%I:%M %p").time(), '5:00 am'),
        (datetime.datetime.strptime('6:00 am', "%I:%M %p").time(), '6:00 am'),
        (datetime.datetime.strptime('7:00 am', "%I:%M %p").time(), '7:00 am'),
        (datetime.datetime.strptime('8:00 am', "%I:%M %p").time(), '8:00 am'),
        (datetime.datetime.strptime('9:00 am', "%I:%M %p").time(), '9:00 am'),
        (datetime.datetime.strptime('10:00 am', "%I:%M %p").time(), '10:00 am'),

        (datetime.datetime.strptime('11:00 am', "%I:%M %p").time(), '11:00 am'),
        (datetime.datetime.strptime('12:00 pm', "%I:%M %p").time(), '12:00 pm'),
        (datetime.datetime.strptime('1:00 pm', "%I:%M %p").time(), '1:00 pm'),
        (datetime.datetime.strptime('2:00 pm', "%I:%M %p").time(), '2:00 pm'),
        (datetime.datetime.strptime('3:00 pm', "%I:%M %p").time(), '3:00 pm'),
        (datetime.datetime.strptime('4:00 pm', "%I:%M %p").time(), '4:00 pm'),
        (datetime.datetime.strptime('5:00 pm', "%I:%M %p").time(), '5:00 pm'),
        (datetime.datetime.strptime('6:00 pm', "%I:%M %p").time(), '6:00 pm'),
        (datetime.datetime.strptime('7:00 pm', "%I:%M %p").time(), '7:00 pm'),
        (datetime.datetime.strptime('8:00 pm', "%I:%M %p").time(), '8:00 pm'),
        (datetime.datetime.strptime('9:00 pm', "%I:%M %p").time(), '9:00 pm'),
        (datetime.datetime.strptime('10:00 pm', "%I:%M %p").time(), '10:00 pm'),
        (datetime.datetime.strptime('11:00 pm', "%I:%M %p").time(), '11:00 pm'),
        (datetime.datetime.strptime('12:00 am', "%I:%M %p").time(), '12:00 am'),


    ))
    departure_time=models.TimeField(choices=(

        (datetime.datetime.strptime('1:00 am', "%I:%M %p").time(), '1:00 am'),
        (datetime.datetime.strptime('2:00 am', "%I:%M %p").time(), '2:00 am'),
        (datetime.datetime.strptime('3:00 am', "%I:%M %p").time(), '3:00 am'),
        (datetime.datetime.strptime('4:00 am', "%I:%M %p").time(), '4:00 am'),
        (datetime.datetime.strptime('5:00 am', "%I:%M %p").time(), '5:00 am'),
        (datetime.datetime.strptime('6:00 am', "%I:%M %p").time(), '6:00 am'),
        (datetime.datetime.strptime('7:00 am', "%I:%M %p").time(), '7:00 am'),
        (datetime.datetime.strptime('8:00 am', "%I:%M %p").time(), '8:00 am'),
        (datetime.datetime.strptime('9:00 am', "%I:%M %p").time(), '9:00 am'),
        (datetime.datetime.strptime('10:00 am', "%I:%M %p").time(), '10:00 am'),

        (datetime.datetime.strptime('11:00 am', "%I:%M %p").time(), '11:00 am'),
        (datetime.datetime.strptime('12:00 pm', "%I:%M %p").time(), '12:00 pm'),
        (datetime.datetime.strptime('1:00 pm', "%I:%M %p").time(), '1:00 pm'),
        (datetime.datetime.strptime('2:00 pm', "%I:%M %p").time(), '2:00 pm'),
        (datetime.datetime.strptime('3:00 pm', "%I:%M %p").time(), '3:00 pm'),
        (datetime.datetime.strptime('4:00 pm', "%I:%M %p").time(), '4:00 pm'),
        (datetime.datetime.strptime('5:00 pm', "%I:%M %p").time(), '5:00 pm'),
        (datetime.datetime.strptime('6:00 pm', "%I:%M %p").time(), '6:00 pm'),
        (datetime.datetime.strptime('7:00 pm', "%I:%M %p").time(), '7:00 pm'),
        (datetime.datetime.strptime('8:00 pm', "%I:%M %p").time(), '8:00 pm'),
        (datetime.datetime.strptime('9:00 pm', "%I:%M %p").time(), '9:00 pm'),
        (datetime.datetime.strptime('10:00 pm', "%I:%M %p").time(), '10:00 pm'),
        (datetime.datetime.strptime('11:00 pm', "%I:%M %p").time(), '11:00 pm'),
        (datetime.datetime.strptime('12:00 am', "%I:%M %p").time(), '12:00 am'),


    ))
    fare=models.IntegerField()
    source=models.CharField(max_length=128)
    destination=models.CharField(max_length=128)
    date_of_journey=models.DateField()
    no_of_seats = models.IntegerField(default=60)
    available_seats=models.IntegerField()

    def __str__(self):
        return self.bus_name


class TicketInfo(models.Model):#amount


    booking_date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=128)
    phone_no=models.CharField(max_length=20)
    no_of_tickets = models.IntegerField(default=0)
    total_amount=models.IntegerField(default=0)

    bus = models.ForeignKey(BusInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __int__(self):
        return self.id


class PassengerInfo(models.Model):

    name=models.CharField(max_length=128)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    seat_no = models.CharField(max_length=10)
    ticket=models.ForeignKey(TicketInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




admin.site.register(PassengerInfo)
admin.site.register(BusInfo)
admin.site.register(TicketInfo)