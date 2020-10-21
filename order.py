from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.uix.screen import MDScreen
from firebase import Database

Builder.load_string('''
<AddRequestDialog>
    orientation: "vertical"
    spacing: "8dp"
    size_hint_y: None
    height: "320dp"
    MDTextField:
        id: first_name
        hint_text: "Nome"
    MDTextField:
        id: place
        hint_text: "Localização"
    MDTextField:
        id: service
        hint_text: "Serviço"
    MDTextField:
        id: contact
        hint_text: "Contacto"

    MDBoxLayout:
        orientation: "horizontal"
        MDLabel:
            id: date_label
            size_hint_x: .9
            text: "Data"
            theme_text_color: "Secondary"

        MDIconButton:
            id: date_picker
            size_hint_x: .2
            icon: "calendar-edit"
    MDBoxLayout:
        orientation: "horizontal"

        MDLabel:
            id: hour_label
            size_hint_x: .9
            text: "Hora"
            theme_text_color: "Secondary"

        MDIconButton:
            id: hour_picker
            size_hint_x: .2
            icon: "clock"

<Order>:
    add_request_button: add_request_button
    
    FloatLayout:
        Image:
            size_hint_y: .2
            source: "logo.png"
            pos_hint: {"center_x": .5, "center_y": .8}
        MDLabel:
            text: "Pressione '+' Para Fazer A Sua Marcação!"
            size_hint_x: .9
            pos_hint: {"center_x": .5, "center_y": .2}
            theme_text_color: "Error"
        MDLabel:
            text: "Ajude-nos a ajudar-te!"
            size_hint_x: .9
            pos_hint: {"center_x": .5, "center_y": .1}
            theme_text_color: "Hint"
            
    MDFloatingActionButton:
        id: add_request_button
        icon: "plus"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .85, "center_y": .1}
'''
                    )

APP = MDApp.get_running_app()
DATABASE = Database()


class AddRequestDialog(MDBoxLayout):
    def __init__(self, **kw):
        super().__init__()
        self.ids.hour_picker.on_release = kw["hour_picker"]
        self.ids.date_picker.on_release = kw['date_picker']


class Order(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)

        self.add_request_dialog = None
        self.content = None
        # Data
        self.first_name = None
        self.place = None
        self.hour = None
        self.contact = int
        self.service = None

    def on_pre_enter(self, *args):
        self.add_request_button.bind(on_release=self.show_add_request_dialog)

    def show_add_request_dialog(self, instance_button):

        if not self.add_request_dialog:
            self.add_request_dialog = MDDialog(
                size_hint=(.8, .7),
                type="custom",
                content_cls=AddRequestDialog(hour_picker=self.show_time_picker, date_picker=self.show_date_picker),
                buttons=[
                    MDFlatButton(
                        text="CANCELAR",
                        text_color=APP.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="MARCAR", text_color=APP.theme_cls.primary_color,
                        on_release=self.add_request
                    ),
                ],
            )
        self.content = self.add_request_dialog.ids.spacer_top_box.children[0]
        self.add_request_dialog.open()

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def get_date(self, date):
        self.content.ids.date_label.color = APP.theme_cls.primary_color
        self.content.ids.date_label.text = date.strftime("%d/%m/%Y")

    def show_time_picker(self):
        """Open time picker dialog."""
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        self.content.ids.hour_label.color = APP.theme_cls.primary_color
        self.content.ids.hour_label.text = time.strftime("%H:%M")

    def add_request(self, button):
        self.first_name = self.content.ids.first_name.text
        self.place = self.content.ids.place.text
        self.service = self.content.ids.service.text
        self.date = self.content.ids.date_label.text
        self.hour = self.content.ids.hour_label.text
        self.contact = self.content.ids.contact.text

        if (self.first_name and self.place and self.contact != "" and
                self.date != "Data" and self.hour != "Hora" and self.service != ""):
            DATABASE.add_order(
                self.first_name, self.place, self.date, self.hour,
                self.contact, self.service,
            )
            self.close_dialog("")
        else:
            print("Deves completar todos os dados")

    def close_dialog(self, button):
        self.add_request_dialog.dismiss()
        self.add_request_dialog = None