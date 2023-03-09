from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

class HomeScreen(MDScreen):
    welcome_label = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
