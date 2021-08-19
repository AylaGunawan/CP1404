"""
CP1404 - Practical 01
Menu-Driven Number Sequence Generator (Extension)
"""

MENU = """
(E) Show even numbers from first to last number
(O) Show odd numbers from first to last number
(S) Show squares from first to last number
(Q) Quit"""

first_number = int(input("First number: "))
last_number = int(input("Last number: "))

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        for i in range(first_number, last_number + 1):
            if i % 2 == 0:
                print(i, end=" ")
    elif choice == "O":
        for i in range(first_number, last_number + 1):
            if i % 2 == 1:
                print(i, end=" ")
    elif choice == "S":
        for i in range(first_number, last_number + 1):
            for j in range(first_number, last_number + 1):
                if i == j * j:
                    print(i, end=" ")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Sequences are fun! :)")
