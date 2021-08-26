"""
CP1404 - Practical 04
List Exercises
"""

# 1. Basic list operations


def main():
    """Program that stores 5 number inputs in a list for operation outputs"""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


# 2. Woefully inadequate security checker


# def main():
#     """Program that checks if input username is in a list of usernames"""
#     usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
#                  'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
#                  'bob']
#     username = input("Username: ")
#     if username in usernames:
#         print("Access granted")
#     else:
#         print("Access denied")


main()
