"""
CP1404 - Practical 03
Password Check
"""

MINIMUM_PASSWORD_LENGTH = 10

password = input("Password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Invalid password")
    password = input("Password: ")
print("*" * len(password))
