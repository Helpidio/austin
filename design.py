from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_string("""
<Design>:
    name: "design"
    FloatLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Design Gráfico"
                        
                    Screen:
                    
                        MDLabel:
                            text: "Com um mundo tão globalizado estando praticamente na era digital dominante em negócios. Oferecemos um apoio para criar soluções através de projetos de comunicação visual que atendam as necessidades do mercado em projetos gráficos que envolvam tanto o impresso quanto o digital. Desenvolvemos marca gráfica, identidade visual, sinalização e outros."
                            pos_hint: {"center_x": .5, "center_y": .8}
                            size_hint_x: .9
                            font_size: (root.width**2 + root.height**2) / 14.5**4
                        MDLabel:
                            text: "        Projetos Editoriais"
                            pos_hint: {"center_x": .540, "center_y": .6}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Livros"
                            pos_hint: {"center_x": .540, "center_y": .560}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Logotipos"
                            pos_hint: {"center_x": .540, "center_y": .520}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Criação visual de sites"
                            pos_hint: {"center_x": .540, "center_y": .480}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Cartazes"
                            pos_hint: {"center_x": .540, "center_y": .440}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Adesivos"
                            pos_hint: {"center_x": .540, "center_y": .4}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Panfletos"
                            pos_hint: {"center_x": .540, "center_y": .360}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Planejamento e desenvolvimento de anúncios"
                            pos_hint: {"center_x": .540, "center_y": .320}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDLabel:
                            text: "        Peças audiovisuais, etc."
                            pos_hint: {"center_x": .540, "center_y": .280}
                            font_style: "Caption"
                            font_size: (root.width**2 + root.height**2) / 14.9**4
                        MDFloatingActionButton:
                            id: back
                            icon: "arrow-left"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hint: {"center_x": .8, "center_y": .1}
""")
APP = MDApp.get_running_app()


class Design(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.back.bind(on_release=self.back)

    def back(self, instance):
        design = APP.root.current_screen
        from home_screen import HomeScreen
        self.home_screen = HomeScreen()
        APP.root.add_widget(self.home_screen)
        APP.root.current = "home"
        APP.root.remove_widget(design)