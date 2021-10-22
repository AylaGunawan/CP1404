"""
CP1404 - Practical 08
Taxi Simulator
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            print_taxis(taxis)
            chosen_taxi = get_taxi(taxis)
        elif choice == "d":
            if chosen_taxi:
                drive_distance = get_valid_distance()
                chosen_taxi.drive(drive_distance)
                print(f"Your {chosen_taxi.name} trip cost you ${chosen_taxi.get_fare():.2f}")
                bill += chosen_taxi.get_fare()
                chosen_taxi.start_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    """Print a list of taxi instances and their index."""
    for i, taxi in enumerate(taxis):
        print(i, "-", taxi)


def get_taxi(taxis):
    """Return a chosen taxi if index within range, else return an empty string."""
    while True:
        try:
            chosen_taxi_index = int(input("Choose taxi: "))
            if chosen_taxi_index > len(taxis) - 1:
                print("Invalid taxi choice")
                return None
            else:
                return taxis[chosen_taxi_index]
        except ValueError:
            print("Invalid input")


def get_valid_distance():
    """Return a valid non-negative integer for distance, else return 0."""
    while True:
        try:
            distance = int(input("Drive how far? "))  # -ve distance?
            if distance < 0:
                return 0  # is this okay?
            else:
                return distance
        except ValueError:
            print("Invalid input")


main()
