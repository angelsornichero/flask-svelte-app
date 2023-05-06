from db.database import db

class Exercises(db.Model):
    body_part = db.Column(db.String(36))
    id = db.Column(db.String(36), primary_key=True)
    equipment = db.Column(db.String(36))
    gif_url = db.Column(db.String(76))
    name = db.Column(db.String(36))
    target = db.Column(db.String(36))

    def __init__(self, body_part, id, equipment, gif_url, name, target):
        self.body_part = body_part
        self.id = id
        self.equipment = equipment
        self.gif_url = gif_url
        self.name = name
        self.target = target