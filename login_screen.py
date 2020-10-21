from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from firebase import Firebase

Builder.load_string("""
<LoginScreen>:
    name: "login_screen"
    
    Image:
        source: 'logo.png'
        size_hint: (.2, .2)
        pos_hint: {'center_x': .5, 'center_y': .8}
        
    MDTextField:
        id: email
        hint_text: "Insira o seu email"
        icon_left: 'email'
        size_hint_x: .7
        pos_hint: {"center_x": .5, "center_y": .6}
        on_text_validate: password.focus = True
    MDTextField:
        id: password
        hint_text: "Insira a sua senha"
        icon_left: 'key-variant'
        password: True
        size_hint_x: .7
        pos_hint: {"center_x": .5, "center_y": .5}
    MDRaisedButton:
        id: login_button
        text: "Entrar"
        size_hint_y: .06
        pos_hint: {"center_x": .5, "center_y": .4}
        font_size: 20
    MDLabel:
        id: error
        pos_hint: {"center_x": .5, "center_y": .2}
        size_hint_x: .5
        theme_text_color: "Error"
        halign: "center"
        
    MDTextButton:
        id: signup_screen
        text: " [color=#000000]Já tens uma conta?[/color] [u]Criar[/u]"
        pos_hint: {"center_x": .5, "center_y": .1}
        size_hint_x: .5
        markup: True
      
    
    
""")
APP = MDApp.get_running_app()
LOGIN = Firebase()

class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.signup_screen.bind(on_release=self.back)
        self.ids.login_button.bind(on_release=self.login)
    def login(self, instance):
        email = self.ids.email.text
        password = self.ids.password.text
        if email != "":
            if password != "":
                self.login_return = LOGIN.login(email=email, password=password)

                if not self.login_return == "True":
                    self.ids.error.text = str(self.login_return)
            else:
                self.ids.error.text = "Insira a sua senha!"
        else:
            self.ids.error.text = "Insira o seu email!"

    def back(self, instance):
        login_screen = APP.root.current_screen
        from signup_screen import SignupScreen
        self.signup_screen = SignupScreen()
        APP.root.add_widget(self.signup_screen)
        APP.root.current = "signup_screen"
        APP.root.remove_widget(login_screen)