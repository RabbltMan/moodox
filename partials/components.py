from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image

class Components(object):
    def __init__(self) -> None:
        self.logo = Image(
            source='./src/logo.png',
            size_hint=(0.4, 0.06),
            opacity=0.65,
            pos_hint={"center_x": .5, "center_y": .93},
        )
        self.MainTopNaviBar = MDTopAppBar(
            id="top_navi",  
            pos_hint={'top': 1}, 
            elevation=0,
            md_bg_color=(99/255, 235/255, 233/255, 0),
            specific_text_color=(50/255, 50/255, 50/255, 1),
            left_action_items=[["head-dots-horizontal-outline"]]
        )

        self.MainContent = MDBoxLayout(
            md_bg_color=(216/255, 185/255, 156/255, 1),
        )
        self.MainBackground = FitImage(
            source="./src/bg.jpg",
            pos_hint={"top": 1},
            opacity=0.5
        )
        self.MainContent.add_widget(self.MainBackground)

