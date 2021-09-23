"""
CP1404 - Practical 07
Miles to Kilometres Converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = "Ayla Gunawan"
MILES_TO_KILOMETRES_MULTIPLIER = 1.60934


class ConvertMilesToKilometresApp(App):
    """Kivy App that converts miles to kilometres."""
    output_kilometres = StringProperty()

    def build(self):
        """Build app from .kv file."""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_increment(self, miles, increment):
        """Handle up/down increment for input text."""
        incremented_miles = self.convert_to_number(miles) + increment
        self.root.ids.input_miles.text = str(incremented_miles)

    def handle_convert(self, miles):
        """Handle conversion of miles to kilometers."""
        kilometers = self.convert_to_number(miles) * MILES_TO_KILOMETRES_MULTIPLIER
        self.update_result(kilometers)

    def update_result(self, kilometres):
        """Update result in text output."""
        self.output_kilometres = str(kilometres)

    @staticmethod
    def convert_to_number(string):
        """Convert string to float or 0.0 invalid."""
        try:
            return float(string)
        except ValueError:
            return 0.0


ConvertMilesToKilometresApp().run()
