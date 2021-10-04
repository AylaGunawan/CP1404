"""
CP1404 - Practical 08
Silver Service Taxi Test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():  # for testing
    """Silver service taxi test client code."""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    tesla = SilverServiceTaxi("Tesla", 100, 2)
    print(tesla)
    print(f"{tesla.name} drove {tesla.drive(18)} km")
    print(tesla)
    print(f"For an {tesla.odometer} km trip in a {tesla.name} with fanciness of {tesla.fanciness}, the fare should be "
          f"${tesla.get_fare()}")
    tesla.start_fare()
    print(tesla)
    tesla.add_fuel(50)
    print(tesla)


main()
