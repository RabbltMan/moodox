from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.app import MDApp

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.mainScreen = MDBoxLayout()
        self.topNaviBar = MDTopAppBar(
            id="topNaviBar",
            title="MOODOX",
            pos_hint={'top': 1},
            left_action_items=[["head-dots-horizontal-outline"]]
        )
        self.mainScreen.add_widget(self.topNaviBar)
        return self.mainScreen

MainApp().run()