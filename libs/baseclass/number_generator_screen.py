from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
import random

class NumberGeneratorScreen(MDScreen):
    number_generator_screen = ObjectProperty()
    
    def generate_number(self):
        self.random_number_label.text = str(random.randint(0, 10))