from db.database import db

class User(db.Model):
    username = db.Column(db.String(16), primary_key=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(32))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email