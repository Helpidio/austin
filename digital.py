from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Digital>:
    name: "digital"
    FloatLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Gestão Digital"
                        
                    Screen:
                    
                        MDLabel:
                            text: "Cada vez mais as empresas vêm observando que não é possível viver de apostas e fundamentar sua gestão em práticas intuitivas. Por isso, a AUSTIN garante um gerenciamento de projetos como solução ao permitir que cada decisão de gerenciamento seja embasada em práticas recomendadas por especialistas e estratégias eficazes."
                            pos_hint: {"center_x": .5, "center_y": .850}
                            size_hint_x: .9
                            font_size: (root.width**2 + root.height**2) / 14.5**4
                        MDLabel:
                            text: "   Maior controle dos processos"
                            pos_hint: {"center_x": .540, "center_y": .680}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "   Cumprimento do cronograma"
                            pos_hint: {"center_x": .540, "center_y": .640}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "   Monitoramneto da lucratividade"
                            pos_hint: {"center_x": .540, "center_y": .6}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "   Riscos minimizados"
                            pos_hint: {"center_x": .540, "center_y": .560}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "   Agilidade na tomada de decisões"
                            pos_hint: {"center_x": .540, "center_y": .520}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "   Maior engajamento do time"
                            pos_hint: {"center_x": .540, "center_y": .480}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "   Maior Satisfação do cliente"
                            pos_hint: {"center_x": .540, "center_y": .440}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDFloatingActionButton:
                            id: back
                            icon: "arrow-left"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hint: {"center_x": .8, "center_y": .1}
""")
APP = MDApp.get_running_app()

class Digital(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        digital = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(digital)