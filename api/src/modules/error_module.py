

class ErrorResponse:
    
    def __init__(self, status_code = 500):
        self.status_code = status_code

    def custom_message(self, message):
        return { "message": message, "success": False }, self.status_code

    def no_authenticaded_response(self):
        return { "message": "[!] You must be authenticated", "success": False }, self.status_code
    
    def no_token(self):
        return { "message": "[!] A token expected", "succes": False }, self.status_code

    def missing_fields(self):
        return { "message": "[!] Some fields missing", "success": False }, self.status_code

    def routine_doesnt_exists(self):
        return { "message": "[!] Routine doesn't exists", "success": False }, self.status_code
    
    def routine_already_exists(self):
        return { "message": "[!] Routine already exists", "success": False }, self.status_code

    def exercise_doesnt_exits(self):
        return { "message": "[!] Exercise doesn't exists", "success": False }, self.status_code

    def invalid_credentials(self):
        return { "message": "[!] Invalid user or password", "success": False }, self.status_code