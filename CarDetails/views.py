
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class RideDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        origin = request.GET.get('origin')
        category = request.GET.get('cat')
        destination = request.GET.get('dest')
        required_hours = int(request.GET.get('rh'))

        if not origin or not category:
            return Response({"error": "Required parameters missing"}, status=status.HTTP_400_BAD_REQUEST)

        cars = Car.objects.filter(current_city=origin, category=category)
        available_cars = []

        for car in cars:
            car_data = CarSerializer(car).data
            car_data['total_payable_amt'] = car.rent_per_hr * required_hours
            available_cars.append(car_data)

        return Response(available_cars)



class Rent_Car(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        car_id = request.data.get('car_id')
        origin = request.data.get('origin')
        destination = request.data.get('dest')
        hours_requirement = request.data.get('hr')

        try:
            car = Car.objects.get(id=car_id)
            amountofrent = int(car.rent_per_hr) * int(hours_requirement)
            ride = Ride.objects.create(
                car=car,
                origin=origin,
                destination=destination,
                hours_requirement=hours_requirement,
                amount=amountofrent
            )

            car.rent_history.append({
                'origin': origin,
                'destination': destination,
                'amount': ride.amount
            })
            car.save()


            return Response({
                'status': 'Car rented successfully',
                'status_code': status.HTTP_200_OK,
                'rent_id': ride.id,
                'total_payable_amt': amountofrent
            })

        except Car.DoesNotExist:
            return Response({
                'status': 'No car available at the moment',
                'status_code': status.HTTP_404_NOT_FOUND
            })



class Post_Save(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        car_id = request.data.get('car_id')
        origin = request.data.get('origin')
        destination = request.data.get('dest')
        hours_requirement = request.data.get('hr')

        try:
            car = Car.objects.get(id=car_id)
            amountofrent = int(car.rent_per_hr) * int(hours_requirement)
           

            car.rent_history.append({
                'origin': origin,
                'destination': destination,
                'amount': amountofrent
            })
            car.save()


            return Response({
                'status': 'Cars rent history updated successfully',
                'status_code': status.HTTP_200_OK,
               
            })

        except Car.DoesNotExist:
            return Response({
                'status': 'No car available at the moment',
                'status_code': status.HTTP_404_NOT_FOUND
            })
