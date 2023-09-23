from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class Main(MDApp):
    def build(self):
        self.mainScreen = MDScreen()
        # Top Navigation Toolbar

        # render main screen
        return self.mainScreen

Main().run()