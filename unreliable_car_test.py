"""
CP1404/CP5632 Prac_09
Test for Unreliable car
"""
from Prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("UnreliableCar 1", 50, 70)  # Example reliability value: 70%
distance_driven = my_car.drive(30)  # This will depend on the random reliability check
if distance_driven > 0:
    print(f"Car successfully drove {distance_driven} km.")
else:
    print("Car failed to start due to low reliability.")
