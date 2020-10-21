from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<PayScreen>:
    FloatLayout:
        Screen:
            MDLabel:
                text: "Facturamento via Multi-caixa express(Transferência). Para que isso seja possível o cliente precisará preencher um formulário de compra de serviços ou produtos (online ou fisicamente para a sua segurança) porém você precisará aceitar os Termos de Serviço da Austin Fornecedora Company. À AUSTIN enviará suas informações de endereço e identidade legalmente reconhecida para facilitar a sua segurança. "
                pos_hint: {"center_x": .5, "center_y": .840}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.5**4
            MDLabel:
                text: "Serviço pós-pago 70%: Esse serviço garante a segurança do vendedor e do comprador, uma forma de pagamento com adiantamento de 30% antes do serviço ser disponibilizado ao cliente (o adiantamento é feito na presença do servente) após ser feito o adiantamento o servente fará o serviço e após o término, o servido deverá obrigatoriamente fazer o pagamento dos 70%(na presença do servente)."
                pos_hint: {"center_x": .5, "center_y": .560}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.5**4  
            MDLabel:
                text: "Pagamento físico/comum: Feito no balcão da AUSTIN localizado na rua Avenida 21 de Janeiro, Morro Bento. Os preços serão disponibilizados na App. Estão sujeitos a alterações a qualquer momento antes ou após à compra. Os serviços e produtos são negociáveis. "
                pos_hint: {"center_x": .5, "center_y": .320}
                size_hint_x: .9
                font_size: (root.width**2 + root.height**2) / 14.5**4

                    
"""
)

class PayScreen(Screen):
    pass