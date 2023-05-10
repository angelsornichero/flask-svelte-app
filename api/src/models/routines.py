from db.database import db
from sqlalchemy.schema import ForeignKey
from models.exercises import Exercises

class Routines(db.Model):
    name = db.Column(db.String(16))
    exercises = db.Column(db.ARRAY(ForeignKey('exercises.name')))
    user = db.Column(ForeignKey('user.username'))
    label = db.Column(db.String(16))

    def __init__(self, name, user, label):
        self.name = name
        self.user = user
        self.label = label

    