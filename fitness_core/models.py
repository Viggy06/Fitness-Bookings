from django.db import models
import pytz
from django.utils.timezone import is_naive

# Create your models here.


class FitnessClassModel(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if is_naive(self.date_time):
            ist = pytz.timezone('Asia/Kolkata')
            self.date_time = ist.localize(self.date_time).astimezone(pytz.UTC)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.instructor}"


class BookingModel(models.Model):
    client_id = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField()
    fitness_class = models.ForeignKey(FitnessClassModel, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return f"{self.client_email} - {self.fitness_class}"

