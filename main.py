import kivy
from kivy.app import App

from number_generator import NumberGenerator

class TrainingApp(App):
    
    def build(self):
        return NumberGenerator()
    
training_app = TrainingApp()
training_app.run()