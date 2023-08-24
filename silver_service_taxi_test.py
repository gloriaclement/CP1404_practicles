from Prac_09.silver_service_taxi import SilverServiceTaxi

# Test code
if __name__ == "__main__":
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 2.0)

    # Drive the taxi 18 km
    my_silver_taxi.drive(18)

    # Calculate and print the fare
    fare = my_silver_taxi.get_fare()
    print(f"Total Fare: ${fare:.2f}")
