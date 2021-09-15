"""
CP1404 - Practical 06
Programming Language Class
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a formatted string for Programming Language instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return a Boolean if Programming Language instance is dynamic."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
