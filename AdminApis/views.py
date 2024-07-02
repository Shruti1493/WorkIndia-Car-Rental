

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from CarDetails.models import Car
from CarDetails.serializers import CarSerializer

class AddCarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            car = serializer.save()
            return Response({
                'message': 'Car added successfully',
                'car_id': car.id,
                'status_code': 200
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)