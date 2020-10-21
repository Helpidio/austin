from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Developer>:
    name: "developer"
    FloatLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Developer"
                        
                    Screen:
                        
                        MDLabel:
                            text: "Realizamos o desenvolvimento técnico e visual de páginas da internet e manutenção de sites, definindo linguagens, bancos de dados, armazenamento e atualização de informações, a fim de atender o volume de internautas e seu correto funcionamento. Fornecemos profissionais essenciais para a elaboração e desenvolvimento do seu aplicativo e software: Deskop Developer, Web Developer & Mobile Developer."
                            pos_hint: {"center_x": .5, "center_y": .820}
                            size_hint_x: .9
                            font_size: (root.width**2 + root.height**2) / 14.5**4

                        Image:
                            source: 'd.png'
                            pos_hint: {"center_x": .5, "center_y": .2}
                        MDFloatingActionButton:
                            id: back
                            icon: "arrow-left"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hint: {"center_x": .8, "center_y": .1}
"""
)

APP = MDApp.get_running_app()

class Developer(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        developer = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(developer)