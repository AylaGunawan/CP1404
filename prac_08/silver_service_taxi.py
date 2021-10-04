"""
CP1404 - Practical 08
Silver Service Taxi Class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent an SilverServiceTaxi object, a specialised version of Taxi that includes fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise an SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness  # check solutions on this one chief

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the trip like a Taxi but with flagfall."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
