from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import User
from event import choices

# Create your models here.
class Event(models.Model):
    """
    This model stores information about Event
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(_('Name Of Event'), max_length=255)
    summary = models.TextField(_('Summary'))
    event_type = models.CharField(_('Gender'), choices=choices.EVENT_TYPE, max_length=255, default=choices.ONLINE)
    max_seat = models.BigIntegerField(_('Max Seat'))
    date_of_event = models.DateField(_('Date Of Event'))
    time = models.TimeField(_('Time Of Event'))
    duration = models.IntegerField(_('Duration of Event'))
    # Booking open window duration is default one month prior until the actual event date (Including actual event date)
    booking_open_window = models.IntegerField(_('Booking Open Window'), default=1)

    def __str__(self):
        return f'{self.name} {self.date_of_event}'


class Booking(models.Model):
    """
    This model stores information about Event booking by User
    """
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_booking')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_booking')
    booking_time = models.DateTimeField(_('Booking time'), default=timezone.now)
    no_of_seats = models.IntegerField(_('No of seats'))

    def __str__(self):
        return f'{self.event} {self.user}'
