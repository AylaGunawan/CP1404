"""
CP1404 - Practical 08
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to create dynamic labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)  # what is this for?
        self.names = ["Ayla", "Lindsay", "Someone else"]

    def build(self):
        """Build Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list of names and add to Kivy GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
