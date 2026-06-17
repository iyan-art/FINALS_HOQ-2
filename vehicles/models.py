from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=200)
    price = models.FloatField()

    def vehicle_info(self):
        return f"{self.brand} costs {self.price}"

    def __str__(self):
        return f"{self.brand} ({self.price})"


class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        return f"{self.brand} Car with {self.doors} doors costs {self.price}"


class Motorcycle(Vehicle):
    helmet_included = models.BooleanField()

    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {self.price}"

