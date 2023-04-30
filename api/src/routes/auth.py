from flask import Blueprint
from flask import request
from models.users import User
from db.database import db
from passlib.hash import pbkdf2_sha256 as hashgen

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "Login"



@auth.route('/register',  methods=['POST'])
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

    return { "message": "[*] User resgistered successfully", "success": True }