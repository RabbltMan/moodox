from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from bin.components import *

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switchScreen(self, target):
        print(f"Switching to {target}")
        self.screenManager.transition.direction = 'right'
        self.screenManager.current = target

    def build(self):
        # render screen manager
        self.screenManager = ScreenManager()
        # render main screen
        self.mainScreen = Screen(name="main")
        self.topNaviBar = AppBars().topNaviBar
        self.topNaviBar.left_action_items = [
            ["head-dots-horizontal-outline", lambda _: self.switchScreen("bs")]
        ]
        self.mainScreen.add_widget(self.topNaviBar)
        self.screenManager.add_widget(self.mainScreen)
        # render brainstorm screen
        self.bsScreen = Screen(name="bs")
        self.topNaviBar = AppBars().topNaviBar
        self.topNaviBar.left_action_items = [
            ["head-dots-horizontal-outline", lambda _: self.switchScreen("main")]
        ]
        self.bsScreen.add_widget(self.topNaviBar)
        self.screenManager.add_widget(self.bsScreen)
        # screen manager state
        self.screenManager.current = "main"
        return self.screenManager

MainApp().run()