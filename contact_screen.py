from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import webbrowser

Builder.load_string("""
<ContactScreen>:
    FloatLayout:
        Screen:
            MDLabel:
                text: "Contacto:"
                pos_hint: {"x": .440, "center_y": .760}
                font_style: "Button"
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 15**4
            MDTextButton:
                id: what
                text: "[color=#2E97F6]929 708 869[/color]"
                markup: True
                pos_hint: {"center_x": .5, "center_y": .720}
                size_hint: .4, .04
            MDLabel:
                text: "Email:"
                pos_hint: {"x": .465, "center_y": .680}
                font_style: "Button"
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 15**4
            MDTextButton:
                id: email
                text: "[color=#2E97F6]austinfornecedora@gmail.com[/color]"
                markup: True
                pos_hint: {"center_x": .5, "center_y": .640}
                size_hint: .6, .04
            MDLabel:
                text: "Redes Sociais:"
                pos_hint: {"x": .420, "center_y": .6}
                font_style: "Button"
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 15**4
            MDTextButton:
                id: face
                text: "[color=#2E97F6]Facebook: Austin Ao[/color]"
                markup: True
                pos_hint: {"center_x": .5, "center_y": .560}
                size_hint: .4, .04
            MDTextButton:
                id: insta 
                text: "[color=#2E97F6]Instagram: austin.company_official[/color]"
                markup: True
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .6, .04
            MDLabel:
                text: "Website:"
                pos_hint: {"x": .445, "center_y": .460}
                font_style: "Button"
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 15**4
            MDTextButton:
                id: web
                text: "[color=#2E97F6]https://austinfornecedora.github.io/Austin/[/color]"
                markup: True
                pos_hint: {"center_x": .5, "center_y": .420}
                size_hint: .7, .04
            MDLabel:
                text: "A AUSTIN agradece pela sua preferência!"
                font_style: "H6"
                pos_hint: {"center_x": .5, "center_y": .260}
                size_hint_x: .9
                font_size: 15
                theme_text_color: "Error"
            MDLabel:
                text: "Trabalhamos para si e por si!"
                pos_hint: {"center_x": .5, "center_y": .2}
                size_hint_x: .9
                theme_text_color: "Hint"
            Image:
                source: "logo.png"
                size_hint: (.2, .2)
                pos_hint: {'center_x': .5, 'center_y':.9}
                                       
            MDTextButton:
                id: dev_name
                text: "[color=#000000]Developer:[/color][color=#2E97F6] Helpidio Mateus[/color]"
                markup: True
                pos_hint: {'center_x': .5, 'center_y':.1}
                size_hint: .7, .04
                font_size: 20
                
            MDTextButton:
                id: gps
                text: "[color=#f62e47][u]Localização[/u][/color]"
                markup: True
                pos_hint: {"x": .05, "center_y": .340}
                font_style: "Caption"
                size_hint_x: .9
                font_size: 25
                
  
""")

class ContactScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.web.bind(on_release=self.link1)
        self.ids.face.bind(on_release=self.link2)
        self.ids.insta.bind(on_release=self.link3)
        self.ids.what.bind(on_release=self.link4)
        self.ids.email.bind(on_release=self.link5)
        self.ids.dev_name.bind(on_release=self.link6)
        self.ids.gps.bind(on_release=self.link7)

    def link1 (self, instance):
        webbrowser.open('https://austinfornecedora.github.io/Austin/')
    def link2 (self, instance):
        webbrowser.open('https://www.facebook.com/austinfornecedora/')
    def link3 (self,instance):
        webbrowser.open('https://www.instagram.com/austin.company_official/')
    def link4 (self, instance):
        webbrowser.open('https://wa.me/244929708869?text=')
    def link5(self, instance):
        webbrowser.open('https://mail.google.com/')
    def link6(self,instance):
        webbrowser.open('https://wa.me/244944459953?text=')
    def link7(self,instance):
        webbrowser.open('https://www.google.com/maps/dir//-8.8983625,13.1944986/@-8.8990992,13.1928786,17z/data=!4m2!4m1!3e0')