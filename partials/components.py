from os import listdir
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.image import Image
from random import choice

class Components(object):
    def __init__(self) -> None:
        self.MainFloatingHeadButton = MDFloatingActionButton(
            id='top_head',
            icon="head-dots-horizontal-outline",
            pos_hint={"right": 0.95, "y": 0.02},
            md_bg_color=(0.5, 0.5, 0.5, 0),
            icon_color=(0.3, 0.4, 0.7, 1),
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

        self.MainBackgroundFilter = MDBoxLayout(
            md_bg_color=(216/255, 185/255, 156/255, 1),
        )
        self.BackgroundImage = FitImage(
            source="./src/bg.jpg",
            pos_hint={"top": 1},
            opacity=0.5
        )
        self.MainBackgroundFilter.add_widget(self.BackgroundImage)

        self.DailyCard = MDCard(
            id='daily_card',
            radius=24,
            md_bg_color=(0.3, 0.3, 0.3, 0.5),
            pos_hint={"center_x": .5, "center_y": .5},
            size_hint=(0.9, 0.77),
        )
        self.imageDir = listdir('./src/card_images/')
        self.cardImage = FitImage(
            source='./src/card_images/' + choice(self.imageDir),
            pos_hint={"top": 1},
            size_hint_y=0.3,
            opacity=0.77,
            radius=(24, 24, 0, 0),
        )
        self.DailyCard.add_widget(self.cardImage)