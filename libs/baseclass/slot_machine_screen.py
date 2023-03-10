from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

import random

class SlotMachineScreen(MDScreen):
    
    def generate_number(self):
        self.ids.first_simbol_label.text = str(random.randint(0, 10))
        self.ids.second_simbol_label.text = str(random.randint(0, 10))
        self.ids.third_simbol_label.text = str(random.randint(0, 10))