from db.database import db
from sqlalchemy.schema import ForeignKey
from datetime import datetime
class Routines(db.Model):
    name = db.Column(db.String(16))
    user = db.Column(ForeignKey('user.username'))
    label = db.Column(db.String(16))
    id = db.Column(db.Integer(), primary_key=True)
    timestamps = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    def __init__(self, name, user, label):
        self.name = name
        self.user = user
        self.label = label
        self.timestamps = datetime.now()

    