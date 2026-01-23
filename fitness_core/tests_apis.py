from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from fitness_core.models import BookingModel, FitnessClassModel
from rest_framework.test import APITestCase

from django.utils.timezone import make_aware
from datetime import datetime

class FitnessClassTests(APITestCase):
     def test_create_class_success(self):
        url = reverse("create-fitness-classes")
        data = {
            "name": "Morning Yoga",
            "date_time": "2025-06-06T10:00:00Z",
            "instructor": "Roy",
            "total_slots": 20,
            "available_slots": 10,
        }

        response = self.client.post(url, data, format="json")

        self.assertIn(
            response.status_code,
            [status.HTTP_200_OK, status.HTTP_201_CREATED]
        )
        print("RESPONSE DATA:", response.data)
        self.assertEqual(response.data['detail']["name"], "Morning Yoga")
        self.assertEqual(response.data['detail']["total_slots"], 20)
        self.assertEqual(response.data['detail']["available_slots"], 10)


#     def test_create_class_with_invalid_slots(self):
#         url = reverse("create-fitness-classes")
#         data = {
#             "name": "Yoga",
#             "date_time": "2025-06-06T10:00:00Z",
#             "instructor": "Rohit",
#             "total_slots": 10,
#             "available_slots": 20,
#         }
#         print(self)
#         response = self.client.post(url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn("WORKING ----------- Available slots cannot exceed total slots", str(response.data))


class BookingTests(APITestCase):

    def setUp(self):
        self.fitness_class = FitnessClassModel.objects.create(
            name="Evening Cardio",
            date_time=make_aware(datetime(2025, 6, 10, 18, 0, 0)),
            instructor="Admin",
            total_slots=10,
            available_slots=5,
        )
        self.url = reverse("create-bookings")

    def test_booking_success(self):
        data = {
            "client_id": "201",
            "client_name": "Aniket",
            "client_email": "aniket@gmail.com",
            "fitness_class": self.fitness_class.id,
        }

        response = self.client.post(self.url, data, format="json")

        self.assertIn(
            response.status_code,
            [status.HTTP_200_OK, status.HTTP_201_CREATED]
        )

        self.assertEqual(response.data["client_name"], "Aniket")
        self.assertEqual(response.data["fitness_class"], self.fitness_class.id)

        # 🔥 Verify slot decrement
        self.fitness_class.refresh_from_db()
        self.assertEqual(self.fitness_class.available_slots, 4)

#     def setUp(self):
#         # Create a fitness class with slots
#         self.fitness_class = FitnessClassModel.objects.create(
#             name="Testing Class",
#             date_time=make_aware(datetime(2025, 6, 10, 10, 0, 0)),
#             instructor="Test Admin",
#             total_slots=0,
#             available_slots=0,
#         )
#         self.url = reverse("create-bookings")

#     def test_booking_no_available_slots(self):
#         # Set slots to 0

#         data = {
#             "client_id": "115",
#             "client_name": "Aniket",
#             "client_email": "aniket@gmail.com",
#             "fitness_class": self.fitness_class.id,
#         }
#         response = self.client.post(self.url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn("WORKING ----------- No available slots", response.data.get("error", ""))
