from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

class AppLayout(MDScreen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()
    
    def __init__(self, *args, **kwargs):
        super(AppLayout, self).__init__(*args, **kwargs)

    def set_current_screen(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.text = screen_name
        self.nav_drawer.set_state("closed")
        