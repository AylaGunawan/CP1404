"""
CP1404 - Practical 07
Miles to Kilometres Converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Ayla Gunawan"


class ConvertMilesToKilometresApp(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        print("Convert")

    def handle_up(self):
        print("Up")

    def handle_down(self):
        print("Down")


ConvertMilesToKilometresApp().run()
