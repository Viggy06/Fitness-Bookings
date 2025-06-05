from rest_framework import serializers

from .models import BookingModel, FitnessClassModel


class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClassModel
        fields = "__all__"

    def validate(self, data):
        if data["available_slots"] > data["total_slots"]:
            raise serializers.ValidationError(
                "Available slots cannot exceed total slots"
            )
        return data


class BookingSerializer(serializers.ModelSerializer):
    fitness_class_name = serializers.CharField(source="fitness_class.name", read_only=True)
    class Meta:
        model = BookingModel
        fields = "__all__"
