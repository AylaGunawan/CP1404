"""
CP1404 - Practical 08
Unreliable Car Class
"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an UnreliableCar object, a specialised version of Car that includes reliability."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only if reliability is equal or greater than a random number."""
        random_number = randint(1, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
