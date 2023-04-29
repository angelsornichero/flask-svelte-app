from ..db.database import db

class User(db.Model):
    username = db.Column(db.String(16), primary_key=True)
    password = db.Column(db.String(76))
    email = db.Column(db.String(32))
    phone = db.Column(db.String(16))