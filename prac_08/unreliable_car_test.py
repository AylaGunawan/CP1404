"""
CP1404 - Practical 08
Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar


def main():  # for testing
    """Unreliable car test client code."""
    old_car = UnreliableCar("Old Car", 100, 50)
    print(old_car)
    for i in range(10):
        print(f"{old_car.name} drove {old_car.drive(25)} km")
        print(old_car)


main()
