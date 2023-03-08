from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

class MyScreenManager(ScreenManager):
    pass

class TrainingApp(MDApp):

    def build(self):
        self.screen_manager = MyScreenManager()
        return Builder.load_file("main.kv")
    
if __name__ == "__main__":
    training_app = TrainingApp()
    training_app.run()