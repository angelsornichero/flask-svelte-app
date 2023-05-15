from flask import Blueprint, request
import jwt
from constants.main import JWT_SECRET
from db.database import db
from models.routines import Routines
from modules.routines_utils import create_routine_module, get_routines_module, delete_routine_module, update_routine_module


class RoutinesRoutes:

    routines = Blueprint('routines', __name__)

    def __init__(self):

        @self.routines.route('/new-routine', methods=['POST'])
        def create_routine():
            name = request.json.get('name')
            label = request.json.get('label')
            token = request.headers.get('authorization')

            return create_routine_module(name=name, label=label, token=token)



        @self.routines.route('/routines', methods=['GET'])
        def get_routines():
            token = request.headers.get('authorization')

            return get_routines_module(token=token)


        @self.routines.route('/routine/<routine_to_delete>', methods=['DELETE'])
        def delete_routine(routine_to_delete):
            token = request.headers.get('authorization')
            
            return delete_routine_module(token=token, routine_to_delete=routine_to_delete)
            


        @self.routines.route('/routine/<routine_to_update>', methods=['PUT'])
        def update_routine(routine_to_update):
            name = request.json.get('name')
            label = request.json.get('label')
            token = request.headers.get('authorization')
            
            return update_routine_module(routine_to_update=routine_to_update, token=token, name=name, label=label)
