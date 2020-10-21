from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from functools import partial

from classes import ListIcon

Builder.load_string("""
<HomeScreen>:
    name: "home"
    NavigationLayout:
        id: nav_layout
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        id: tool_bar
                        title: "Home"
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.set_state()]]
                    ScreenManager:
                        id: screen_manager
        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"
                Image:
                    size_hint_y: .3
                    source: "logo.png"
                ScrollView:
                    MDList:
                        id: nav_list


""")


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

        from first_screen import FirstScreen
        from contact_screen import ContactScreen
        from privacy_screen import PrivacyScreen
        from term_screen import TermScreen
        from pay_screen import PayScreen
        from order import Order
        from page_info_screen import PageScreen

        self.list_screen = {
            FirstScreen: ('first_screen', 'Home', 'home'),
            PageScreen: ('page_screen','Meu Perfil','account'),
            PayScreen: ('pay', 'Métodos de Pagamento', 'cash'),
            Order: ('order', 'Minhas Marcações', 'plus'),
            PrivacyScreen: ('privacy', 'Políticas de Privacidade', 'lock'),
            TermScreen:('term', 'Termos de Uso', 'book-open'),
            ContactScreen: ('contact', 'Contactos', 'cellphone')

        }

    def on_enter(self):

        for screen, details in self.list_screen.items():
            identification, text, icon = details
            self.ids.screen_manager.add_widget(screen(name=identification))
            self.ids.nav_list.add_widget(
                ListIcon(text=text, icon=icon, on_release=partial(self.button_list_actions, text, identification)))

    def button_list_actions(self, title, identification):
        self.ids.tool_bar.title = title
        self.ids.screen_manager.current = identification
        self.ids.nav_drawer.set_state()
