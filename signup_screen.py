from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from firebase import Firebase

Builder.load_string('''
<SignupScreen>:
    name: "signup_screen"
    
    Image:
        source: 'logo.png'
        size_hint: (.2, .2)
        pos_hint: {'center_x': .5, 'center_y': .9}

    MDTextField:
        id: first_name
        hint_text: "Nome"
        helper_text: "Exemplo: Helpidio"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": .5, "center_y": .8}
        size_hint_x: .8
        on_text_validate: last_name.focus = True

    MDTextField:
        id: last_name
        hint_text: "Apelido"
        helper_text: "Exemplo: Mateus"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": .5, "center_y": .7}
        size_hint_x: .8
        on_text_validate: email.focus = True

    MDTextField:
        id: email
        hint_text: "Email"
        helper_text: "Exemplo: helpidiolafame@gmail.com"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .8
        on_text_validate: password.focus = True

    MDTextField:
        id: password
        hint_text: "Senha"
        password: True
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .8
        on_text_validate: confirm_password.focus = True
    MDTextField:
        id: confirm_password
        hint_text: "Confirmar Senha"
        password: True
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .8
        on_text_validate: cel_number.focus = True

    MDTextField:
        id: cel_number
        hint_text: "Número de Celular"
        helper_text: "Exemplo: 944459953"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .8
        
    MDLabel:
        id: error_label
        pos_hint: {"center_x": .5, "center_y": .220}
        size_hint_x: .5
        theme_text_color: "Error"
        halign: "center"
        
    MDRaisedButton:
        id: signup_button
        pos_hint: {"center_x": .5, "center_y": .140}
        size_hint_y: .06
        text: "Criar"
        font_size: 20
              
    MDTextButton:
        id: login_button
        text: " [u][color=#000000]Já tenho uma conta[/color][/u]"
        pos_hint: {"center_x": .5, "center_y": .08}
        size_hint_x: .5
        markup: True
    
''')

APP = MDApp.get_running_app()
SIGNUP = Firebase()

class SignupScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.login_button.bind(on_release=self.login_screen)
        self.ids.signup_button.bind(on_release=self.signup_button_action)
    def signup_button_action(self, instance):
        first_name = self.ids.first_name.text
        last_name = self.ids.last_name.text
        email = self.ids.email.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text
        cel_number = self.ids.cel_number.text
        error_label = self.ids.error_label
        if first_name != "" and last_name != "" and email != "" and password != "" and cel_number != "":
            if password == confirm_password:
                if 12 > len(password) > 6:
                    if len(cel_number) == 9:
                        self.create_user(first_name, last_name, email, password, cel_number)
                    else:
                        error_label.text = "Contacto Invalido"
                else:
                    error_label.text = "A senha deve conter\nentre 6 à 12 Caracteres"
            else:
                error_label.text = "Senhas não coincidem\nVerificar senhas!"
        else:
            error_label.text = "Deve completar todos os campos"

    def create_user(self, first_name, last_name, email, password, cel_number,):
        SIGNUP.signup(
            name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            cel_number=cel_number,
        )

    def login_screen(self, instance):
        signup_screen = APP.root.current_screen
        from login_screen import LoginScreen
        self.login_screen = LoginScreen()
        APP.root.add_widget(self.login_screen)
        APP.root.current = "login_screen"
        APP.root.remove_widget(signup_screen)