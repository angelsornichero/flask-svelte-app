from flask import Flask
from constants.main import SQL_URI
from routes.auth import AuthRoutes
from routes.routines import RoutinesRoutes
from tasks.exercises import get_exercises
from db.database import db


class App:
    app = Flask(__name__)
    
    def __init__(self):
        self.init_db()
        self.init_app_context()
        self.blueprints()
    def init_db(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = SQL_URI
        db.init_app(self.app)
        
    def init_app_context(self):
        with self.app.app_context():
            db.create_all()
            get_exercises()

    def blueprints(self):
        self.app.register_blueprint(AuthRoutes().auth)
        self.app.register_blueprint(RoutinesRoutes().routines)
    
    def middlewares(self):
        def hola():
            return 'Jeje'
        self.app.before_request_funcs = {
            # blueprint name: [list_of_functions]
            'routines': [hola]
        }


    