from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Info>:
    name: "info"
    FloatLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Informática"
                        
                    Screen:
                    
                        MDLabel:
                            text: "Manutenção de Computadores independentemente da situação do seu computador. Trabalhamos na área ou fazemos a retirada do computador na sua residência, empresa ou escritório. Analisamos e consertamos seu computador com rapidez e eficiência."
                            size_hint_x: .9
                            pos_hint: {"center_x": .5, "center_y": .850}
                            font_size: (root.width**2 + root.height**2) / 14.5**4
                        MDLabel:
                            text: "-  Instalação de todo tipo de sistema operativo"
                            pos_hint: {"center_x": .540, "center_y": .7}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Windows XP"
                            pos_hint: {"center_x": .540, "center_y": .660}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Windows 7/8/10"
                            pos_hint: {"center_x": .540, "center_y": .620}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Servidor 2008/12/16/19"
                            pos_hint: {"center_x": .540, "center_y": .580}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "-  Instalação de todo tipo de Programa"
                            pos_hint: {"center_x": .540, "center_y": .540}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Instalação completa dos drivers"
                            pos_hint: {"center_x": .540, "center_y": .5}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Recuperação de senha do computador"
                            pos_hint: {"center_x": .540, "center_y": .460}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Proteção/Remoção de vírus(Antivírus)"
                            pos_hint: {"center_x": .540, "center_y": .420}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "-  Hardware"
                            pos_hint: {"center_x": .540, "center_y": .380}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Diagnóstico geral"
                            pos_hint: {"center_x": .540, "center_y": .340}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Montagem e reparação de redes"
                            pos_hint: {"center_x": .540, "center_y": .3}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Montagem de Cyber Café"
                            pos_hint: {"center_x": .540, "center_y": .260}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4              
                        MDLabel:
                            text: "-  Outros Serviços"
                            pos_hint: {"center_x": .540, "center_y": .220}
                            font_style: "Button"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Coloca-se jogos em Playstation(3 & 4)"
                            pos_hint: {"center_x": .540, "center_y": .180}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - Reparação de aparelhos"
                            pos_hint: {"center_x": .540, "center_y": .140}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "      - etc..."
                            pos_hint: {"center_x": .540, "center_y": .1}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                            
                        MDFloatingActionButton:
                            id: back
                            icon: "arrow-left"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hint: {"center_x": .8, "center_y": .1}
""")
APP = MDApp.get_running_app()


class Info(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        info = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(info)