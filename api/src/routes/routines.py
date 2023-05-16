from flask import Blueprint, request
import jwt
from constants.main import JWT_SECRET
from db.database import db
from models.routines import Routines
from modules.routines_module import RoutineModule


class RoutinesRoutes:

    routines = Blueprint('routines', __name__)

    def __init__(self):

        @self.routines.route('/new-routine', methods=['POST'])
        def create_routine():
            name = request.json.get('name')
            label = request.json.get('label')
            token = request.headers.get('authorization')

            return RoutineModule(name=name, label=label, token=token).create_routine_module()



        @self.routines.route('/routines', methods=['GET'])
        def get_routines():
            token = request.headers.get('authorization')

            return RoutineModule(token=token).get_routines_module()


        @self.routines.route('/routine/<routine_to_delete>', methods=['DELETE'])
        def delete_routine(routine_to_delete):
            token = request.headers.get('authorization')
            
            return RoutineModule(token=token).delete_routine_module(routine_to_delete=routine_to_delete)
            


        @self.routines.route('/routine/<routine_to_update>', methods=['PUT'])
        def update_routine(routine_to_update):
            name = request.json.get('name')
            label = request.json.get('label')
            token = request.headers.get('authorization')
            
            return RoutineModule(token=token, name=name, label=label).update_routine_module(routine_to_update=routine_to_update)
