from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Other>:
    name: "other"
    FloatLayout:
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                title: "Outros Serviços"
            
            FloatLayout:
                BoxLayout:
                    Screen:
                        ScrollView:
                            MDList:
                                OneLineListItem:
                                    id: stylist
                                    text: "Estilista"
                                OneLineListItem:
                                    id: recycle
                                    text: "Reciclagem de Papel"

                MDFloatingActionButton:
                    id: back
                    icon: "arrow-left"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": .8, "center_y": .1}
""")
APP = MDApp.get_running_app()


class Other(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        other = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(other)