from kivy.uix.screenmanager import Screen
import random

class NumberGeneratorScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def generate_number(self):
        self.random_number_label.text = str(random.randint(0, 10))