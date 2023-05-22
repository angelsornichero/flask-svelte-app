from flask import request
from modules.jwt_module import JwtModule
from modules.error_module import ErrorResponse
from functools import wraps

def is_authorithed(func):
    @wraps(func)
    def decorated_func(*args,**kwargs):
        try:
            token = request.headers.get('authorization')
        except AttributeError:
            return ErrorResponse(401).no_authenticaded_response()
        verified = JwtModule().verify_jwt(token=token)
        if verified == False:
            return ErrorResponse(401).no_authenticaded_response()
        
        return func(*args, **kwargs)
    return decorated_func