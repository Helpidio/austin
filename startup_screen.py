from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

kv = """
<StartupScreen>
    name: "startup_screen"
"""


class StartupScreen(MDScreen):
    Builder.load_string(kv)

    def __init__(self, **kw):
        super().__init__(**kw)
        from firebase import Firebase

        self.app = MDApp.get_running_app()
        self.my_firebase = Firebase()

    def on_enter(self):
        from home_screen import HomeScreen
        from login_screen import LoginScreen

        home_screen = HomeScreen()
        login_screen = LoginScreen()
        self.app.root.add_widget(home_screen)
        self.app.root.add_widget(login_screen)

        try:
            with open("refresh_token.txt", "r") as f:
                refresh_token = f.read()
                self.my_firebase.exchange_refresh_token(refresh_token)
                Clock.schedule_once(lambda dt: self.load_home(), 1)
        except:
            Clock.schedule_once(lambda dt: self.load_login(), 1)

    def load_home(self):
        self.app.root.current = "home"

    def load_login(self):
        self.app.root.current = "login_screen"