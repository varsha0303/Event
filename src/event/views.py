from rest_framework import viewsets

from event.models import (Event, Booking)
from event.serializer import (EventSerializer, BookingSerializer)
from event.permission import (EventPermission, BookingPermission)
from user import choices

# Create your views here.
class EvenViewSet(viewsets.ModelViewSet):
    """
    Event View
    """
    serializer_class = EventSerializer
    permission_classes = (EventPermission, )

    def get_queryset(self, ):
        # All events are avaialble for users
        return Event.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    """
    Booking View
    """
    serializer_class = BookingSerializer
    permission_classes = (BookingPermission, )

    def get_queryset(self, ):
        # If logged in user is Admin then return all bookings with sorted date of events
        if self.request.user.user_type == choices.ADMIN:
            return Booking.objects.all().order_by('event__date_of_event')

        # If logged in user is not Admin then return all bookings of that particular user
        # with sorted date of events
        return Booking.objects.filter(user=self.request.user).order_by('event__date_of_event')
