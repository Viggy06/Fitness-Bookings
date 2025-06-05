import datetime
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BookingModel, FitnessClassModel
from .pagination import CustomPagination

from .serializers import BookingSerializer, FitnessClassSerializer
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class FitnessClassListAPI(generics.ListAPIView):
    queryset = FitnessClassModel.objects.order_by("-id")
    serializer_class = FitnessClassSerializer
    pagination_class = CustomPagination


class FitnessClassCreateAPI(APIView):

    def post(self, request):
        try:
            serializer = FitnessClassSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                logger.info(
                    f"Fitness class created successfully {datetime.datetime.now()}"
                )

                return Response(
                    {
                        "detail": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )    

            logger.warning(f"Invalid fitness class data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"Error creating fitness class due to - {e}")
            return Response(
                {"detail": "Something went wrong!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BookingGetPostAPI(APIView):
    def get(self, request):
        email = request.query_params.get("email")
        queryset = BookingModel.objects.order_by("-id")
        if not queryset:
            return Response({"detail": "No data found"}, status=status.HTTP_200_OK)

        if email:
            queryset = queryset.filter(client_email = email)

        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            fitness_class = serializer.validated_data["fitness_class"]


            if fitness_class.available_slots <= 0:
                logger.warning(
                    f"No slots available for class {fitness_class.name} - (id: {fitness_class.id})"
                )
                return Response(
                    {"error": "No available slots for this fitness class."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            logger.info(
                f"Booking successfull for client-{request.data.get("email")} at {datetime.datetime.now()}"
            )
            fitness_class.available_slots -= 1
            fitness_class.save()

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
