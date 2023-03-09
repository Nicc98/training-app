from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem

class OptionsNavigationDrawer(MDBoxLayout):
    options_navigation_drawer = ObjectProperty()        

class OptionsItem(OneLineIconListItem, ThemableBehavior):
    icon = StringProperty()
    text = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))
