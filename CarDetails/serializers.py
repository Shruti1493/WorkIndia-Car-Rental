from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class RideSerializer(serializers.ModelField):
    class Meta:
        model = Ride
        fields = '__all__'