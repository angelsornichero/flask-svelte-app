from models.users import User
from db.database import db
from passlib.hash import pbkdf2_sha256 as hashgen
from modules.jwt_module import JwtModule
from modules.error_module import ErrorResponse

class UserModule:

    def __init__(self, username, password, email=None, repeat_password=None):
        self.username = username
        self.password = password
        self.email = email
        self.repeat_password = repeat_password

    def login(self): 
        if self.username is None or self.password is None:
            return ErrorResponse(400).missing_fields()
        find_user = User.query.filter_by(username=self.username).first()

        if find_user is None:
            return ErrorResponse(401).invalid_credentials()
                
        verify = hashgen.verify(self.password, find_user.password)
        if not verify:
            return ErrorResponse(401).invalid_credentials()

        

        return { "message": "[*] User logged in successfully", "success": True, "token": JwtModule.encode_jwt(self.username) }
    
    def register(self):
        if self.username is None or self.email is None or self.password is None or self.repeat_password is None:
                return ErrorResponse(400).missing_fields()

        if self.password != self.repeat_password:
                return ErrorResponse(401).custom_message("[!] Passwords do not match")

        find_user = User.query.filter_by(username=self.username).first()

        if find_user is not None:
            return ErrorResponse(401).custom_message("[!] User already exists")         
        hash = hashgen.hash(self.password)
        new_user = User(username=self.username, email=self.email, password=hash)
        db.session.add(new_user)
        db.session.commit()

        return { "message": "[*] User resgistered successfully", "success": True, "token": JwtModule.encode_jwt(self.username) }