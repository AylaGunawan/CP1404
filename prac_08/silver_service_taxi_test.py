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
    print(f"Fare should be $48.80: ${tesla.get_fare():.2f}")  # with Inheriting Enhancements applied
    print(tesla)
    tesla.start_fare()
    print(tesla)
    tesla.add_fuel(50)
    print(tesla)


main()
