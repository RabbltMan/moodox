from kivymd.uix.toolbar import MDTopAppBar
from main import MainApp

MainTopNaviBar = MDTopAppBar(id="topNaviBar", 
                         title="MOODOX", 
                         pos_hint={'top': 1}, 
                         left_action_items=[["head-dots-horizontal-outline", lambda _: MainApp.switchScreen()]])

