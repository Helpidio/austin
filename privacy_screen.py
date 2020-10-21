from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<PrivacyScreen>:
    FloatLayout:
        Screen:
            MDLabel:
                font_style: "Caption"
                text: "A Politica de Privacidade da AUSTIN fornecedora company aplica-se a todos os serviços oferecidos pela AUSTIN App, suas afiliadas e aos serviços oferecidos no site."
                pos_hint: {"center_x": .5, "center_y": .920}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "Button"
                text: "QUEREMOS QUE VOCÊ ENTENDA OS TIPOS DE INFORMAÇÕES QUE PEDIMOS QUANDO USAR OS NOSSOS SERVIÇOS"
                pos_hint: {"center_x": .5, "center_y": .820}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "Caption"
                text: "Coletamos informações dos clientes para uma melhor interação entre a AUSTIN e você, o que inclui Identificação pessoal, morada e idioma que você fala."
                pos_hint: {"center_x": .5, "center_y": .720}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "Caption"
                text: "O Usuário deve saber porquê está fornecendo informações. Queremos capacita-lo para tomar ás decisões corretas. Você não precisa criar uma conta de usuário para ter acesso aos serviços e produtos da AUSTIN App, basta fazer um login de acesso rápido com o seu e-mail e uma senha. É obrigatório fazer um login de acesso rápido Porque fazemos o controle de actividades que fazes no App e precisamos informa-lo sobre ás alterações que serão feitas no App. "
                pos_hint: {"center_x": .5, "center_y": .540}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "H6"
                text: "COOKIES"
                pos_hint: {"center_x": .5, "center_y": .380}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "Caption"
                text: "Quando você está conectado também coletamos informações, armazenando dados temporariamente para melhorar a sua experiência de navegação no app e recomendar conteúdo de seu interesse. Ao utilizar nossos serviços, você concorda com tal monitoramento. A sua visita ao nosso App e acesso aos nossos serviços é registado: termos que você pesquisa, interação com os conteúdos da App e compras dos serviços."
                pos_hint: {"center_x": .5, "center_y": .240}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
"""
)

class PrivacyScreen(Screen):
    pass