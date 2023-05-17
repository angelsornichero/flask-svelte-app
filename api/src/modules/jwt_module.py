import jwt
from constants.main import JWT_SECRET

class JwtModule:
    def encode_jwt(username):
        encoded_jwt = jwt.encode({"username": username}, JWT_SECRET, algorithm="HS256")
        return encoded_jwt
    
    def decode_jwt(self, token):
        decoded = jwt.decode(token, JWT_SECRET, algorithms="HS256")
        return decoded
    
    def get_user(self, token):
        decoded = self.decode_jwt(token)
        return decoded['username']
