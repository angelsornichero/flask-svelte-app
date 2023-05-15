from flask import Blueprint
from flask import request
from models.users import User
from db.database import db
from passlib.hash import pbkdf2_sha256 as hashgen
import jwt
from constants.main import JWT_SECRET


class AuthRoutes:

    auth = Blueprint('auth', __name__)

    def __init__(self):
        
        print(self.auth)

        @self.auth.route('/login', methods=['POST'])
        def login():
            username = request.json.get('username')
            password = request.json.get('password')

            if username is None or password is None:
                return { "message": "[!] Please fill all fields", "success": False }, 401

            find_user = User.query.filter_by(username=username).first()

            if find_user is None:
                return { "message": "[!] Invalid user or password", "success": False }, 401
            
            verify = hashgen.verify(password, find_user.password)
            if not verify:
                return { "message": "[!] Invalid user or password", "success": False }, 401

            encoded_jwt = jwt.encode({"username": username}, JWT_SECRET, algorithm="HS256")

            return { "message": "[*] User logged in successfully", "success": True, "token": encoded_jwt }



        @self.auth.route('/register',  methods=['POST'])
        def register():
            username = request.json.get('username')
            email = request.json.get('email')
            password = request.json.get('password')
            repeat_password = request.json.get('repeat_password')

            if username is None or email is None or password is None or repeat_password is None:
                return { "message": "[!] Please fill all fields", "success": False }, 401

            if password != repeat_password:
                return { "message": "[!] Passwords do not match", "success": False }, 401

            find_user = User.query.filter_by(username=username).first()

            if find_user is not None:
                return { "message": "[!] User already exists", "success": False }, 401 
            
            hash = hashgen.hash(password)
            new_user = User(username=username, email=email, password=hash)
            db.session.add(new_user)
            db.session.commit()

            encoded_jwt = jwt.encode({"username": username}, JWT_SECRET, algorithm="HS256")

            return { "message": "[*] User resgistered successfully", "success": True, "token": encoded_jwt }
