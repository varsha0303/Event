from rest_framework import viewsets
from rest_framework.response import Response

from event.models import (Event, Booking)
from event.serializer import (EventSerializer, BookingSerializer)
from event.permission import (EventPermission, BookingPermission)
from user import choices

# Create your views here.
class EvenViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (EventPermission, )

    def get_queryset(self, ):
        return Event.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = (BookingPermission, )

    def get_queryset(self, ):
        if self.request.user.user_type == choices.ADMIN:
            return Booking.objects.all().order_by('event__date_of_event')

        return Booking.objects.filter(user=self.request.user).order_by('event__date_of_event')
