from kivymd.uix.screen import MDScreen

class AppLayout(MDScreen):
    
    def __init__(self, *args, **kwargs):
        super(AppLayout, self).__init__(*args, **kwargs)

    def set_current_screen(self, screen_name):
        self.ids.screen_manager.current = screen_name
        self.ids.toolbar.title = screen_name
        self.ids.nav_drawer.set_state("closed")
        