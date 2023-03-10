from kivymd.uix.screen import MDScreen

import random

class SlotMachineScreen(MDScreen):
    
    def spin(self):
        self.ids.spin_btn.disabled = True
        self.ids.first_simbol_label.text = str(random.randint(0, 10))
        self.ids.second_simbol_label.text = str(random.randint(0, 10))
        self.ids.third_simbol_label.text = str(random.randint(0, 10))
        self.ids.spin_btn.disabled = False