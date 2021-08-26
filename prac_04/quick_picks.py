"""
CP1404 - Practical 04
"Quick Pick" Lottery Ticket generator
"""

import random

NUMBER_OF_RANDOM_NUMBERS = 6
MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45


def main():
    """Program for a quick pick lottery ticket generator"""
    number_of_quick_picks = get_number_of_quick_picks()
    quick_pick_numbers = []
    selected_random_numbers = []
    for quick_pick in range(number_of_quick_picks):
        generate_quick_pick_numbers(quick_pick_numbers, selected_random_numbers)
        print_quick_pick_numbers(quick_pick_numbers)
        del quick_pick_numbers[:]
        del selected_random_numbers[:]


def get_number_of_quick_picks():
    """Get valid input for number of quick picks"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            while number_of_quick_picks < 0:
                print("Invalid number of quick picks")
                number_of_quick_picks = int(input("How many quick picks? "))
            is_valid_input = True
        except ValueError:
            print("Invalid value for quick picks (non-integer)")
    return number_of_quick_picks


def generate_quick_pick_numbers(quick_pick_numbers, selected_random_numbers):
    """Generate random and unique quick pick numbers into a list"""
    for i in range(NUMBER_OF_RANDOM_NUMBERS):
        random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        while random_number in selected_random_numbers:
            random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        quick_pick_numbers.append(random_number)
        selected_random_numbers.append(random_number)


def print_quick_pick_numbers(quick_pick_numbers):
    """Print formatted quick pick numbers in ascending order"""
    quick_pick_numbers.sort()
    for quick_pick_number in quick_pick_numbers:
        print(f"{quick_pick_number:2}", end=" ")
    print()


main()
