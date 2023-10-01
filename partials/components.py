from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.image import Image

class Components(object):
    def __init__(self) -> None:
        self.MainFloatingHeadButton = MDFloatingActionButton(
            id='top_head',
            icon="head-dots-horizontal-outline",
            pos_hint={"right": 0.95, "y": 0.05},
            md_bg_color=(0.5, 0.5, 0.5, 0),
            icon_color=(0.617, 0.616, 0.617, 1),
            icon_size="32sp",
            shadow_offset=(0, 0),
            shadow_color=(224/255, 205/255, 182/255, 0.3),
            elevation=0,
        )
        self.logo = Image(
            source='./src/logo.png',
            opacity=0.65,
            size_hint_y=0.09,
            pos_hint={"top": 0.98}
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

