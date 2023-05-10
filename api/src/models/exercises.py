from db.database import db

class Exercises(db.Model):
    body_part = db.Column(db.String(100))
    id = db.Column(db.String(100), primary_key=True)
    equipment = db.Column(db.String(100))
    gif_url = db.Column(db.String(1000))
    name = db.Column(db.String(100))
    target = db.Column(db.String(100))

    def __init__(self, body_part, id, equipment, gif_url, name, target):
        self.body_part = body_part
        self.id = id
        self.equipment = equipment
        self.gif_url = gif_url
        self.name = name
        self.target = target