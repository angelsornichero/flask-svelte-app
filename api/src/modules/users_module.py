from models.users import User
from db.database import db
from passlib.hash import pbkdf2_sha256 as hashgen
import jwt
from constants.main import JWT_SECRET


class UserModule:

    def __init__(self, username, password, email=None, repeat_password=None):
        self.username = username
        self.password = password
        self.email = email
        self.repeat_password = repeat_password

    def login(self): 
        if self.username is None or self.password is None:
                    return { "message": "[!] Please fill all fields", "success": False }, 401

        find_user = User.query.filter_by(username=self.username).first()

        if find_user is None:
            return { "message": "[!] Invalid user or password", "success": False }, 401
                
        verify = hashgen.verify(self.password, find_user.password)
        if not verify:
            return { "message": "[!] Invalid user or password", "success": False }, 401

        encoded_jwt = jwt.encode({"username": self.username}, JWT_SECRET, algorithm="HS256")

        return { "message": "[*] User logged in successfully", "success": True, "token": encoded_jwt }
    
    def register(self):
        if self.username is None or self.email is None or self.password is None or self.repeat_password is None:
                return { "message": "[!] Please fill all fields", "success": False }, 401

        if self.password != self.repeat_password:
                return { "message": "[!] Passwords do not match", "success": False }, 401

        find_user = User.query.filter_by(username=self.username).first()

        if find_user is not None:
            return { "message": "[!] User already exists", "success": False }, 401         
        hash = hashgen.hash(self.password)
        new_user = User(username=self.username, email=self.email, password=hash)
        db.session.add(new_user)
        db.session.commit()

        encoded_jwt = jwt.encode({"username": self.username}, JWT_SECRET, algorithm="HS256")

        return { "message": "[*] User resgistered successfully", "success": True, "token": encoded_jwt }