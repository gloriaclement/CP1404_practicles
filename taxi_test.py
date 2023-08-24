"""
CP1404/CP5632 Prac_09
Test for Car class
"""
from taxi import Taxi


def main():

    my_taxi = Taxi("Prius 1", 100, 1.23)  # Create a new taxi object, my_taxi
    my_taxi.drive(40)  # Drive the taxi 40 km

    # Print the taxi's details and the current fare
    print(f"Taxi Details: {my_taxi}")
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter (start a new fare) and then drive the car 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print the details and the current fare
    print(f"\nTaxi Details: {my_taxi}")
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
