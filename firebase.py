import requests
import json
import uuid


from kivymd.app import MDApp

class Firebase():

    wak = "AIzaSyCFCnTYlHL9z6Y62y55TRAhEaXrhOXzcw8"

    @staticmethod
    def Signup(localId, first_name, last_name, cel_number, email):
        new_user_data = {
            'Nome': first_name,
            'Apelido': last_name,
            'Email': email,
            'Contacto': cel_number
        }
        post_request = requests.patch(
            f'https://austin-4bf29.firebaseio.com/users/{localId}.json',
            data=json.dumps(new_user_data)
        )

    def signup(self, email, password, name, last_name, cel_number):
        app = MDApp.get_running_app()

        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wak
        signup_payload = {
            "email": email,
            "password": password}
        signup_request = requests.post(signup_url, data=signup_payload)
        #print(sign_up_request.ok)
        #print(sign_up_request.content.decode())
        signup_data = json.loads(signup_request.content.decode())

        if signup_request.ok:
            self.Signup(signup_data["localId"], name, last_name, cel_number, email)
            Firebase().login(email, password)

        else:
            print(signup_data["error"]["message"])

    def login(self, email, password):
        app = MDApp.get_running_app()

        """Called if a user tried to sign up and their email already existed."""
        signin_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + self.wak
        signin_payload = {"email": email, "password": password, "returnSecureToken": True}
        signin_request = requests.post(signin_url, data=signin_payload)
        signin_data = json.loads(signin_request.content.decode())

        if signin_request.ok == True:
            refresh_token = signin_data['refreshToken']
            #localId = sign_up_data['localId']
            #idToken = sign_up_data['idToken']
            # Save refreshToken to a file
            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)

            login = app.root.current_screen
            from home_screen import HomeScreen
            self.home = HomeScreen()
            app.root.add_widget(self.home)
            app.root.current = "home"
            app.root.remove_widget(login)
            return True
        else:
            return signin_data["error"]["message"]

    def exchange_refresh_token(self, refresh_token):
        refresh_url = "https://securetoken.googleapis.com/v1/token?key=" + self.wak
        refresh_payload = '{"grant_type": "refresh_token", "refresh_token": "%s"}' % refresh_token
        refresh_req = requests.post(refresh_url, data=refresh_payload)
        id_token = refresh_req.json()['id_token']
        local_id = refresh_req.json()['user_id']
        return id_token, local_id

class Database():

    @staticmethod
    def add_order(first_name, place, date, hour, contact, service):
        n_request = uuid.uuid1()
        request_data = {
            "name": first_name,
            "localização": place,
            "data": date,
            "hora": hour,
            "número": contact,
            "Serviço": service,
        }

        post_request = requests.patch(
            f'https://austin-4bf29.firebaseio.com/Marcação/{n_request}.json',
            data=json.dumps(request_data)
        )

    @staticmethod
    def order_account(type_request):
        get_request = requests.get(f'https://austin-4bf29.firebaseio.com/users{type_request}.json')
        order_data = json.loads(get_request.content.decode())
        return order_data





