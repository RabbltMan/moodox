from random import randint
from functools import partial
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from partials.components import *

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def renderColorfulButtonIcon(self, *args):
        r, g, b, _ = args[0].icon_color
        r += randint(-4, 4)/255
        g += randint(-4, 4)/255
        b += randint(-4, 4)/255
        if not 0 <= r <= 1:
            r = 1 if r > 1 else 0
        if not 0 <= g <= 1:
            g = 1 if g > 1 else 0
        if not 0 <= b <= 1:
            b = 1 if b > 1 else 0
        args[0].icon_color = (r, g, b, 1)

    def debug(self, *args):
        pass

    def build(self):
        components = Components()
        # render screen manager
        self.screenManager = ScreenManager()
        # render main screen
        self.mainScreen = Screen(name="main")
        self.mainScreen.add_widget(components.logo, index=1)
        self.mainScreen.add_widget(components.MainFloatingHeadButton, index=2)
        self.mainScreen.add_widget(components.MainBackgroundFilter, index=2)
        self.mainScreen.add_widget(components.DailyCard)
        self.screenManager.add_widget(self.mainScreen)
        
        # execute callbacks
        Clock.schedule_interval(partial(self.renderColorfulButtonIcon, components.MainFloatingHeadButton), 0.5)
        Clock.schedule_interval(partial(self.debug, components), 1)
        # screen manager state
        self.screenManager.current = "main"
        return self.screenManager

MainApp().run()