from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from partials.components import *

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        components = Components()
        # render screen manager
        self.screenManager = ScreenManager()
        # render main screen
        self.mainScreen = Screen(name="main")
        self.mainScreen.add_widget(components.MainTopNaviBar, index=1)
        self.mainScreen.add_widget(components.MainContent, index=2)
        self.mainScreen.add_widget(components.logo)
        self.screenManager.add_widget(self.mainScreen)
        # screen manager state
        self.screenManager.current = "main"
        return self.screenManager

MainApp().run()