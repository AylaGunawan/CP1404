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
    chosen_taxi = ""
    bill = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            print_taxis(taxis)
            chosen_taxi = get_valid_taxi_index(taxis)
        elif choice == "d":
            if chosen_taxi == "":
                print("You need to choose a taxi before you can drive")
            else:
                drive_distance = get_valid_distance()
                taxis[chosen_taxi].drive(drive_distance)  # DRY? taxis[chosen_taxi] and .get_fare()?
                print(f"Your {taxis[chosen_taxi].name} trip cost you ${taxis[chosen_taxi].get_fare():.2f}")
                bill += taxis[chosen_taxi].get_fare()
                taxis[chosen_taxi].start_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")  # DRY? print_bill function?
    print("Taxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    """Print a list of taxi instances and their index."""
    for i, taxi in enumerate(taxis):
        print(i, "-", taxi)


def get_valid_taxi_index(taxis):
    """Get a valid taxi index within the taxis list range"""
    is_valid_input = False
    while not is_valid_input:
        try:
            chosen_taxi = int(input("Choose taxi: "))
            if chosen_taxi > (len(taxis) - 1):
                print("Invalid taxi choice")
                chosen_taxi = ""
            return chosen_taxi
        except ValueError:
            print("Invalid input")


def get_valid_distance():
    """Get a valid non-negative integer for distance."""
    is_valid_input = False
    while not is_valid_input:
        try:
            distance = int(input("Drive how far? "))
            if distance < 0:
                print("Invalid distance")
                distance = int(input("Drive how far? "))
            return distance
        except ValueError:
            print("Invalid input")


main()
