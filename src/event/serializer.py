from datetime import datetime
from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from event.models import (Event, Booking)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'summary', 'max_seat', 'date_of_event', 'time', 'duration', 'booking_open_window')
        read_only_fields = ('id',)



class BookingSerializer(FlexFieldsModelSerializer):

    def create(self, validated_data):
        """
        While booking user have to add event id and no_of_seats
        which user's this booking is set here (Logged in user will be set to user)
        """
        validated_data['user'] = self.context['request'].user
        return Booking.objects.create(**validated_data)

    def validate(self, data):
        """
        Validation for booking a ticket for an event
        """
        today = datetime.today().date()

        # If date of event is passed then user cannot book a ticket
        if today > data['event'].date_of_event :
            raise serializers.ValidationError({'error': f'Cannot book a ticket because booking window is closed on {data["event"].date_of_event}.'})

        # If date of event is not between the booking window then user cannot book a ticket
        # (Date of event - booking window) is the booking window time
        # Booking window should be no. of months
        if today < (data['event'].date_of_event + relativedelta(months=-data["event"].booking_open_window)):
            raise serializers.ValidationError({'error': f'Cannot book a ticket because booking window is not opened yet, please book ticket for this event on or after {data["event"].date_of_event + relativedelta(months=-data["event"].booking_open_window)}'})

        return data


    class Meta:
        model = Booking
        fields = ('id', 'event', 'no_of_seats', 'booking_time')
        read_only_fields = ('id', 'user')
        expandable_fields = {'event': (EventSerializer)}