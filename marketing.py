from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Marketing>:
    name: "marketing"
    FloatLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Marketing Digital"
                               
                    Screen: 
                                                      
                        MDLabel:
                            text: "Projetar o produto e a imagem da organização com o fim de ocupar uma posição diferenciada na escolha de seu público-alvo. A AUSTIN Marketing trabalha para si e por si, em conjunto de atividades que visa entender e atender às necessidades do cliente. Elevando a sua empresa ou marca aos destaques do mundo digital."
                            pos_hint: {"center_x": .5, "center_y": .850}
                            size_hint_x: .9
                            font_size: (root.width**2 + root.height**2) / 14.5**4                     
                                                    
                        MDFloatingActionButton:
                            id: back
                            icon: "arrow-left"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hint: {"center_x": .8, "center_y": .1}
            
"""
)

APP = MDApp.get_running_app()

class Marketing(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        marketing = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(marketing)
