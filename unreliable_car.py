"""
CP1404/CP5632 Prac_09
Unreliable car program
"""
from Prac_06.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on the parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than the car's reliability."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)  # Call the drive method from the base class (Car)
        else:
            return 0  # Car didn't start due to low reliability
