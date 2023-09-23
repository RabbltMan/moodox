from kivymd.uix.toolbar import MDTopAppBar

class AppBars(object):
    def __init__(self) -> None:
        self.topNaviBar = MDTopAppBar(
            id="topNaviBar",
            title="MOODOX",
            pos_hint={'top': 1},
            left_action_items=[
                ["head-dots-horizontal-outline", lambda _: self.switchScreen()]
            ]
        )

