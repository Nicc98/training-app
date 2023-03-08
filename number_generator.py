from kivy.uix.boxlayout import BoxLayout

import random

class NumberGenerator(BoxLayout):

    def __init__(self):
        super(NumberGenerator, self).__init__()
    
    def generate_number(self):
        self.random_number_label.text = str(random.randint(0, 10))