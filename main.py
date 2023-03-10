from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemeManager

from libs.baseclass.app_layout import AppLayout
from libs.helpers.config_setup import ConfigSetup

class TrainingApp(MDApp):
    theme_manager = ThemeManager()

    def build(self):
        Builder.load_file("main.kv")
        self.theme_manager.theme_style = "Light"
        self.theme_manager.primary_palette = "Blue"
        self.theme_cls.accent_palette = "LightBlue"
        return AppLayout()
    
if __name__ == "__main__":

    config = ConfigSetup()
    config.change_screen_size()

    TrainingApp().run()