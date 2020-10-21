from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Freelancer>:
    name: "freelancer"
    FloatLayout:
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                title: "Freelancer"
            
            FloatLayout:
                BoxLayout:
                    Screen:
                        ScrollView:
                            MDList:
                                OneLineIconListItem:
                                    id: day
                                    text: "Diárista"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    id: handyman
                                    text: "Handyman"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Cozinheira/o"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Pedreiro/s"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Electricista"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Canalizador"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Barbeiro"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Fotógrafo"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Cabeleireira"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Motorista"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                OneLineIconListItem:
                                    text: "Ladrilhador"
                                    IconLeftWidget:
                                        icon: "account-outline"
                                
                MDFloatingActionButton:
                    id: back
                    icon: "arrow-left"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": .8, "center_y": .1}
""")
APP = MDApp.get_running_app()


class Freelancer(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        freelancer = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(freelancer)


