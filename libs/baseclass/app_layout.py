from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager

class AppLayout(MDScreen):
    app_root = ObjectProperty()
    nav_drawer = ObjectProperty()
    screen_manager = ScreenManager()
    
    def __init__(self, *args, **kwargs):
        super(AppLayout, self).__init__(*args, **kwargs)

    def set_current_screen(self, screen_name):
        self.screen_manager.current = screen_name
        