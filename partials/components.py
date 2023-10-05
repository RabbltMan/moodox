from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.image import Image
from random import choice, randint
from os import listdir
from time import sleep
from datetime import date

class Components(object):
    def __init__(self) -> None:
        self.MainFloatingHeadButton = MDFloatingActionButton(
            id='top_head',
            icon="head-dots-horizontal-outline",
            pos_hint={"right": 0.990, "y": 0.008},
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

        self.DailyCard = MDRelativeLayout(
            id='daily_card',
            radius=(24, 24, 24, 24),
            md_bg_color=(0.3, 0.3, 0.3, 0.2),
            pos_hint={"center_x": .5, "center_y": .5},
            size_hint=(0.9, 0.77),
        )
        self.imageDir = listdir('./src/card_images/')
        self.cardImage = FitImage(
            source='./src/card_images/' + choice(self.imageDir),
            pos_hint={"top": 1},
            size_hint_y=0.33,
            opacity=0.77,
            radius=(24, 24, 0, 0),
        )
        self.dateSection = MDGridLayout(
            pos_hint={"x": 0, "y": 0.8},
            rows=3,
            cols=1,
            md_bg_color=(1, 1, 1, 0.8),
            size_hint=(0.25, 0.2),
            radius=(24, 0, 20, 0)
        )
        self.monthLabel = Label(
            text=str(date.today().month),
            pos_hint={"x": 0.75},
            padding_x=0.3,
            color=(1, 0.3, 0, 1),
            font_size="27sp",
            font_name="./src/DottedSong.ttf"
        )
        self.dayLabel = Label(
            text=str(date.today().day),
            padding_x=0.3,
            color=(0, 0.3, 1, 1),
            font_size="27sp",
            font_name="./src/DottedSong.ttf"
        )
        self.weekDayLabel = Label(
            text=["MON","TUE","WED","THU","FRI","SAT","SUN"][date.today().weekday()],
            padding_x=0.3,
            color=(0, 0, 0, 1),
            font_size="16sp",
            font_name="./src/DottedSong.ttf"
        )
        self.faceSrc = randint(0, 9)
        self.face = Image(
            source="./src/emojis/" + listdir('./src/emojis/')[self.faceSrc % len(listdir('./src/emojis/'))],
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.2, 0.2),
            opacity=0.95,
        )
        self.changeFaceBtn = MDFloatingActionButton(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.2, 0.2),
            opacity=0,
            md_bg_color=(0.5, 0.5, 0.5, 0),
            icon_color=(0.3, 0.4, 0.7, 0),
            shadow_offset=(0, 0),
            shadow_color=(224/255, 205/255, 182/255, 0),
            elevation=0,
        )
        self.changeFaceBtn.bind(on_press=self.handleChange)
        self.DailyCard.add_widget(self.cardImage)
        self.dateSection.add_widget(self.monthLabel)
        self.dateSection.add_widget(self.weekDayLabel)
        self.dateSection.add_widget(self.dayLabel)
        self.DailyCard.add_widget(self.dateSection)
        self.DailyCard.add_widget(self.face)
        self.DailyCard.add_widget(self.changeFaceBtn)

    def handleChange(self, *args):
        self.faceSrc += 1
        self.face.source = "./src/emojis/" + listdir('./src/emojis/')[self.faceSrc % len(listdir('./src/emojis/'))]
