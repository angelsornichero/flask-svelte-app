from flask import Flask
from constants.main import PORT, SQL_URI
from db.database import db


app = Flask(__name__)

# DB
app.config["SQLALCHEMY_DATABASE_URI"] = SQL_URI
db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(port=PORT)