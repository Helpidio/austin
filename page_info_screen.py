from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from firebase import Database

Builder.load_string("""
<PageScreen>:

    Image:
        source: 'logo.png'
        size_hint: (.2, .2)
        pos_hint: {'center_x': .5, 'center_y': .8}
        
    OneLineIconListItem:
        id: first_name
        pos_hint: {"x": .250, "top": .7}
        size_hint: (.5, .1)
        IconLeftWidget:
            icon: "account"
    OneLineIconListItem:
        id: last_name
        pos_hint: {"x": .250, "top": .6}
        size_hint: (.5, .1)
        IconLeftWidget:
            icon: "account-outline"
    OneLineIconListItem:
        id: email
        pos_hint: {"x": .250, "top": .5}
        size_hint: (.5, .1)
        IconLeftWidget:
            icon: "email"
    OneLineIconListItem:
        id: contact
        pos_hint: {"x": .250, "top": .4}
        size_hint: (.5, .1)
        IconLeftWidget:
            icon: "cellphone"
    MDRaisedButton:
        id: log_out_button
        text: "Encerrar Sessão"
        pos_hint: {"center_x": .5, "center_y": .1}
""")
APP = MDApp.get_running_app()
db = Database()

class PageScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.log_out_button.bind(on_release=self.log_out)

    def on_pre_enter(self, *args):
        APP.root.current_screen.ids.tool_bar.right_action_items = []

    def log_out(self, instance):
        with open("refresh_token.txt", "w") as f:
            f.write("")
        home_screen = APP.root.current_screen
        from login_screen import LoginScreen
        self.login_screen = LoginScreen()
        APP.root.add_widget(self.login_screen)
        APP.root.current = "login_screen"
        APP.root.remove_widget(home_screen)