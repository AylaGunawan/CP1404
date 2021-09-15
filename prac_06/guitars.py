"""
CP1404 - Practical 06
Guitars Client Program
"""

from guitar import Guitar


def main():
    """Guitar client program."""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = get_valid_number("Year: ")
        cost = get_valid_number("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("\nThese are my guitars:")
    print_guitars(guitars)


def get_valid_number(prompt):
    """Get valid number equal or greater than 0."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = float(input(prompt))
            while number < 0:
                print("Invalid number")
                number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number (must be a number)")


def print_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
