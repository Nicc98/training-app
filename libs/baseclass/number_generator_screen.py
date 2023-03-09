from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

import random

class NumberGeneratorScreen(MDScreen):
    
    def generate_number(self):
        self.random_number_label.text = str(random.randint(0, 10))