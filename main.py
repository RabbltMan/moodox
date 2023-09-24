from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from bin.components import *

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switchScreen(self):
        pass

    def build(self):
        # render screen manager
        self.screenManager = ScreenManager()
        # render main screen
        self.mainScreen = Screen(name="main")
        self.mainScreen.add_widget(MainTopNaviBar)
        self.screenManager.add_widget(self.mainScreen)
        # render brainstorm screen
        self.bsScreen = Screen(name="bs")
        self.bsScreen.add_widget(MainTopNaviBar)
        self.screenManager.add_widget(self.bsScreen)
        # screen manager state
        self.screenManager.current = "main"
        return self.screenManager

MainApp().run()