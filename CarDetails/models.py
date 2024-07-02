from django.db import models

# Create your models here.

class Car(models.Model):
    category = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20, unique=True)
    current_city = models.CharField(max_length=100)
    rent_per_hr = models.DecimalField(max_digits=10, decimal_places=2)
    rent_history = models.JSONField(default=list)

    def __str__(self):
        return f"{self.category} - {self.model} ({self.number_plate})"

class Ride(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    hours_requirement = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"