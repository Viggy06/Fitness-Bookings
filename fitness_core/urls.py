from django.urls import path

from .views import BookingGetPostAPI, FitnessClassCreateAPI, FitnessClassListAPI


urlpatterns = [
    path("get-all-classes/", FitnessClassListAPI.as_view(), name="get-all-fitness-classes"),
    path("create-fitness-classes/", FitnessClassCreateAPI.as_view(), name="create-fitness-classes"),

    #Booking
    path("get-all-bookings/", BookingGetPostAPI.as_view(), name="get-all-bookings"),
    path("create-booking/", BookingGetPostAPI.as_view(), name="create-bookings"),
]
