from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<TermScreen>:
    FloatLayout:
        Screen:
            MDLabel:
                font_style: "Caption"
                text: "Introdução: primeiro agradecemos por utilizar a AUSTIN app. A AUSTIN App é um serviço disponibilizado pela AUSTIN Fornecedora Company localizada na Avenida 21 de Janeiro, Morro Bento, Luanda, Angola. O uso que você faz da AUSTIN App está sujeito a termos de serviços da AUSTIN App. Qualquer conflito que houver com os termos de serviços da AUSTIN contacte-nos. Mas saiba que eles são irrefutáveis e inalteráveis ."
                pos_hint: {"center_x": .5, "center_y": .840}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "Caption"
                text: "Seu uso da AUSTIN App: A AUSTIN é uma empresa facilitadora na procura de serviços e produtos. Acesso aos conteúdos. Você pode usar a AUSTIN App para: procurar, localizar, visualizar, acessar serviços e produtos. Para usar a AUSTIN App é necessário ter um  dispositivo que atendam com os requisitos de sistema e de compatibilidade à App."
                pos_hint: {"center_x": .5, "center_y": .640}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "Caption"
                text: "Acesso aos serviços e pagamentos: Ao usar a AUSTIN App você firmará um acesso de compras aos nossos serviços e produtos. O contrato de compra e uso do conteúdo é firmado quando você recebe um e-mail ou sms da AUSTIN a confirmar a compra de serviços e produtos. O cumprimento do contrato começa quando a compra é concluída. "
                pos_hint: {"center_x": .5, "center_y": .460}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
            MDLabel:
                font_style: "Caption"
                text: "AUSTIN pagamentos: formas de processamento de pagamentos. Facturamento via Multi-caixa express (Transferência). Para que isso seja possível o cliente precisará preencher um formulário de compra de serviços ou produtos (online ou fisicamente para a sua segurança), porém você precisará aceitar os Termos de Serviço da AUSTIN."
                pos_hint: {"center_x": .5, "center_y": .280}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.9**4
"""
)


class TermScreen(Screen):
    pass