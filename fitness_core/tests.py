from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import BookingModel, FitnessClassModel
from django.utils.timezone import make_aware
from datetime import datetime

class FitnessClassTests(APITestCase):

    def test_create_class_with_invalid_slots(self):
        url = reverse("create-fitness-classes")
        data = {
            "name": "Yoga",
            "date_time": "2025-06-06T10:00:00Z",
            "instructor": "Rohit",
            "total_slots": 10,
            "available_slots": 20,
        }
        print(self)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Available slots cannot exceed total slots", str(response.data))


class BookingTests(APITestCase):
    def setUp(self):
        # Create a fitness class with slots
        self.fitness_class = FitnessClassModel.objects.create(
            name="Testing Class",
            date_time=make_aware(datetime(2025, 6, 10, 10, 0, 0)),
            instructor="Test Admin",
            total_slots=0,
            available_slots=0,
        )
        self.url = reverse("create-bookings")

    def test_booking_no_available_slots(self):
        # Set slots to 0

        data = {
            "client_id": "115",
            "client_name": "Aniket",
            "client_email": "aniket@gmail.com",
            "fitness_class": self.fitness_class.id,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("No available slots", response.data.get("error", ""))
