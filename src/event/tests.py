from django.urls import reverse
from rest_framework.test import (APITestCase, APIClient)
from rest_framework import status
from user.models import User
from user import choices
from event.models import Event

class BaseTestCase(APITestCase):
     def setUp(self):
        self.client = APIClient()
        User.objects.create_user(first_name="test", last_name="user", email="user@gmail.com",
                            password="Testing12$", user_type=choices.ADMIN)

        auth_url = '/login/'
        data = {"email": "user@gmail.com", "password": "Testing12$"}

        response = self.client.post(auth_url, data, format='json')
        token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.event = Event.objects.create(name="Modular Event Planning", summary="Modular Event Planning",
        max_seat=50, date_of_event="2023-07-16", time="10:00", duration=1, booking_open_window=2)

class EventTest(BaseTestCase):
    """
    Test cases for Event API
    """
    def setUp(self):
        super().setUp()
        self.url = '/api/event/'

    def test_create_event(self, ):
        data = {
            "name": "Modular Event Planning",
            "summary": "Modular Event Planning",
            "max_seat": 50 ,
            "date_of_event": "2023-08-20",
            "time": "10:00",
            "duration": 1,
            "booking_open_window": 2
            }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_event(self, ):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_event(self,):
        url = f'{self.url}{self.event.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        """
        Test to update Event.
        """
        data = { "max_seat_available": 100}

        response = self.client.patch(f'{self.url}{str(self.event.id)}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookingTest(BaseTestCase):
    """
    Test cases for Booking ticket
    """
    def setUp(self):
        super().setUp()
        self.url = '/api/booking/'

    def test_booking(self, ):
        data = {
            "event": self.event.id,
            "no_of_seats": 2
        }
        response = self.client.post(self.url, data, format='json')
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_booking_fail(self, ):
        event = Event.objects.create(name="Modular Event Planning", summary="Modular Event Planning",
        max_seat=50, date_of_event="2023-09-20", time="10:00", duration=1, booking_open_window=2)
        data = {
            "event": event.id,
            "no_of_seats": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
