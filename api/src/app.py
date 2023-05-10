from flask import Flask
from constants.main import PORT, SQL_URI
from db.database import db
from routes.auth import auth
from routes.routines import routines
from tasks.exercises import get_exercises


app = Flask(__name__)

# DB
app.config["SQLALCHEMY_DATABASE_URI"] = SQL_URI
db.init_app(app)

with app.app_context():
    db.create_all()
    get_exercises()

# Blueprints
app.register_blueprint(auth)
app.register_blueprint(routines)

if __name__ == "__main__":
   
   app.run(port=PORT, debug=True)

    