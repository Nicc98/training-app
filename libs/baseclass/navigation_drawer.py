from kivy.properties import StringProperty, ListProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

class ContentNavigationDrawer(MDBoxLayout):
    pass

class OptionItem(OneLineIconListItem):

    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class OptionList(ThemableBehavior, MDList):

    def set_color_item(self, instance_item):
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color