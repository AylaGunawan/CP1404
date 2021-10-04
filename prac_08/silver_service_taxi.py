"""
CP1404 - Practical 08
Silver Service Taxi Class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent an SilverServiceTaxi object, a specialised version of Taxi that includes fanciness."""

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise an SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
