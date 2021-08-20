"""
CP1404 - Practical 03
Broken Scores
"""

import random


def main():
    """Program that displays score category for user input and random score"""
    user_score = int(input("Enter score: "))
    category = determine_category(user_score)
    print_category(user_score, category)

    random_score = random.randint(0, 100)
    category = determine_category(random_score)
    print_category(random_score, category)


def determine_category(score):
    """Determine category of score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_category(score, category):
    """Print score and its category"""
    print(f"The score {score} is {category}")


main()
