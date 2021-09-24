"""
CP1404 - Practical 08
Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar


def main():  # for testing
    """Unreliable car test client code."""
    old_car = UnreliableCar("Old Car", 100, 50)
    print(old_car)
    print(f"{old_car.name} drove {old_car.drive(25)} km")
    print(old_car)
    old_car.add_fuel(75)
    print(old_car)
    print(f"{old_car.name} drove {old_car.drive(100)} km")
    print(old_car)


main()
