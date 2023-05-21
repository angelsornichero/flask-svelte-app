from flask import Blueprint
from flask import request
from modules.users_module import UserModule


class AuthRoutes:

    auth = Blueprint('auth', __name__)

    def __init__(self):
        @self.auth.route('/login', methods=['POST'])
        def login():
            try: 
                username = request.json.get('username')
                password = request.json.get('password')
            except AttributeError:
                return {}, 400

            return UserModule(username=username, password=password).login()
            

        @self.auth.route('/register',  methods=['POST'])
        def register():
            try:
                username = request.json.get('username')
                email = request.json.get('email')
                password = request.json.get('password')
                repeat_password = request.json.get('repeat_password')
            except AttributeError:
                return {}, 400
            
            return UserModule(username=username, password=password, email=email, repeat_password=repeat_password).register()
