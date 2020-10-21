from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Arq>:
    name: "arq"
    FloatLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Arquitetura"
                        
                    Screen:
                    
                        MDLabel:
                            text: "A AUSTIN está em associação com profissionais extremamente experientes nas áreas de Engenharia geográfica e Arquitetura. "
                            pos_hint: {"center_x": .5, "center_y": .9}
                            size_hint_x: .9
                            font_size: (root.width**2 + root.height**2) / 14.5**4
                        MDLabel:
                            text: "-  Acompanhamento de obras de construção"
                            pos_hint: {"center_x": .540, "center_y": .8}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "-  projetos de construção civil(planta)"
                            pos_hint: {"center_x": .540, "center_y": .760}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "-  croquis de localização"
                            pos_hint: {"center_x": .540, "center_y": .720}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "-  levantamentos topográficos"
                            pos_hint: {"center_x": .540, "center_y": .680}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                            
                        MDFloatingActionButton:
                            id: back
                            icon: "arrow-left"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hint: {"center_x": .8, "center_y": .1}
""")
APP = MDApp.get_running_app()


class Arq(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        arq = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(arq)