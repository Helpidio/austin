from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp




Builder.load_string("""
<FirstScreen>:
    name: "first_screen"
    FloatLayout:
        MDCard:
            orientation: "vertical"
            size_hint: 1, None
            height: self.minimum_height
            pos_hint: {"center_x": .5, "center_y": .9}
            BoxLayout:
                id: box
                size_hint: 1, None
                height: dp(150)
                FitImage:
                    source: "ban.png"
                   
        Image:           
            source: "marketing.png"
            pos_hint: {"center_x": .2, "center_y": .6}
            size_hint: .250, .4
        MDTextButton:
            id: marketing
            text: "Marketing Digital"
            pos_hint: {"center_x": .2, "center_y": .5}
            size_hint: .3, .05
            custom_color: 0, 0, 0, 1
        Image:
            source: "deve.png"
            pos_hint: {"center_x": .5, "center_y": .6}
            size_hint: .2, .2       
        MDTextButton:
            id: developer
            text: "Developer"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: .2, .05
            custom_color: 0, 0, 0, 1
        Image:
            source: "design.png"
            pos_hint: {"center_x": .8, "center_y": .6}
            size_hint: .2, .2
        MDTextButton:
            id: design
            text: "Design Gráfico"
            pos_hint: {"center_x": .8, "center_y": .5}
            size_hint: .3, .05
            custom_color: 0, 0, 0, 1
        Image:
            source: "info.png"
            pos_hint: {"center_x": .2, "center_y": .4}
            size_hint: .2, .2
        MDTextButton:
            id: info
            text: "Informática"
            pos_hint: {"center_x": .2, "center_y": .3}
            size_hint: .2, .05
            custom_color: 0, 0, 0, 1
        Image:
            source: "free.png"
            pos_hint: {"center_x": .5, "center_y": .4}
            size_hint: .2, .2
        MDTextButton:
            id: freelancer
            text: "Freelancer"
            pos_hint: {"center_x": .5, "center_y": .3}
            size_hint: .2, .05
            custom_color: 0, 0, 0, 1
        Image:
            source: "perfi.png"
            pos_hint: {"center_x": .8, "center_y": .4}
            size_hint: .2, .2
        MDTextButton:
            id: digital
            text: "Gestão Digital"
            pos_hint: {"center_x": .8, "center_y": .3}
            size_hint: .3, .05
            custom_color: 0, 0, 0, 1
        Image:
            source: "arqui.png"
            pos_hint: {"center_x": .2, "center_y": .2}
            size_hint: .2, .2
        MDTextButton:
            id: arq
            text: "Arquitetura"
            pos_hint: {"center_x": .2, "center_y": .1}
            size_hint: .2, .05
            custom_color: 0, 0, 0, 1
        Image:
            source: "outro.png"
            pos_hint: {"center_x": .5, "center_y": .2}
            size_hint: .2, .2
        MDTextButton:
            id: other
            text: "Outros"
            pos_hint: {"center_x": .5, "center_y": .1}
            size_hint: .2, .05
            custom_color: 0, 0, 0, 1   
                              
""")
APP = MDApp.get_running_app()

class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.marketing.bind(on_release=self.marketing)
        self.ids.developer.bind(on_release=self.developer)
        self.ids.design.bind(on_release=self.design)
        self.ids.info.bind(on_release=self.info)
        self.ids.freelancer.bind(on_release=self.freelancer)
        self.ids.digital.bind(on_release=self.digital)
        self.ids.arq.bind(on_release=self.arq)
        self.ids.other.bind(on_release=self.other)

    def marketing(self, instance):
        first_screen = APP.root.current_screen
        from marketing import Marketing
        self.marketing = Marketing()
        APP.root.add_widget(self.marketing)
        APP.root.current = "marketing"
        APP.root.remove_widget(first_screen)

    def developer(self, instance):
        home_screen = APP.root.current_screen
        from developer import Developer
        self.developer = Developer()
        APP.root.add_widget(self.developer)
        APP.root.current = "developer"
        APP.root.remove_widget(home_screen)

    def design(self, instance):
        home_screen = APP.root.current_screen
        from design import Design
        self.design = Design()
        APP.root.add_widget(self.design)
        APP.root.current = "design"
        APP.root.remove_widget(home_screen)

    def info(self, instance):
        home_screen = APP.root.current_screen
        from info import Info
        self.info = Info()
        APP.root.add_widget(self.info)
        APP.root.current = "info"
        APP.root.remove_widget(home_screen)

    def freelancer(self, instance):
        home_screen = APP.root.current_screen
        from freelancer import Freelancer
        self.freelancer = Freelancer()
        APP.root.add_widget(self.freelancer)
        APP.root.current = "freelancer"
        APP.root.remove_widget(home_screen)

    def digital(self, instance):
        home_screen = APP.root.current_screen
        from digital import Digital
        self.digital = Digital()
        APP.root.add_widget(self.digital)
        APP.root.current = "digital"
        APP.root.remove_widget(home_screen)

    def arq(self, instance):
        home_screen = APP.root.current_screen
        from arq import Arq
        self.arq = Arq()
        APP.root.add_widget(self.arq)
        APP.root.current = "arq"
        APP.root.remove_widget(home_screen)

    def other(self, instance):
        home_screen = APP.root.current_screen
        from other import Other
        self.other = Other()
        APP.root.add_widget(self.other)
        APP.root.current = "other"
        APP.root.remove_widget(home_screen)


