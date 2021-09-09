"""
CP1404 - Practical 06
Guitar Test Client Code
"""

from guitar import Guitar


def main():
    """Guitar Test client program"""
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2013)

    print(f"{guitar_1.name} get_age() - Expected 99. Got {guitar_1.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected 8. Got {guitar_2.get_age()}")
    print(f"{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")


main()
