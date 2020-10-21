from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from startup_screen import StartupScreen

class MainApp(MDApp):

    def build(self):

        sm = ScreenManager()
        return sm

    def on_start(self):
        ss = StartupScreen()
        self.root.add_widget(ss)
        self.root.current = "startup_screen"

MainApp().run()