"""
CP1404 - Practical 06
Guitar Class
"""

CURRENT_YEAR = 2021


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string for Guitar instance."""
        return f"{self.name} ({self.year:.0f}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return difference between Guitar instance's and current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return Boolean if vintage (Guitar instance's age is 50 or more)."""
        if self.get_age() >= 50:
            return True
        else:
            return False
