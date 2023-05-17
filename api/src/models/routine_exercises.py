from db.database import db
from sqlalchemy.schema import ForeignKey

class Routines_Exercises(db.Model):
    body_part = db.Column(db.String(100))
    id = db.Column(db.Integer(), primary_key=True)
    equipment = db.Column(db.String(100))
    gif_url = db.Column(db.String(1000))
    name = db.Column(db.String(100))
    target = db.Column(db.String(100))
    routine_id = db.Column(ForeignKey('routines.id'))
    reps = db.Column(db.Integer())
    series = db.Column(db.Integer())

    def __init__(self, body_part, equipment, gif_url, name, target, routine_id, reps, series):
        self.body_part = body_part
        self.equipment = equipment
        self.gif_url = gif_url
        self.name = name
        self.target = target
        self.routine_id = routine_id
        self.reps = reps
        self.series = series